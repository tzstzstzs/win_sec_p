import logging
from src.python.view.password_policy_view.password_policy_window import PasswordPolicyWindow
from src.python.models.password_policy_models.password_policy_service import get_password_policy
from tkinter import messagebox
from src.python.controllers.base_controller import BaseController


class PasswordPolicyController(BaseController):
    def retrieve_data(self):
        logging.info("Attempting to retrieve password policy [controller].")
        try:
            self.data = get_password_policy()
            self.main_window.enable_button(self.main_window.password_policy_section[2])
            logging.info("Successfully retrieved password policy [controller].")
            return self.data
        except Exception as e:
            logging.error(f"Failed to retrieve password policy [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving password policy: {e}")
            return None

    def show_data(self):
        if self.data:
            try:
                PasswordPolicyWindow(self.main_window, self.data)
            except Exception as e:
                logging.error(f"Error displaying password policy [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the password policy.")
        else:
            logging.warning("No password policy data available to display [controller].")
            messagebox.showinfo("Password Policy", "No password policy data available.")
