import logging
from src.python.view.password_policy_view.password_policy_analysis_window import PasswordPolicyAnalysisWindow
from src.python.models.password_policy_models.password_policy_analysis_service import PasswordPolicyAnalysisService
from src.python.view.password_policy_view.password_policy_settings_window import PasswordPolicySettingsWindow
from src.python.models.settings_manager import SettingsManager
from tkinter import messagebox


class PasswordPolicyAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []
        self.settings_manager = SettingsManager()
        # Load 'password_policy' settings using SettingsManager
        self.password_policy_settings = self.settings_manager.get_setting('password_policy')
        self.settings_window = None

    def perform_password_policy_analysis(self, policy_data):
        logging.info("Attempting to analyze password policy [controller].")
        try:
            # Pass the current settings to the analysis service
            analysis_service = PasswordPolicyAnalysisService(policy_data, self.password_policy_settings)
            self.analysis_results = analysis_service.analyze_password_policy()
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
                PasswordPolicyAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying password policy analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the password policy analysis.")
        else:
            logging.warning("No password policy analysis data available to display [controller].")
            messagebox.showinfo("Password Policy Analysis", "No password policy analysis data available.")

    def open_password_policy_settings(self):
        # Check if the settings window is already open
        if not self.settings_window or not self.settings_window.winfo_exists():
            current_settings = self.settings_manager.get_setting('password_policy')
            self.settings_window = PasswordPolicySettingsWindow(
                self.main_window,
                save_callback=self.save_password_policy_settings,
                defaults=current_settings
            )
            self.settings_window.grab_set()
        else:
            # Bring the existing settings window to focus
            self.settings_window.focus_set()

    def save_password_policy_settings(self, settings):
        # Save the updated 'password_policy' settings
        self.settings_manager.update_setting('password_policy', settings)
        self.password_policy_settings = settings
        logging.info(f"Password policy settings saved: {self.password_policy_settings}")