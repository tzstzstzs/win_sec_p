import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from src.python.view.style_config import THEME_NAME, MAIN_WINDOW_TITLE, WINDOW_SIZE, BUTTON_STYLE
from src.python.models.check_user_privileges import is_admin
import platform
from src.python.view.section_creator import create_section


class MainWindow(ThemedTk):
    def __init__(self):
        super().__init__(theme=THEME_NAME)
        self.title(MAIN_WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)

        style = ttk.Style()
        style.configure('TButton', **BUTTON_STYLE)

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

        sections = [
            ('User List', self.show_users),
            ('Running Processes', self.show_processes),
            ('Port List', self.show_open_ports),
            ('Installed Apps', self.show_installed_apps),
            ('Password Policy', self.show_password_policy)
        ]
        for title, callback in sections:
            setattr(self, f"{title.lower().replace(' ', '_')}_section", create_section(self, title, callback))

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

    def enable_button(self, button):
        button['state'] = 'normal'

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
