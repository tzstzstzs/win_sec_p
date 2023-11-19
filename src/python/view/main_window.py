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

        self.show_user_list_button = ttk.Button(self.frame1, text='Show User List', command=self.controller.show_users, state='disabled')
        self.show_user_list_button.pack(side=tk.RIGHT)

        # Option 2 - Running Processes
        self.frame2 = ttk.Frame(self)
        self.frame2.pack(fill=tk.X, padx=5, pady=5)

        self.option2_var = tk.BooleanVar()
        self.option2_checkbox = ttk.Checkbutton(self.frame2, text='Running Processes', variable=self.option2_var)
        self.option2_checkbox.pack(side=tk.LEFT)

        self.show_option2_button = ttk.Button(self.frame2, text='Show Running Processes', command=self.controller.show_processes, state='disabled')
        self.show_option2_button.pack(side=tk.RIGHT)

        # Option 3 - Placeholder for future functionality
        self.frame3 = ttk.Frame(self)
        self.frame3.pack(fill=tk.X, padx=5, pady=5)

        self.option3_var = tk.BooleanVar()
        self.option3_checkbox = ttk.Checkbutton(self.frame3, text='Option 3', variable=self.option3_var)
        self.option3_checkbox.pack(side=tk.LEFT)

        self.show_option3_button = ttk.Button(self.frame3, text='Show Option 3', command=self.controller.show_option3, state='disabled')
        self.show_option3_button.pack(side=tk.RIGHT)

        # Run Button
        self.run_button = ttk.Button(self, text='Run Selected Features', command=self.run_selected_features)
        self.run_button.pack(expand=True, padx=5, pady=5)

    def run_selected_features(self):
        if self.option1_var.get():
            self.controller.retrieve_users()
        if self.option2_var.get():
            self.controller.retrieve_processes()
        # Add logic for option3_var when implemented

    def enable_user_list_button(self):
        self.show_user_list_button['state'] = 'normal'

    def enable_process_list_button(self):
        self.show_option2_button['state'] = 'normal'
