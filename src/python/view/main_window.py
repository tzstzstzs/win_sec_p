import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from src.python.models.check_user_privileges import is_admin
import platform
from src.python.view.main_window_sections.user_list_section import create_user_list_section
from src.python.view.main_window_sections.process_list_section import create_process_list_section
from src.python.view.main_window_sections.port_list_section import create_port_list_section
from src.python.view.main_window_sections.installed_apps_section import create_installed_apps_section
from src.python.view.main_window_sections.password_policy_section import create_password_policy_section


class MainWindow(ThemedTk):
    def __init__(self):
        super().__init__(theme="clearlooks")
        self.title('Windows Security Application')
        self.geometry('600x500')

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))

        self.create_widgets()
        self.check_user_status()

        # Callbacks to be set later
        self.on_show_users = None
        self.on_show_processes = None
        self.on_show_open_ports = None
        self.on_show_installed_apps = None
        self.on_show_password_policy = None
        self.on_run_selected_features = None

    def create_widgets(self):
        # Option 1 - User List
        self.user_list_frame, self.user_list_var, self.show_user_list_button = create_user_list_section(self, self.show_users)

        # Option 2 - Running Processes
        self.process_list_frame, self.process_list_var, self.show_processes_button = create_process_list_section(self, self.show_processes)

        # Option 3 - Check Open Ports and Progress Bar
        self.checkports_frame, self.checkports_var, self.show_checkports_button = create_port_list_section(self, self.show_open_ports)

        # Option 4 - Installed Applications
        self.apps_frame, self.apps_var, self.show_apps_button = create_installed_apps_section(self, self.show_installed_apps)

        # Option 5 - Check Password Policy
        self.policy_frame, self.policy_var, self.show_policy_button = create_password_policy_section(self,self.show_password_policy)

        # Run Button
        self.run_button = ttk.Button(self, text='Run Selected Features', command=self.run_selected_features)
        self.run_button.pack(expand=True, padx=5, pady=5)

        # Textbox for user status
        self.user_status_textbox = tk.Text(self, height=2, width=50)
        self.user_status_textbox.pack(pady=10)

        # Label for OS version
        self.os_version_label = ttk.Label(self, text=f"OS Version: {self.get_os_version()}")
        self.os_version_label.pack(pady=10)

    def set_callbacks(self, show_users, show_processes, show_open_ports, show_installed_apps, show_password_policy,
                      run_selected_features):
        self.on_show_users = show_users
        self.on_show_processes = show_processes
        self.on_show_open_ports = show_open_ports
        self.on_show_installed_apps = show_installed_apps
        self.on_show_password_policy = show_password_policy
        self.on_run_selected_features = run_selected_features

    def show_users(self):
        if self.on_show_users:
            self.on_show_users()

    def show_processes(self):
        if self.on_show_processes:
            self.on_show_processes()

    def show_open_ports(self):
        if self.on_show_open_ports:
            self.on_show_open_ports()

    def show_installed_apps(self):
        if self.on_show_installed_apps:
            self.on_show_installed_apps()

    def show_password_policy(self):
        if self.on_show_password_policy:
            self.on_show_password_policy()

    def run_selected_features(self):
        if self.on_run_selected_features:
            self.on_run_selected_features()

    def enable_user_list_button(self):
        self.show_user_list_button['state'] = 'normal'

    def enable_process_list_button(self):
        self.show_processes_button['state'] = 'normal'

    def enable_checkports_button(self):
        self.show_checkports_button['state'] = 'normal'

    def enable_password_policy_button(self):
        self.show_policy_button['state'] = 'normal'

    def enable_installed_apps_button(self):
        self.show_apps_button['state'] = 'normal'

    def check_user_status(self):
        if is_admin():
            self.user_status_textbox.insert(tk.END, "The application is running as Admin.")
            self.user_status_textbox.config(fg='black')
        else:
            self.user_status_textbox.insert(tk.END, "Warning: Not all features may be available. Please run as Admin.")
            self.user_status_textbox.config(fg='red')

    @staticmethod
    def get_os_version():
        return platform.version()
