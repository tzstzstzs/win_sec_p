import tkinter as tk
from tkinter import ttk


def create_process_list_section(parent, on_show_processes_callback):
    process_list_frame = ttk.Frame(parent)
    process_list_frame.pack(fill=tk.X, padx=5, pady=5)

    process_list_var = tk.BooleanVar()
    process_list_checkbox = ttk.Checkbutton(process_list_frame, text='Running Processes', variable=process_list_var)
    process_list_checkbox.pack(side=tk.LEFT)

    show_processes_button = ttk.Button(process_list_frame, text='Show Running Processes', command=on_show_processes_callback,
                                       state='disabled')
    show_processes_button.pack(side=tk.RIGHT)

    return process_list_frame, process_list_var, show_processes_button
