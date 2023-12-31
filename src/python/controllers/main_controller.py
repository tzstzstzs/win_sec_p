import logging
from tkinter import messagebox
from src.python.controllers.port_controller import PortController
from src.python.controllers.process_controller import ProcessController
from src.python.controllers.user_controller import UserController
from src.python.controllers.app_controller import AppController
from src.python.controllers.password_policy_controller import PasswordPolicyController
from src.python.controllers.updates_controller import UpdatesController
from src.python.controllers.export_controller import ExportController


class MainController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.user_controller = UserController(main_window)
        self.process_controller = ProcessController(main_window)
        self.port_controller = PortController(main_window)
        self.app_controller = AppController(main_window)
        self.password_policy_controller = PasswordPolicyController(main_window)
        self.updates_controller = UpdatesController(main_window)
        self.export_controller = ExportController(main_window, self)
        self.setup_callbacks()

        self.data_store = {}

    def setup_callbacks(self):
        self.main_window.set_callbacks(
            self.show_users,
            self.show_processes,
            self.show_open_ports,
            self.show_installed_apps,
            self.show_password_policy,
            self.show_installed_updates,
            self.run_selected_features,
            self.handle_export
        )

    def run(self):
        try:
            self.main_window.mainloop()
        except Exception as e:
            logging.error(f"Main window loop error: {e}", exc_info=True)
            messagebox.showerror("Error", "An unexpected error occurred in the main window loop.")

    def run_selected_features(self):
        try:
            if self.main_window.user_list_section[1].get():
                users = self.user_controller.retrieve_users()
                if users is not None:
                    self.data_store['User List'] = users
                print("Stored User List: ", self.data_store['User List'])
            if self.main_window.running_processes_section[1].get():
                processes = self.process_controller.retrieve_processes()
                if processes is not None:
                    self.data_store['Running Processes'] = processes
            if self.main_window.port_list_section[1].get():
                ports = self.port_controller.retrieve_ports()
                if ports is not None:
                    self.data_store['Open Ports'] = ports
            if self.main_window.installed_apps_section[1].get():
                apps = self.app_controller.retrieve_installed_apps()
                if apps is not None:
                    self.data_store['Installed Apps'] = apps
            if self.main_window.password_policy_section[1].get():
                password_policy = self.password_policy_controller.retrieve_password_policy()
                if password_policy is not None:
                    self.data_store['Password Policy'] = password_policy
            if self.main_window.installed_updates_section[1].get():
                updates = self.updates_controller.retrieve_updates()
                if updates is not None:
                    self.data_store['Password Policy'] = updates
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
            self.port_controller.show_ports()
        except Exception as e:
            self.handle_controller_error(e, "open ports")

    def show_installed_apps(self):
        try:
            self.app_controller.show_installed_apps()
        except Exception as e:
            self.handle_controller_error(e, "installed apps")

    def show_password_policy(self):
        try:
            self.password_policy_controller.show_password_policy()
        except Exception as e:
            self.handle_controller_error(e, "password policy")

    def show_installed_updates(self):
        try:
            self.updates_controller.show_updates()
        except Exception as e:
            self.handle_controller_error(e, "installed updates")

    def handle_export(self):
        self.export_controller.export_data()
        print(self.data_store)

    def handle_controller_error(self, error, feature):
        logging.error(f"Error displaying {feature}: {error}", exc_info=True)
        messagebox.showerror("Error", f"An error occurred while displaying {feature}.")
