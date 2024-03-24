import logging
from src.python.view.installed_updates_view.updates_analysis_window import UpdatesAnalysisWindow
from src.python.models.installed_updates_models.updates_analysis_service import UpdatesAnalysisService
from src.python.view.installed_updates_view.updates_analysis_settings_window import UpdatesAnalysisSettingsWindow
from tkinter import messagebox
from src.python.controllers.base_analysis_controller import BaseAnalysisController


class UpdatesAnalysisController(BaseAnalysisController):
    def __init__(self, main_window):
        super().__init__(main_window, 'authorized_updates')

    def perform_analysis(self, installed_updates_data):
        logging.info("Attempting to analyze installed updates data [controller].")
        try:
            # Pass the installed updates data to the analysis service
            analysis_service = UpdatesAnalysisService(installed_updates_data, self.analysis_settings)
            self.analysis_results = analysis_service.analyze()
            self.main_window.enable_button(self.main_window.installed_updates_section[4])
            logging.info("Successfully analyzed installed updates data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze installed updates data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing installed updates data: {e}")
            return None

    def show_analysis_results(self):
        if self.analysis_results:
            try:
                UpdatesAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying updates analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the updates analysis.")
        else:
            logging.warning("No updates analysis data available to display [controller].")
            messagebox.showinfo("Updates Analysis", "No updates analysis data available.")

    def open_settings_window(self):
        super().open_settings_window(UpdatesAnalysisSettingsWindow, 'authorized_updates')

    def save_analysis_settings(self, settings):
        self.settings_manager.update_setting('authorized_updates', settings)
        self.updates_analysis_settings = settings
        logging.info(f"Updates analysis settings saved: {self.updates_analysis_settings}")
