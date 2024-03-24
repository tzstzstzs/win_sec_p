import logging
from src.python.view.installed_apps_view.apps_window import InstalledAppsWindow
from src.python.models.installed_apps_models.apps_service import get_installed_apps
from tkinter import messagebox
from src.python.controllers.base_controller import BaseController


class AppsController(BaseController):
    def retrieve_data(self):
        logging.info("Attempting to retrieve installed applications [controller].")
        try:
            self.data = get_installed_apps()
            self.main_window.enable_button(self.main_window.installed_apps_section[2])
            logging.info("Successfully retrieved installed applications [controller].")
            return self.data
        except Exception as e:
            logging.error(f"Failed to retrieve installed applications [controller]: {e}", exc_info=True)
            messagebox.showerror("Error",
                                 f"An error occurred while retrieving installed applications [controller]: {e}")
            return None

    def show_data(self):
        if self.data:
            try:
                InstalledAppsWindow(self.main_window, self.data)
            except Exception as e:
                logging.error(f"Error displaying installed applications [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying installed applications.")
        else:
            logging.warning("No installed applications data available to display [controller].")
            messagebox.showinfo("Installed Apps", "No installed applications data available.")
