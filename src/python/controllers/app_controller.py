from src.python.view.installed_apps_window import InstalledAppsWindow
from src.python.models.installed_apps_service import get_installed_apps
from tkinter import messagebox

class AppController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.apps_data = []

    def retrieve_installed_apps(self):
        print("retrieve_installed_apps initiated")
        try:
            self.apps_data = get_installed_apps()
            self.main_window.enable_installed_apps_button()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to retrieve installed applications: {e}")

    def show_installed_apps(self):
        if self.apps_data:
            InstalledAppsWindow(self.main_window, self.apps_data)
        else:
            messagebox.showinfo("Installed Apps", "Something is wrong with installed apps data")
