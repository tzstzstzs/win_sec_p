import logging
from src.python.view.user_analysis_window import UserAnalysisWindow
from src.python.models.user_analysis_service import UserAnalysisService
from tkinter import messagebox


class UserAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []

    def perform_user_analysis(self, user_data):
        logging.info("Attempting to analyze user data [controller].")
        try:
            # Pass the user data to the analysis service
            analysis_service = UserAnalysisService(user_data)
            self.analysis_results = analysis_service.analyze_users()
            self.main_window.enable_button(self.main_window.user_list_section[4])  # Adjust the index as per the main window design
            logging.info("Successfully analyzed user data [controller].")
            print(self.analysis_results)
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
