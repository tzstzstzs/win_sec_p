import logging
from src.python.view.installed_apps_view.apps_analysis_window import AppsAnalysisWindow
from src.python.models.installed_apps_models.apps_analysis_service import AppsAnalysisService
from src.python.view.installed_apps_view.apps_analysis_settings_window import AppsAnalysisSettingsWindow
from src.python.models.settings_manager import SettingsManager
from tkinter import messagebox


class AppsAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []
        self.settings_manager = SettingsManager()
        self.apps_analysis_settings = self.settings_manager.get_setting('authorized_apps')
        self.settings_window = None

    def perform_apps_analysis(self, installed_apps_data):
        logging.info("Attempting to analyze installed apps data [controller].")
        try:
            # Pass the installed apps data to the analysis service
            analysis_service = AppsAnalysisService(installed_apps_data, self.apps_analysis_settings)
            self.analysis_results = analysis_service.analyze_apps()
            self.main_window.enable_button(self.main_window.installed_apps_section[4])
            logging.info("Successfully analyzed installed apps data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze installed apps data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing installed apps data: {e}")
            return None

    def show_apps_analysis(self):
        if self.analysis_results:
            try:
                AppsAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying apps analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the apps analysis.")
        else:
            logging.warning("No apps analysis data available to display [controller].")
            messagebox.showinfo("Apps Analysis", "No apps analysis data available.")

    def open_apps_analysis_settings(self):
        # Check if the settings window is already open
        if not self.settings_window or not self.settings_window.winfo_exists():
            current_settings = self.settings_manager.get_setting('authorized_apps')
            self.settings_window = AppsAnalysisSettingsWindow(
                self.main_window,
                save_callback=self.save_apps_analysis_settings,
                defaults=current_settings
            )
            self.settings_window.grab_set()
        else:
            # Bring the existing settings window to focus
            self.settings_window.focus_set()

    def save_apps_analysis_settings(self, settings):
        # Save the updated 'authorized_apps' settings
        self.settings_manager.update_setting('authorized_apps', settings)
        self.apps_analysis_settings = settings
        logging.info(f"Apps analysis settings saved: {self.apps_analysis_settings}")
