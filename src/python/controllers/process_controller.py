from src.python.view.process_list_window import ProcessListWindow
from src.python.models.process_service import get_running_processes_with_psutil
from tkinter import messagebox

class ProcessController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.processes_data = []

    def retrieve_processes(self):
        try:
            self.processes_data = get_running_processes_with_psutil()
            self.main_window.enable_process_list_button()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to retrieve running processes: {e}")

    def show_processes(self):
        if self.processes_data:
            ProcessListWindow(self.main_window, self.processes_data)
