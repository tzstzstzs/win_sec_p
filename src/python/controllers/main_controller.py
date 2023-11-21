from src.python.view.main_window import MainWindow
from src.python.models.user_service import get_windows_users_with_powershell
from src.python.models.process_service import get_running_processes_with_psutil
from src.python.view.user_list_window import UserListWindow
from src.python.view.process_list_window import ProcessListWindow
from src.python.models import port_service
from src.python.view.port_list_window import PortListWindow
from tkinter import messagebox
import threading


class MainController:
    def __init__(self):
        self.main_window = MainWindow(self)
        self.users_data = []
        self.processes_data = []
        self.open_ports_data = []

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
        start_port = 8070
        end_port = 8080
        host = '127.0.0.1'
        self.main_window.start_progress(end_port - start_port + 1)

        # Run the scan in a separate thread to prevent UI freezing
        threading.Thread(
            target=port_service.run_port_scan,
            args=(
                host,
                start_port,
                end_port,
                self.main_window.update_progress,
                self.complete_port_scan,
                self.error_port_scan
            ),
            daemon=True  # This makes sure the thread will close when the main application exits
        ).start()

    def complete_port_scan(self, open_ports):
        # This function will be called once scanning is complete
        # Since it updates the GUI, it should schedule the changes in the main thread
        self.open_ports_data = open_ports
        self.main_window.stop_progress()
        self.main_window.enable_checkports_button()

    def error_port_scan(self, error):
        # This function will be called if there's an error during scanning
        # Error handling code goes here
        self.main_window.stop_progress()
        messagebox.showerror("Error", f"Unable to complete port scan: {error}")

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
