import logging
from tkinter import messagebox
from src.python.controllers.port_controller import PortController
from src.python.controllers.process_controller import ProcessController
from src.python.controllers.user_controller import UserController
from src.python.controllers.app_controller import AppController


class MainController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.user_controller = UserController(main_window)
        self.process_controller = ProcessController(main_window)
        self.port_controller = PortController(main_window)
        self.app_controller = AppController(main_window)
        self.setup_callbacks()

    def setup_callbacks(self):
        self.main_window.set_callbacks(
            self.show_users,
            self.show_processes,
            self.show_open_ports,
            self.show_installed_apps,
            self.run_selected_features
        )

    def run(self):
        try:
            self.main_window.mainloop()
        except Exception as e:
            logging.error(f"Main window loop error: {e}", exc_info=True)
            messagebox.showerror("Error", "An unexpected error occurred in the main window loop.")

    def run_selected_features(self):
        try:
            if self.main_window.option1_var.get():
                self.user_controller.retrieve_users()
            if self.main_window.option2_var.get():
                self.process_controller.retrieve_processes()
            if self.main_window.checkports_var.get():
                self.port_controller.check_ports()
            if self.main_window.apps_var.get():
                self.app_controller.retrieve_installed_apps()
        except Exception as e:
            logging.error(f"Error running selected features: {e}", exc_info=True)
            messagebox.showerror("Error", "An error occurred while running selected features.")

    # Wrapper functions for controllers
    def show_users(self):
        try:
            self.user_controller.show_users()
        except Exception as e:
            self.handle_controller_error(e, "users")

    def show_processes(self):
        try:
            self.process_controller.show_processes()
        except Exception as e:
            self.handle_controller_error(e, "processes")

    def show_open_ports(self):
        try:
            self.port_controller.show_open_ports()
        except Exception as e:
            self.handle_controller_error(e, "open ports")

    def show_installed_apps(self):
        try:
            self.app_controller.show_installed_apps()
        except Exception as e:
            self.handle_controller_error(e, "installed apps")

    def handle_controller_error(self, error, feature):
        logging.error(f"Error displaying {feature}: {error}", exc_info=True)
        messagebox.showerror("Error", f"An error occurred while displaying {feature}.")
