from src.python.view.port_list_window import PortListWindow
from src.python.models import port_service
from tkinter import messagebox
import threading


class PortController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.open_ports_data = []

    def check_ports(self):
        start_port = 8070
        end_port = 8080
        host = '127.0.0.1'
        self.main_window.start_progress(end_port - start_port + 1)

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
            daemon=True
        ).start()

    def complete_port_scan(self, open_ports):
        self.open_ports_data = open_ports
        self.main_window.stop_progress()
        self.main_window.enable_checkports_button()

    def error_port_scan(self, error):
        self.main_window.stop_progress()
        messagebox.showerror("Error", f"Unable to complete port scan: {error}")

    def show_open_ports(self):
        if self.open_ports_data:
            PortListWindow(self.main_window, self.open_ports_data)
        else:
            messagebox.showinfo("Open Ports", "No open ports found.")
