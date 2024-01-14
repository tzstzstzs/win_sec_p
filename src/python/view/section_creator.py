import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_section(parent, title, show_data_callback, show_result_callback, icon_path):
    frame = ttk.Frame(parent)
    frame.pack(fill='x', padx=5, pady=5)

    retrieve_var = tk.BooleanVar()
    analyze_var = tk.BooleanVar()

    ttk.Label(frame, text=title).pack(side='left', padx=5)

    img = Image.open(icon_path)
    img = img.resize((20, 20), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    display_result_button = ttk.Button(frame, image=img, command=show_result_callback, state='disabled')
    display_result_button.image = img  # keep a reference!
    display_result_button.pack(side='right', padx=(5, 5))

    analyze_checkbox = ttk.Checkbutton(frame, variable=analyze_var, state='disabled')
    analyze_checkbox.pack(side='right', padx=(0, 0))
    ttk.Label(frame, text="Analyze:").pack(side='right', padx=(5, 0))

    img = Image.open(icon_path)
    img = img.resize((20, 20), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    display_data_button = ttk.Button(frame, image=img, command=show_data_callback, state='disabled')
    display_data_button.image = img  # keep a reference!
    display_data_button.pack(side='right', padx=(5, 100))

    retrieve_checkbox = ttk.Checkbutton(frame, variable=retrieve_var)
    retrieve_checkbox.pack(side='right', padx=(0, 5))
    ttk.Label(frame, text="Retrieve:").pack(side='right', padx=(5, 0))

    retrieve_var.trace('w', lambda *args: toggle_analyze_checkbox(retrieve_var, analyze_var, analyze_checkbox))

    return frame, retrieve_var, display_data_button, analyze_var, display_result_button


def toggle_analyze_checkbox(retrieve_var, analyze_var, analyze_checkbox):
    """
    Enable or disable the analysis checkbox based on the retrieve checkbox's state.
    """
    if retrieve_var.get():
        analyze_checkbox['state'] = 'normal'
    else:
        analyze_checkbox['state'] = 'disabled'
        analyze_var.set(False)
