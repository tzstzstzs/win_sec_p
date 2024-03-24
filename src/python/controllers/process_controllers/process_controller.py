import logging
from src.python.view.process_view.process_list_window import ProcessListWindow
from src.python.models.process_models.process_service import get_running_processes
from tkinter import messagebox
from src.python.controllers.base_controller import BaseController


class ProcessController(BaseController):
    def retrieve_data(self):
        logging.info("Attempting to retrieve running processes [controller].")
        try:
            self.data = get_running_processes()
            self.main_window.enable_button(self.main_window.running_processes_section[2])
            logging.info("Successfully retrieved running processes [controller].")
            return self.data
        except Exception as e:
            logging.error(f"Failed to retrieve running processes [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving running processes [controller]: {e}")
            return None

    def show_data(self):
        if self.data:
            try:
                ProcessListWindow(self.main_window, self.data)
            except Exception as e:
                logging.error(f"Error displaying running processes [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying running processes.")
        else:
            logging.warning("No running processes data available to display [controller].")
            messagebox.showinfo("Running Processes", "No running processes data available.")
