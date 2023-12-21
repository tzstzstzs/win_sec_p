import tkinter as tk
from tkinter import ttk


def create_user_list_section(parent, on_show_users_callback):
    user_list_frame = ttk.Frame(parent)
    user_list_frame.pack(fill=tk.X, padx=5, pady=5)

    user_list_var = tk.BooleanVar()
    user_list_checkbox = ttk.Checkbutton(user_list_frame, text='User List', variable=user_list_var)
    user_list_checkbox.pack(side=tk.LEFT)

    show_user_list_button = ttk.Button(user_list_frame, text='Show User List', command=on_show_users_callback, state='disabled')
    show_user_list_button.pack(side=tk.RIGHT)

    return user_list_frame, user_list_var, show_user_list_button
