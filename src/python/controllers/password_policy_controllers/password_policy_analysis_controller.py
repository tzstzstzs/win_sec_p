import logging
from src.python.view.password_policy_view.password_policy_analysis_window import PasswordPolicyAnalysisWindow
from src.python.models.password_policy_models.password_policy_analysis_service import PasswordPolicyAnalysisService
from src.python.view.password_policy_view.password_policy_settings_window import PasswordPolicySettingsWindow
from tkinter import messagebox
from src.python.controllers.base_analysis_controller import BaseAnalysisController


class PasswordPolicyAnalysisController(BaseAnalysisController):
    def __init__(self, main_window):
        super().__init__(main_window, 'password_policy')

    def perform_analysis(self, policy_data):
        logging.info("Attempting to analyze password policy [controller].")
        try:
            # Pass the current settings to the analysis service
            analysis_service = PasswordPolicyAnalysisService(policy_data, self.analysis_settings)
            self.analysis_results = analysis_service.analyze()
            self.main_window.enable_button(self.main_window.password_policy_section[4])
            logging.info("Successfully analyzed password policy [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze password policy [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing password policy: {e}")
            return None

    def show_analysis_results(self):
        if self.analysis_results:
            try:
                PasswordPolicyAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying password policy analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the password policy analysis.")
        else:
            logging.warning("No password policy analysis data available to display [controller].")
            messagebox.showinfo("Password Policy Analysis", "No password policy analysis data available.")

    def open_settings_window(self):
        super().open_settings_window(PasswordPolicySettingsWindow, 'password_policy')

    def save_analysis_settings(self, settings):
        self.settings_manager.update_setting('password_policy', settings)
        self.password_policy_settings = settings
        logging.info(f"Password policy settings saved: {self.password_policy_settings}")