import tkinter as tk
from tkinter import ttk

def create_password_policy_section(parent, on_show_password_policy_callback):
    policy_frame = ttk.Frame(parent)
    policy_frame.pack(fill=tk.X, padx=5, pady=5)

    policy_var = tk.BooleanVar()
    policy_checkbox = ttk.Checkbutton(policy_frame, text='Password Policy', variable=policy_var)
    policy_checkbox.pack(side=tk.LEFT)

    show_policy_button = ttk.Button(policy_frame, text='Show Password Policy', command=on_show_password_policy_callback, state='disabled')
    show_policy_button.pack(side=tk.RIGHT)

    return policy_frame, policy_var, show_policy_button
