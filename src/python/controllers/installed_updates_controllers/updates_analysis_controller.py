import logging
from src.python.view.installed_updates_view.updates_analysis_window import UpdatesAnalysisWindow
from src.python.models.installed_updates_models.updates_analysis_service import UpdatesAnalysisService
from src.python.view.installed_updates_view.updates_analysis_settings_window import UpdatesAnalysisSettingsWindow
from src.python.models.settings_manager import SettingsManager
from tkinter import messagebox


class UpdatesAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []
        self.settings_manager = SettingsManager()
        self.updates_analysis_settings = self.settings_manager.get_setting('authorized_updates')
        self.settings_window = None

    def perform_updates_analysis(self, installed_updates_data):
        logging.info("Attempting to analyze installed updates data [controller].")
        try:
            # Pass the installed updates data to the analysis service
            analysis_service = UpdatesAnalysisService(installed_updates_data, self.updates_analysis_settings)
            self.analysis_results = analysis_service.analyze_updates()
            self.main_window.enable_button(self.main_window.installed_updates_section[4])
            logging.info("Successfully analyzed installed updates data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze installed updates data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing installed updates data: {e}")
            return None

    def show_updates_analysis(self):
        if self.analysis_results:
            try:
                UpdatesAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying updates analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the updates analysis.")
        else:
            logging.warning("No updates analysis data available to display [controller].")
            messagebox.showinfo("Updates Analysis", "No updates analysis data available.")

    def open_updates_analysis_settings(self):
        # Check if the settings window is already open
        if not self.settings_window or not self.settings_window.winfo_exists():
            current_settings = self.settings_manager.get_setting('authorized_updates')
            self.settings_window = UpdatesAnalysisSettingsWindow(
                self.main_window,
                save_callback=self.save_updates_analysis_settings,
                defaults=current_settings
            )
            self.settings_window.grab_set()
        else:
            # Bring the existing settings window to focus
            self.settings_window.focus_set()

    def save_updates_analysis_settings(self, settings):
        # Save the updated 'authorized_updates' settings
        self.settings_manager.update_setting('authorized_updates', settings)
        self.updates_analysis_settings = settings
        logging.info(f"Updates analysis settings saved: {self.updates_analysis_settings}")
