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

        # Set the show methods from the respective controllers
        self.show_users = self.user_controller.show_users
        self.show_processes = self.process_controller.show_processes
        self.show_open_ports = self.port_controller.show_open_ports
        self.show_installed_apps = self.app_controller.show_installed_apps

        # Set the callbacks for MainWindow
        self.main_window.set_callbacks(
            self.show_users,
            self.show_processes,
            self.show_open_ports,
            self.show_installed_apps,
            self.run_selected_features
        )

    def run(self):
        self.main_window.mainloop()

    def run_selected_features(self):
        if self.main_window.option1_var.get():
            self.user_controller.retrieve_users()
        if self.main_window.option2_var.get():
            self.process_controller.retrieve_processes()
        if self.main_window.checkports_var.get():
            self.port_controller.check_ports()
        if self.main_window.apps_var.get():  # Assuming you have added a variable for the installed apps
            self.app_controller.retrieve_installed_apps()
