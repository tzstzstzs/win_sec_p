import logging
from src.python.view.password_policy_analysis_window import PasswordPolicyResultWindow
from src.python.models.password_policy_analysis_service import PasswordPolicyAnalysisService
from tkinter import messagebox


class PasswordPolicyAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []

    def perform_password_policy_analysis(self, policy_data):
        logging.info("Attempting to analyze password policy [controller].")
        try:
            self.analysis_results = PasswordPolicyAnalysisService(policy_data).analyze_password_policy()
            self.main_window.enable_button(self.main_window.password_policy_section[4])
            logging.info("Successfully analyzed password policy [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze password policy [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing password policy: {e}")
            return None

    def show_password_policy_analysis(self):
        if self.analysis_results:
            try:
                PasswordPolicyResultWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying password policy analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the password policy analysis.")
        else:
            logging.warning("No password policy analysis data available to display [controller].")
            messagebox.showinfo("Password Policy Analysis", "No password policy analysis data available.")
