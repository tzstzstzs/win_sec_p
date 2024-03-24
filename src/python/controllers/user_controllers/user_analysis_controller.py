import logging
from src.python.view.user_view.user_analysis_window import UserAnalysisWindow
from src.python.models.user_models.user_analysis_service import UserAnalysisService
from src.python.view.user_view.user_analysis_settings_window import UserAnalysisSettingsWindow
from tkinter import messagebox
from src.python.controllers.base_analysis_controller import BaseAnalysisController


class UserAnalysisController(BaseAnalysisController):
    def __init__(self, main_window):
        super().__init__(main_window, 'default_users')

    def perform_analysis(self, user_data):
        logging.info("Attempting to analyze user data [controller].")
        try:
            # Pass the user data to the analysis service
            analysis_service = UserAnalysisService(user_data, self.analysis_settings)
            self.analysis_results = analysis_service.analyze()
            self.main_window.enable_button(self.main_window.user_list_section[4])
            logging.info("Successfully analyzed user data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze user data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing user data: {e}")
            return None

    def show_analysis_results(self):
        if self.analysis_results:
            try:
                UserAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying user analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the user analysis.")
        else:
            logging.warning("No user analysis data available to display [controller].")
            messagebox.showinfo("User Analysis", "No user analysis data available.")

    def open_settings_window(self):
        super().open_settings_window(UserAnalysisSettingsWindow, 'default_users')

    def save_analysis_settings(self, settings):
        self.settings_manager.update_setting('default_users', settings)
        self.user_analysis_settings = settings
        logging.info(f"User analysis settings saved: {self.user_analysis_settings}")
