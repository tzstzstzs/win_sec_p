import tkinter as tk
from tkinter import ttk, scrolledtext
from ttkthemes import ThemedTk
from src.python.view.style_config import THEME_NAME, MAIN_WINDOW_TITLE, WINDOW_SIZE, BUTTON_STYLE
import platform
from src.python.view.section_creator import create_section


class MainWindow(ThemedTk):
    def __init__(self, admin_status=False):
        super().__init__(theme=THEME_NAME)
        self.admin_status = admin_status
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
        self.on_show_installed_updates = None

        self.on_show_users_result = None
        self.on_show_processes_result = None
        self.on_show_open_ports_result = None
        self.on_show_installed_apps_result = None
        self.on_show_password_policy_result = None
        self.on_show_installed_updates_result = None

        self.on_open_user_analysis_settings = None
        self.on_open_process_analysis_settings = None
        self.on_open_password_policy_settings = None

        self.on_run_selected_features = None
        self.on_export_data = None
        self.on_export_result = None

    def create_widgets(self):
        style = ttk.Style()
        style.configure('Bold.TCheckbutton', font=('Helvetica', 10, 'bold'))

        # Create a frame to hold both checkboxes
        select_all_frame = ttk.Frame(self)
        select_all_frame.pack(fill='x', padx=5, pady=10)

        # Select All for Analyze Checkboxes
        self.select_all_analyze_var = tk.BooleanVar(value=False)
        self.select_all_analyze_checkbox = ttk.Checkbutton(
            select_all_frame, text="", variable=self.select_all_analyze_var,
            command=lambda: self.toggle_select_all(self.select_all_analyze_var, retrieve=False),
            style='Bold.TCheckbutton')

        # Select All for Analyze Checkboxes
        self.select_all_analyze_var = tk.BooleanVar(value=False)
        self.select_all_analyze_checkbox = ttk.Checkbutton(
            select_all_frame, text="", variable=self.select_all_analyze_var,
            command=lambda: self.toggle_select_all(self.select_all_analyze_var, retrieve=False),
            style='Bold.TCheckbutton')
        self.select_all_analyze_checkbox.pack(side='right', padx=55)

        # Select All for Retrieve Checkboxes
        self.select_all_retrieve_var = tk.BooleanVar(value=False)
        self.select_all_retrieve_checkbox = ttk.Checkbutton(
            select_all_frame, text="", variable=self.select_all_retrieve_var,
            command=lambda: self.toggle_select_all(self.select_all_retrieve_var, retrieve=True),
            style='Bold.TCheckbutton')
        self.select_all_retrieve_checkbox.pack(side='right', padx=153)

        sections = [
            ('User List', self.show_users, self.show_users_result, self.open_user_analysis_settings),
            ('Running Processes', self.show_processes, self.show_processes_result, self.open_process_analysis_settings),
            ('Port List', self.show_open_ports, self.show_open_ports_result, None),
            ('Installed Apps', self.show_installed_apps, self.show_installed_updates_result, None),
            ('Password Policy', self.show_password_policy, self.show_password_policy_result,
             self.open_password_policy_settings),
            ('Installed Updates', self.show_installed_updates, self.show_installed_updates_result, None)
        ]

        for title, data_callback, result_callback, settings_callback in sections:
            section = create_section(self, title, data_callback, result_callback, settings_callback)
            setattr(self, f"{title.lower().replace(' ', '_')}_section", section)

        # Run Button
        self.run_button = ttk.Button(self, text='Run Selected Features', command=self.run_selected_features)
        self.run_button.pack(expand=True, padx=5, pady=5)

        # Export Data Button
        self.export_data_button = ttk.Button(self, text="Export Data", command=self.export_data)
        self.export_data_button.pack(expand=True, padx=5, pady=5)

        # Export Result Button
        self.export_result_button = ttk.Button(self, text="Export Result", command=self.export_result)
        self.export_result_button.pack(expand=True, padx=5, pady=5)

        # Textbox for user status
        self.user_status_textbox = tk.Text(self, height=2, width=50)
        self.user_status_textbox.pack(pady=10)

        # Label for OS version
        self.os_version_label = ttk.Label(self, text=f"OS Version: {self.get_os_version()}")
        self.os_version_label.pack(pady=10)

    def set_callbacks(self, show_users, show_processes, show_open_ports, show_installed_apps, show_password_policy,
                      show_installed_updates, show_users_result, show_processes_result, show_open_ports_result,
                      show_installed_apps_result, show_password_policy_result, show_installed_updates_result,
                      open_user_analysis_settings, open_process_analysis_settings, open_password_policy_settings,
                      run_selected_features, export_data, export_result):
        self.on_show_users = show_users
        self.on_show_processes = show_processes
        self.on_show_open_ports = show_open_ports
        self.on_show_installed_apps = show_installed_apps
        self.on_show_password_policy = show_password_policy
        self.on_show_installed_updates = show_installed_updates
        self.on_show_users_result = show_users_result
        self.on_show_processes_result = show_processes_result
        self.on_show_open_ports_result = show_open_ports_result
        self.on_show_installed_apps_result = show_installed_apps_result
        self.on_show_password_policy_result = show_password_policy_result
        self.on_show_installed_updates_result = show_installed_updates_result
        self.on_open_user_analysis_settings = open_user_analysis_settings
        self.on_open_process_analysis_settings = open_process_analysis_settings
        self.on_open_password_policy_settings = open_password_policy_settings
        self.on_run_selected_features = run_selected_features
        self.on_export_data = export_data
        self.on_export_result = export_result

    def show_users(self):
        if self.on_show_users:
            self.on_show_users()

    def open_user_analysis_settings(self):
        if self.on_open_user_analysis_settings:
            self.on_open_user_analysis_settings()

    def show_users_result(self):
        if self.on_show_users_result:
            self.on_show_users_result()

    def show_processes(self):
        if self.on_show_processes:
            self.on_show_processes()

    def open_process_analysis_settings(self):
        if self.on_open_process_analysis_settings:
            self.on_open_process_analysis_settings()

    def show_processes_result(self):
        if self.on_show_processes_result:
            self.on_show_processes_result()

    def show_open_ports(self):
        if self.on_show_open_ports:
            self.on_show_open_ports()

    def show_open_ports_result(self):
        if self.on_show_open_ports_result:
            self.on_show_open_ports_result()

    def show_installed_apps(self):
        if self.on_show_installed_apps:
            self.on_show_installed_apps()

    def show_installed_apps_result(self):
        if self.on_show_installed_apps_result:
            self.on_show_installed_apps_result()

    def show_password_policy(self):
        if self.on_show_password_policy:
            self.on_show_password_policy()

    def open_password_policy_settings(self):
        if self.on_open_password_policy_settings:
            self.on_open_password_policy_settings()

    def show_password_policy_result(self):
        if self.on_show_password_policy_result:
            self.on_show_password_policy_result()

    def show_installed_updates(self):
        if self.on_show_installed_updates:
            self.on_show_installed_updates()

    def show_installed_updates_result(self):
        if self.on_show_installed_updates_result:
            self.on_show_installed_updates_result()

    def toggle_select_all(self, select_all_var, retrieve):
        is_selected = select_all_var.get()
        for section in ['user_list', 'running_processes', 'port_list', 'installed_apps', 'password_policy',
                        'installed_updates']:
            section_obj = getattr(self, f"{section}_section")
            section_var = section_obj[1] if retrieve else section_obj[
                3]  # retrieve checkbox if retrieve=True else analyze checkbox
            section_var.set(is_selected)

    def run_selected_features(self):
        if self.on_run_selected_features:
            self.on_run_selected_features()

    def export_data(self):
        if self.on_export_data:
            self.on_export_data()

    def export_result(self):
        if self.on_export_result:
            self.on_export_result()

    def enable_button(self, button):
        button['state'] = 'normal'

    def check_user_status(self):
        if self.admin_status:
            self.user_status_textbox.insert(tk.END, "The application is running as Admin.")
            self.user_status_textbox.config(fg='black')
        else:
            self.user_status_textbox.insert(tk.END, "Warning: Not all features may be available. Please run as Admin.")
            self.user_status_textbox.config(fg='red')

    @staticmethod
    def get_os_version():
        return platform.version()
