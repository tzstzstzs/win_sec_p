import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Windows Security Application')
        self.geometry('500x300')
        self.create_widgets()

    def create_widgets(self):
        # Option 1 - User List
        self.frame1 = ttk.Frame(self)
        self.frame1.pack(fill=tk.X, padx=5, pady=5)

        self.option1_var = tk.BooleanVar()
        self.option1_checkbox = ttk.Checkbutton(self.frame1, text='User List', variable=self.option1_var)
        self.option1_checkbox.pack(side=tk.LEFT)

        self.show_user_list_button = ttk.Button(self.frame1, text='Show User List', command=self.controller.show_users,
                                                state='disabled')
        self.show_user_list_button.pack(side=tk.RIGHT)

        # Option 2 - Running Processes
        self.frame2 = ttk.Frame(self)
        self.frame2.pack(fill=tk.X, padx=5, pady=5)

        self.option2_var = tk.BooleanVar()
        self.option2_checkbox = ttk.Checkbutton(self.frame2, text='Running Processes', variable=self.option2_var)
        self.option2_checkbox.pack(side=tk.LEFT)

        self.show_option2_button = ttk.Button(self.frame2, text='Show Running Processes',
                                              command=self.controller.show_processes, state='disabled')
        self.show_option2_button.pack(side=tk.RIGHT)

        # Option 3 - Check open ports
        self.checkports_frame = ttk.Frame(self)
        self.checkports_frame.pack(fill=tk.X, padx=5, pady=5)

        self.checkports_var = tk.BooleanVar()
        self.checkports_checkbox = ttk.Checkbutton(self.checkports_frame, text='Check Ports',
                                                   variable=self.checkports_var)
        self.checkports_checkbox.pack(side=tk.LEFT)

        self.show_checkports_button = ttk.Button(self.checkports_frame, text='Show Open Ports',
                                                 command=self.controller.show_open_ports, state='disabled')
        self.show_checkports_button.pack(side=tk.RIGHT)

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=5, pady=5)

        # Run Button
        self.run_button = ttk.Button(self, text='Run Selected Features', command=self.run_selected_features)
        self.run_button.pack(expand=True, padx=5, pady=5)

    def run_selected_features(self):
        if self.option1_var.get():
            self.controller.retrieve_users()
        if self.option2_var.get():
            self.controller.retrieve_processes()
        if self.checkports_var.get():
            self.controller.check_ports()

    def enable_user_list_button(self):
        self.show_user_list_button['state'] = 'normal'

    def enable_process_list_button(self):
        self.show_option2_button['state'] = 'normal'

    def enable_checkports_button(self):
        self.show_checkports_button['state'] = 'normal'

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
