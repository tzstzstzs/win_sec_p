import tkinter as tk
from tkinter import ttk


def create_installed_apps_section(parent, on_show_installed_apps_callback):
    apps_frame = ttk.Frame(parent)
    apps_frame.pack(fill=tk.X, padx=5, pady=5)

    apps_var = tk.BooleanVar()
    apps_checkbox = ttk.Checkbutton(apps_frame, text='Installed Applications', variable=apps_var)
    apps_checkbox.pack(side=tk.LEFT)

    show_apps_button = ttk.Button(apps_frame, text='Show Installed Apps', command=on_show_installed_apps_callback,
                                  state='disabled')
    show_apps_button.pack(side=tk.RIGHT)

    return apps_frame, apps_var, show_apps_button
