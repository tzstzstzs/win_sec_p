from src.python.view.user_list_window import UserListWindow
from src.python.models.user_service import get_windows_users_with_powershell
from tkinter import messagebox


class UserController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.users_data = []

    def retrieve_users(self):
        try:
            self.users_data = get_windows_users_with_powershell()
            self.main_window.enable_user_list_button()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to retrieve user data: {e}")

    def show_users(self):
        if self.users_data:
            UserListWindow(self.main_window, self.users_data)
