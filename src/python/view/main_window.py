import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from src.python.models.check_user_privileges import is_admin
import platform


class MainWindow(ThemedTk):
    def __init__(self):
        super().__init__(theme="clearlooks")
        self.title('Windows Security Application')
        self.geometry('600x400')

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))

        self.create_widgets()
        self.check_user_status()

        # Callbacks to be set later
        self.on_show_users = None
        self.on_show_processes = None
        self.on_show_open_ports = None
        self.on_show_installed_apps = None
        self.on_run_selected_features = None

    def create_widgets(self):
        # Option 1 - User List
        self.frame1 = ttk.Frame(self)
        self.frame1.pack(fill=tk.X, padx=5, pady=5)

        self.option1_var = tk.BooleanVar()
        self.option1_checkbox = ttk.Checkbutton(self.frame1, text='User List', variable=self.option1_var)
        self.option1_checkbox.pack(side=tk.LEFT)

        self.show_user_list_button = ttk.Button(self.frame1, text='Show User List', command=self.show_users,
                                                state='disabled')
        self.show_user_list_button.pack(side=tk.RIGHT)

        # Option 2 - Running Processes
        self.frame2 = ttk.Frame(self)
        self.frame2.pack(fill=tk.X, padx=5, pady=5)

        self.option2_var = tk.BooleanVar()
        self.option2_checkbox = ttk.Checkbutton(self.frame2, text='Running Processes', variable=self.option2_var)
        self.option2_checkbox.pack(side=tk.LEFT)

        self.show_option2_button = ttk.Button(self.frame2, text='Show Running Processes', command=self.show_processes, state='disabled')
        self.show_option2_button.pack(side=tk.RIGHT)

        # Option 3 - Check open ports
        self.checkports_frame = ttk.Frame(self)
        self.checkports_frame.pack(fill=tk.X, padx=5, pady=5)

        self.checkports_var = tk.BooleanVar()
        self.checkports_checkbox = ttk.Checkbutton(self.checkports_frame, text='Check Ports', variable=self.checkports_var)
        self.checkports_checkbox.pack(side=tk.LEFT)

        self.show_checkports_button = ttk.Button(self.checkports_frame, text='Show Open Ports', command=self.show_open_ports, state='disabled')
        self.show_checkports_button.pack(side=tk.RIGHT)

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=5, pady=5)

        # Option 4 - Installed Applications
        self.apps_frame = ttk.Frame(self)
        self.apps_frame.pack(fill=tk.X, padx=5, pady=5)

        self.apps_var = tk.BooleanVar()
        self.apps_checkbox = ttk.Checkbutton(self.apps_frame, text='Installed Applications', variable=self.apps_var)
        self.apps_checkbox.pack(side=tk.LEFT)

        self.show_apps_button = ttk.Button(self.apps_frame, text='Show Installed Apps', command=self.show_installed_apps, state='disabled')
        self.show_apps_button.pack(side=tk.RIGHT)

        # Run Button
        self.run_button = ttk.Button(self, text='Run Selected Features', command=self.run_selected_features)
        self.run_button.pack(expand=True, padx=5, pady=5)

        # Textbox for user status
        self.user_status_textbox = tk.Text(self, height=2, width=50)
        self.user_status_textbox.pack(pady=10)

        # Label for OS version
        self.os_version_label = ttk.Label(self, text=f"OS Version: {self.get_os_version()}")
        self.os_version_label.pack(pady=10)

    def set_callbacks(self, show_users, show_processes, show_open_ports, show_installed_apps,
                      run_selected_features):
        self.on_show_users = show_users
        self.on_show_processes = show_processes
        self.on_show_open_ports = show_open_ports
        self.on_show_installed_apps = show_installed_apps
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

    def run_selected_features(self):
        if self.on_run_selected_features:
            self.on_run_selected_features()

    def enable_user_list_button(self):
        self.show_user_list_button['state'] = 'normal'

    def enable_process_list_button(self):
        self.show_option2_button['state'] = 'normal'

    def enable_checkports_button(self):
        self.show_checkports_button['state'] = 'normal'

    def enable_installed_apps_button(self):
        self.show_apps_button['state'] = 'normal'

    def start_progress(self, max_value):
        self.progress_bar['maximum'] = max_value
        self.progress_bar['value'] = 0
        # Removed self.progress_bar.start()

    def update_progress(self, value):
        self.progress_bar['value'] = value
        self.update_idletasks()  # This will update the UI to reflect the progress

    def stop_progress(self):
        # Removed self.progress_bar.stop()
        self.progress_bar['value'] = 0
        # Optionally, you can hide the progress bar if the process is done
        # self.progress_bar.pack_forget()

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
