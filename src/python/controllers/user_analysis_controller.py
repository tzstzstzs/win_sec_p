import logging
from src.python.view.user_analysis_window import UserAnalysisWindow
from src.python.models.user_analysis_service import UserAnalysisService
from src.python.view.user_analysis_settings_window import UserAnalysisSettingsWindow
from tkinter import messagebox


class UserAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []
        # Default settings for user analysis
        self.default_users = {
            "Alapértelmezett fiók",
            "Rendszergazda",
            "Vendég",
            "VDAGUtilityAccount"
            "test_project1"
        }
        # List to store actual settings
        self.user_analysis_settings = self.default_users

    def perform_user_analysis(self, user_data):
        logging.info("Attempting to analyze user data [controller].")
        try:
            # Pass the user data to the analysis service
            analysis_service = UserAnalysisService(user_data, self.user_analysis_settings)
            self.analysis_results = analysis_service.analyze_users()
            self.main_window.enable_button(self.main_window.user_list_section[4])
            logging.info("Successfully analyzed user data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze user data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing user data: {e}")
            return None

    def show_user_analysis(self):
        if self.analysis_results:
            try:
                UserAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying user analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the user analysis.")
        else:
            logging.warning("No user analysis data available to display [controller].")
            messagebox.showinfo("User Analysis", "No user analysis data available.")

    def open_user_analysis_settings(self):
        self.settings_window = UserAnalysisSettingsWindow(
            self.main_window,
            save_callback=self.save_user_analysis_settings,
            defaults=self.default_users
        )
        self.settings_window.grab_set()  # Make the settings window modal

    def save_user_analysis_settings(self, settings):
        self.user_analysis_settings = settings
        logging.info(f"User analysis settings saved: {self.user_analysis_settings}")