import tkinter as tk
from tkinter import ttk

def create_port_list_section(parent, on_show_ports_callback):
    port_list_frame = ttk.Frame(parent)
    port_list_frame.pack(fill=tk.X, padx=5, pady=5)

    port_list_var = tk.BooleanVar()
    port_list_checkbox = ttk.Checkbutton(port_list_frame, text='Open Ports', variable=port_list_var)
    port_list_checkbox.pack(side=tk.LEFT)

    show_port_list_button = ttk.Button(port_list_frame, text='Show Open Ports', command=on_show_ports_callback, state='disabled')
    show_port_list_button.pack(side=tk.RIGHT)

    return port_list_frame, port_list_var, show_port_list_button
