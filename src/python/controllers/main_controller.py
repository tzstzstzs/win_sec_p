from src.python.view.main_window import MainWindow
from src.python.models.user_service import get_windows_users_with_powershell
from src.python.models.process_service import get_running_processes_with_psutil
from src.python.view.user_list_window import UserListWindow
from src.python.view.process_list_window import ProcessListWindow
from src.python.models import port_service
from src.python.view.port_list_window import PortListWindow
from tkinter import messagebox


class MainController:
    def __init__(self):
        self.main_window = MainWindow(self)
        self.users_data = []
        self.processes_data = []
        self.open_ports_data = None

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

    def check_ports(self):
        # Define the range of ports you want to scan
        start_port = 20
        end_port = 100
        host = '127.0.0.1'  # Local host
        try:
            self.open_ports_data = port_service.scan_open_ports(host, start_port, end_port)
            self.main_window.enable_checkports_button()
        except KeyboardInterrupt:
            messagebox.showinfo("Port Scan", "Port scan was cancelled by the user.")
        except Exception as e:
            messagebox.showerror("Port Scan", f"An error occurred: {e}")

    def show_users(self):
        if self.users_data:
            UserListWindow(self.main_window, self.users_data)

    def show_processes(self):
        if self.processes_data:
            ProcessListWindow(self.main_window, self.processes_data)

    def show_open_ports(self):
        if self.open_ports_data:
            PortListWindow(self.main_window, self.open_ports_data)
        else:
            messagebox.showinfo("Open Ports", "No open ports found.")
