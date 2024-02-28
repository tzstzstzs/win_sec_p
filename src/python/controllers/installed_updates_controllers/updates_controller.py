import logging
from src.python.view.installed_updates_view.updates_window import UpdateListWindow
from src.python.models.installed_updates_models.updates_service import get_installed_updates_with_powershell
from tkinter import messagebox


class UpdatesController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.updates_data = []

    def retrieve_updates(self):
        logging.info("Attempting to retrieve updates data [controller].")
        try:
            self.updates_data = get_installed_updates_with_powershell()
            self.main_window.enable_button(self.main_window.installed_updates_section[2])
            logging.info("Successfully retrieved updates data [controller].")
            return self.updates_data
        except Exception as e:
            logging.error(f"Failed to retrieve updates data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving updates data: {e}")
            return None

    def show_updates(self):
        if self.updates_data:
            try:
                UpdateListWindow(self.main_window, self.updates_data)
            except Exception as e:
                logging.error(f"Error displaying updates list [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the updates list.")
        else:
            logging.warning("No updates data available to display [controller].")
            messagebox.showinfo("Update List", "No updates data available.")
