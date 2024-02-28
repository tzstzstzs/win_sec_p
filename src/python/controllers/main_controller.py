import logging
from tkinter import messagebox
from src.python.controllers.user_controllers.user_controller import UserController
from src.python.controllers.user_controllers.user_analysis_controller import UserAnalysisController
from src.python.controllers.process_controllers.process_controller import ProcessController
from src.python.controllers.process_controllers.process_analysis_controller import ProcessAnalysisController
from src.python.controllers.open_ports_controllers.open_ports_controller import PortController
from src.python.controllers.open_ports_controllers.open_ports_analysis_controller import PortAnalysisController
from src.python.controllers.installed_apps_controllers.apps_controller import AppController
from src.python.controllers.installed_apps_controllers.apps_analysis_controller import AppsAnalysisController
from src.python.controllers.password_policy_controllers.password_policy_controller import PasswordPolicyController
from src.python.controllers.password_policy_controllers.password_policy_analysis_controller import PasswordPolicyAnalysisController
from src.python.controllers.installed_updates_controllers.installed_updates_controller import UpdatesController
from src.python.controllers.export_controller import ExportController


class MainController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.user_controller = UserController(main_window)
        self.user_analysis_controller = UserAnalysisController(main_window)
        self.process_controller = ProcessController(main_window)
        self.process_analysis_controller = ProcessAnalysisController(main_window)
        self.port_controller = PortController(main_window)
        self.port_analysis_controller = PortAnalysisController(main_window)
        self.app_controller = AppController(main_window)
        self.app_analysis_controller = AppsAnalysisController(main_window)
        self.password_policy_controller = PasswordPolicyController(main_window)
        self.password_policy_analysis_controller = PasswordPolicyAnalysisController(main_window)
        self.updates_controller = UpdatesController(main_window)
        self.export_controller = ExportController(main_window, self)
        self.setup_callbacks()

        self.data_store = {}
        self.all_results = {}

    def setup_callbacks(self):
        self.main_window.set_callbacks(
            self.show_users,
            self.show_processes,
            self.show_open_ports,
            self.show_installed_apps,
            self.show_password_policy,
            self.show_installed_updates,
            self.show_users_result,
            self.show_processes_result,
            self.show_open_ports_result,
            self.show_installed_apps_result,
            self.show_password_policy_result,
            self.show_installed_updates_result,
            self.open_user_analysis_settings,
            self.open_process_analysis_settings,
            self.open_port_analysis_settings,
            self.open_apps_analysis_settings,
            self.open_password_policy_settings,
            self.run_selected_features,
            self.export_data,
            self.export_result
        )

    def run(self):
        try:
            self.main_window.mainloop()
        except Exception as e:
            logging.error(f"Main window loop error: {e}", exc_info=True)
            messagebox.showerror("Error", "An unexpected error occurred in the main window loop.")

    def run_selected_features(self):
        try:
            self.handle_user_list()
            self.handle_processes()
            self.handle_ports()
            self.handle_apps()
            self.handle_password_policy()
            if self.main_window.installed_updates_section[1].get():
                updates = self.updates_controller.retrieve_updates()
                if updates is not None:
                    self.data_store['Installed Updates'] = updates
        except Exception as e:
            logging.error(f"Error running selected features: {e}", exc_info=True)
            messagebox.showerror("Error", "An error occurred while running selected features.")

    def handle_user_list(self):
        """
        Handles the retrieval and storage of user list data.
        """
        if not self.main_window.user_list_section[1].get():
            return
        users = self.user_controller.retrieve_users()
        if users is None:
            return
        self.data_store['User List'] = users
        if self.main_window.user_list_section[3].get():
            self.analyze_user(users)

    def analyze_user(self, users):
        """
        Analyzes the user data.
        Parameters:
            users (list): The list of users to be analyzed.
        """
        user_analysis_result = self.user_analysis_controller.perform_user_analysis(users)
        if user_analysis_result is not None:
            self.all_results['User Analysis Result'] = user_analysis_result

    def handle_processes(self):
        """
        Handles the retrieval and storage of process list data.
        """
        if not self.main_window.running_processes_section[1].get():
            return
        processes = self.process_controller.retrieve_processes()
        if processes is None:
            return
        self.data_store['Running Processes'] = processes
        if self.main_window.running_processes_section[3].get():
            self.analyze_process(processes)

    def analyze_process(self, processes):
        """
        Analyzes the process data.
        Parameters:
            processes (list): The list of processes to be analyzed.
        """
        process_analysis_result = self.process_analysis_controller.perform_process_analysis(processes)
        if process_analysis_result is not None:
            self.all_results['Process Analysis Result'] = process_analysis_result

    def handle_ports(self):
        """
        Handles the retrieval and storage of port list data.
        """
        if not self.main_window.port_list_section[1].get():
            return
        ports = self.port_controller.retrieve_ports()
        if ports is None:
            return
        self.data_store['Open Ports'] = ports
        if self.main_window.port_list_section[3].get():
            self.analyze_ports(ports)

    def analyze_ports(self, ports):
        """
        Analyzes the ports data.
        Parameters:
            processes (list): The list of processes to be analyzed.
            :param ports:
        """
        port_analysis_result = self.port_analysis_controller.perform_port_analysis(ports)
        if port_analysis_result is not None:
            self.all_results['Port Analysis Result'] = port_analysis_result

    def handle_apps(self):
        """
        Handles the retrieval and storage of installed apps data.
        """
        if not self.main_window.installed_apps_section[1].get():
            return
        apps = self.app_controller.retrieve_installed_apps()
        if apps is None:
            return
        self.data_store['Installed Apps'] = apps
        if self.main_window.installed_apps_section[3].get():
            self.analyze_apps(apps)

    def analyze_apps(self, apps):
        """
        Analyzes the installed apps data.
        Parameters:
            apps (list): The list of applications to be analyzed.
            :param apps:
        """
        apps_analysis_result = self.app_analysis_controller.perform_apps_analysis(apps)
        if apps_analysis_result is not None:
            self.all_results['Apps Analysis Result'] = apps_analysis_result

    def handle_password_policy(self):
        if not self.main_window.password_policy_section[1].get():
            return
        password_policy = self.password_policy_controller.retrieve_password_policy()
        if password_policy is None:
            return
        self.data_store['Password Policy'] = password_policy
        if not self.main_window.password_policy_section[3].get():
            return
        self.analyze_password_policy(password_policy)

    def analyze_password_policy(self, password_policy):
        password_policy_result = self.password_policy_analysis_controller.perform_password_policy_analysis(
            password_policy)
        if password_policy_result is not None:
            self.all_results['Password Policy Result'] = password_policy_result

    # Wrapper functions for controllers
    def show_users(self):
        try:
            self.user_controller.show_users()
        except Exception as e:
            self.handle_controller_error(e, "users")

    def open_user_analysis_settings(self):
        try:
            self.user_analysis_controller.open_user_analysis_settings()
        except Exception as e:
            self.handle_controller_error(e, "user analysis settings")

    def show_users_result(self):
        try:
            self.user_analysis_controller.show_user_analysis()
        except Exception as e:
            self.handle_controller_error(e, "user analysis")

    def show_processes(self):
        try:
            self.process_controller.show_processes()
        except Exception as e:
            self.handle_controller_error(e, "processes")

    def open_process_analysis_settings(self):
        try:
            self.process_analysis_controller.open_process_analysis_settings()
        except Exception as e:
            self.handle_controller_error(e, "process analysis settings")

    def show_processes_result(self):
        try:
            self.process_analysis_controller.show_process_analysis()
        except Exception as e:
            self.handle_controller_error(e, "process analysis")

    def show_open_ports(self):
        try:
            self.port_controller.show_ports()
        except Exception as e:
            self.handle_controller_error(e, "open ports")

    def open_port_analysis_settings(self):
        try:
            self.port_analysis_controller.open_ports_settings_window()
        except Exception as e:
            self.handle_controller_error(e, "port analysis settings")

    def show_open_ports_result(self):
        try:
            self.port_analysis_controller.open_analysis_window()
        except Exception as e:
            self.handle_controller_error(e, "port analysis")

    def show_installed_apps(self):
        try:
            self.app_controller.show_installed_apps()
        except Exception as e:
            self.handle_controller_error(e, "installed apps")

    def open_apps_analysis_settings(self):
        try:
            self.app_analysis_controller.open_apps_analysis_settings()
        except Exception as e:
            self.handle_controller_error(e, "apps analysis settings")

    def show_installed_apps_result(self):
        try:
            self.app_analysis_controller.show_apps_analysis()
        except Exception as e:
            self.handle_controller_error(e, "apps analysis")

    def show_password_policy(self):
        try:
            self.password_policy_controller.show_password_policy()
        except Exception as e:
            self.handle_controller_error(e, "password policy")

    def open_password_policy_settings(self):
        try:
            self.password_policy_analysis_controller.open_password_policy_settings()
        except Exception as e:
            self.handle_controller_error(e, "password policy settings")

    def show_password_policy_result(self):
        try:
            self.password_policy_analysis_controller.show_password_policy_analysis()
        except Exception as e:
            self.handle_controller_error(e, "password policy analysis")

    def show_installed_updates(self):
        try:
            self.updates_controller.show_updates()
        except Exception as e:
            self.handle_controller_error(e, "installed updates")

    def show_installed_updates_result(self):
        pass

    def export_data(self):
        self.export_controller.export_data()

    def export_result(self):
        self.export_controller.export_result()

    def handle_controller_error(self, error, feature):
        logging.error(f"Error displaying {feature}: {error}", exc_info=True)
        messagebox.showerror("Error", f"An error occurred while displaying {feature}.")
