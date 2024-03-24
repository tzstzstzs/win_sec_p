import logging
from src.python.view.installed_updates_view.updates_window import UpdateListWindow
from src.python.models.installed_updates_models.updates_service import get_installed_updates_with_powershell
from tkinter import messagebox
from src.python.controllers.base_controller import BaseController


class UpdatesController(BaseController):
    def retrieve_data(self):
        logging.info("Attempting to retrieve updates data [controller].")
        try:
            self.data = get_installed_updates_with_powershell()
            self.main_window.enable_button(self.main_window.installed_updates_section[2])
            logging.info("Successfully retrieved updates data [controller].")
            return self.data
        except Exception as e:
            logging.error(f"Failed to retrieve updates data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving updates data: {e}")
            return None

    def show_data(self):
        if self.data:
            try:
                UpdateListWindow(self.main_window, self.data)
            except Exception as e:
                logging.error(f"Error displaying updates list [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the updates list.")
        else:
            logging.warning("No updates data available to display [controller].")
            messagebox.showinfo("Update List", "No updates data available.")
