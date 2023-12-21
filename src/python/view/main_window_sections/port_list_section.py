import tkinter as tk
from tkinter import ttk

def create_port_list_section(parent, on_show_open_ports_callback, start_progress, stop_progress, update_progress):
    checkports_frame = ttk.Frame(parent)
    checkports_frame.pack(fill=tk.X, padx=5, pady=5)

    checkports_var = tk.BooleanVar()
    checkports_checkbox = ttk.Checkbutton(checkports_frame, text='Check Ports', variable=checkports_var)
    checkports_checkbox.pack(side=tk.LEFT)

    show_checkports_button = ttk.Button(checkports_frame, text='Show Open Ports', command=on_show_open_ports_callback, state='disabled')
    show_checkports_button.pack(side=tk.RIGHT)

    progress_bar = ttk.Progressbar(parent, orient='horizontal', mode='determinate')
    progress_bar.pack(fill=tk.X, padx=5, pady=5)

    return checkports_frame, checkports_var, show_checkports_button, progress_bar, start_progress, stop_progress, update_progress
