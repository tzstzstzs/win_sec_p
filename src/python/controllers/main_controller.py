from src.python.view.main_window import MainWindow
from src.python.models.user_service import get_windows_users_with_powershell
from src.python.models.process_service import get_running_processes_with_psutil
from src.python.view.user_list_window import UserListWindow
from src.python.view.process_list_window import ProcessListWindow
from tkinter import messagebox


class MainController:
    def __init__(self):
        self.main_window = MainWindow(self)
        self.users_data = []
        self.processes_data = []

    def run(self):
        self.main_window.mainloop()

    def retrieve_users(self):
        try:
            self.users_data = get_windows_users_with_powershell()
            self.main_window.enable_user_list_button()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to retrieve user data: {e}")

    def retrieve_processes(self):
        try:
            self.processes_data = get_running_processes_with_psutil()
            self.main_window.enable_process_list_button()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to retrieve running processes: {e}")

    def show_users(self):
        if self.users_data:
            UserListWindow(self.main_window, self.users_data)

    def show_processes(self):
        if self.processes_data:
            ProcessListWindow(self.main_window, self.processes_data)

    def show_option3(self):
        # Placeholder for showing results of Option 3
        messagebox.showinfo("Info", "Option 3 functionality not yet implemented.")
