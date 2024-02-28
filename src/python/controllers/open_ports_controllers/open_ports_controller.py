import logging
from src.python.view.open_ports_view.open_ports_list_window import PortListWindow
from src.python.models.open_ports_models.open_ports_service import get_active_ports_with_powershell
from tkinter import messagebox


class PortController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ports_data = []

    def retrieve_ports(self):
        logging.info("Attempting to retrieve port data [controller].")
        try:
            self.ports_data = get_active_ports_with_powershell()
            self.main_window.enable_button(self.main_window.port_list_section[2])
            logging.info("Successfully retrieved port data [controller].")
            return self.ports_data
        except Exception as e:
            logging.error(f"Failed to retrieve port data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving port data: {e}")
            return None

    def show_ports(self):
        if self.ports_data:
            try:
                PortListWindow(self.main_window, self.ports_data)
            except Exception as e:
                logging.error(f"Error displaying port list [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the port list.")
        else:
            logging.warning("No port data available to display [controller].")
            messagebox.showinfo("Port List", "No port data available.")
