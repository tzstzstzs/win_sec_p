import tkinter as tk
from tkinter import ttk


def create_section(parent, section_title, on_show_callback):
    frame = ttk.Frame(parent)
    frame.pack(fill=tk.X, padx=5, pady=5)

    var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(frame, text=section_title, variable=var)
    checkbox.pack(side=tk.LEFT)

    show_button = ttk.Button(frame, text=f'Show {section_title}', command=on_show_callback, state='disabled')
    show_button.pack(side=tk.RIGHT)

    return frame, var, show_button
