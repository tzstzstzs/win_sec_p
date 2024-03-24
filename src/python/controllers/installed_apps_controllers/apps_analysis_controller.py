import logging
from src.python.view.installed_apps_view.apps_analysis_window import AppsAnalysisWindow
from src.python.models.installed_apps_models.apps_analysis_service import AppsAnalysisService
from src.python.view.installed_apps_view.apps_analysis_settings_window import AppsAnalysisSettingsWindow
from tkinter import messagebox
from src.python.controllers.base_analysis_controller import BaseAnalysisController


class AppsAnalysisController(BaseAnalysisController):
    def __init__(self, main_window):
        super().__init__(main_window, 'authorized_apps')

    def perform_analysis(self, installed_apps_data):
        logging.info("Attempting to analyze installed apps data [controller].")
        try:
            # Pass the installed apps data to the analysis service
            analysis_service = AppsAnalysisService(installed_apps_data, self.analysis_settings)
            self.analysis_results = analysis_service.analyze()
            self.main_window.enable_button(self.main_window.installed_apps_section[4])
            logging.info("Successfully analyzed installed apps data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze installed apps data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing installed apps data: {e}")
            return None

    def show_analysis_results(self):
        if self.analysis_results:
            try:
                AppsAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying apps analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the apps analysis.")
        else:
            logging.warning("No apps analysis data available to display [controller].")
            messagebox.showinfo("Apps Analysis", "No apps analysis data available.")

    def open_settings_window(self):
        super().open_settings_window(AppsAnalysisSettingsWindow, 'authorized_apps')

    def save_analysis_settings(self, settings):
        self.settings_manager.update_setting('authorized_apps', settings)
        self.apps_analysis_settings = settings
        logging.info(f"Apps analysis settings saved: {self.apps_analysis_settings}")
