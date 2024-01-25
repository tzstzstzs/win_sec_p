import logging
from src.python.view.password_policy_analysis_window import PasswordPolicyResultWindow
from src.python.models.password_policy_analysis_service import PasswordPolicyAnalysisService
from src.python.view.password_policy_settings_window import PasswordPolicySettingsWindow
from tkinter import messagebox


class PasswordPolicyAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []
        # Default settings for password policy
        self.default_settings = {
            'logoff_time': '30',
            'min_length': '8',
            'max_age': '90',
            'min_age': '1',
            'history': '5',
            'lockout_threshold': '5',
            'lockout_duration': '30',
            'lockout_obs_win': '30'
        }
        # Dictionary to store actual settings
        self.password_policy_settings = {}

    def perform_password_policy_analysis(self, policy_data):
        logging.info("Attempting to analyze password policy [controller].")
        try:
            # Pass the current settings to the analysis service
            analysis_service = PasswordPolicyAnalysisService(policy_data, self.password_policy_settings)
            self.analysis_results = analysis_service.analyze_password_policy()
            self.main_window.enable_button(self.main_window.password_policy_section[4])
            logging.info("Successfully analyzed password policy [controller].")
            print(self.analysis_results)
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

    def open_password_policy_settings(self):
        # Open the settings window
        self.settings_window = PasswordPolicySettingsWindow(
            self.main_window,
            save_callback=self.save_password_policy_settings,
            defaults=self.default_settings
        )
        self.settings_window.grab_set()  # Make the settings window modal

    def save_password_policy_settings(self, settings):
        self.password_policy_settings = settings
        logging.info(f"Password policy settings saved: {self.password_policy_settings}")