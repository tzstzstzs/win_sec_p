import logging
from src.python.view.installed_apps_window import InstalledAppsWindow
from src.python.models.installed_apps_service import get_installed_apps
from tkinter import messagebox


class AppController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.apps_data = []

    def retrieve_installed_apps(self):
        logging.info("Attempting to retrieve installed applications.")
        try:
            self.apps_data = get_installed_apps()
            self.main_window.enable_button(self.main_window.installed_apps_section[2])
            logging.info("Successfully retrieved installed applications.")
        except Exception as e:
            logging.error(f"Failed to retrieve installed applications: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while retrieving installed applications: {e}")

    def show_installed_apps(self):
        if self.apps_data:
            try:
                InstalledAppsWindow(self.main_window, self.apps_data)
            except Exception as e:
                logging.error(f"Error displaying installed applications: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying installed applications.")
        else:
            logging.warning("No installed applications data available to display.")
            messagebox.showinfo("Installed Apps", "No installed applications data available.")


# Initialize logging at the start of the application
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
