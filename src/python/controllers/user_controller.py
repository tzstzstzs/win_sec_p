import logging
from src.python.view.user_list_window import UserListWindow
from src.python.models.user_service import get_windows_users_with_powershell
from tkinter import messagebox


class UserController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.users_data = []

    def retrieve_users(self):
        logging.info("Attempting to retrieve user data [controller].")
        try:
            self.users_data = get_windows_users_with_powershell()
            self.main_window.enable_button(self.main_window.user_list_section[2])
            logging.info("Successfully retrieved user data [controller].")
            return self.users_data
        except Exception as e:
            logging.error(f"Failed to retrieve user data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving user data: {e}")
            return None

    def show_users(self):
        if self.users_data:
            try:
                UserListWindow(self.main_window, self.users_data)
            except Exception as e:
                logging.error(f"Error displaying user list [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the user list.")
        else:
            logging.warning("No user data available to display [controller].")
            messagebox.showinfo("User List", "No user data available.")
