import logging
from src.python.view.password_policy_window import PasswordPolicyWindow
from src.python.models.password_policy_service import get_password_policy
from tkinter import messagebox

# Initialize logging at the start of the application
logging.basicConfig(level=logging.INFO, filename='password.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class PasswordPolicyController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.policy_data = []

    def retrieve_password_policy(self):
        logging.info("Attempting to retrieve password policy.")
        try:
            self.policy_data = get_password_policy()
            self.main_window.enable_button(self.main_window.show_policy_button)
            # Trigger any UI update or enablement here
            logging.info("Successfully retrieved password policy.")
        except Exception as e:
            logging.error(f"Failed to retrieve password policy: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving password policy: {e}")

    def show_password_policy(self):
        if self.policy_data:
            try:
                PasswordPolicyWindow(self.main_window, self.policy_data)
            except Exception as e:
                logging.error(f"Error displaying password policy: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the password policy.")
        else:
            logging.warning("No password policy data available to display.")
            messagebox.showinfo("Password Policy", "No password policy data available.")
