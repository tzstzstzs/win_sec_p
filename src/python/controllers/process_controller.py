import logging
from src.python.view.process_list_window import ProcessListWindow
from src.python.models.process_service import get_running_processes_with_psutil
from tkinter import messagebox


class ProcessController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.processes_data = []

    def retrieve_processes(self):
        logging.info("Attempting to retrieve running processes [controller].")
        try:
            self.processes_data = get_running_processes_with_psutil()
            self.main_window.enable_button(self.main_window.running_processes_section[2])
            logging.info("Successfully retrieved running processes [controller].")
        except Exception as e:
            logging.error(f"Failed to retrieve running processes: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving running processes: {e}")

    def show_processes(self):
        if self.processes_data:
            try:
                ProcessListWindow(self.main_window, self.processes_data)
            except Exception as e:
                logging.error(f"Error displaying process list: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the process list.")
        else:
            logging.warning("No process data available to display.")
            messagebox.showinfo("Process List", "No process data available.")
