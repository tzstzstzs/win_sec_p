import tkinter as tk
from tkinter import ttk


class UserAnalysisWindow(tk.Toplevel):
    def __init__(self, parent, vulnerable_user_accounts):
        super().__init__(parent)
        self.title("Vulnerable User Accounts Analysis")
        self.geometry('300x400')
        self.parent = parent
        self.vulnerable_user_accounts = vulnerable_user_accounts

        # Create a frame for the label, list and scrollbar
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a label to display the specified text
        label = ttk.Label(frame, text="The following accounts should be disabled:")
        label.pack(side=tk.TOP, fill=tk.X)

        # Create a frame for the listbox and scrollbar
        list_frame = ttk.Frame(frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox to display vulnerable accounts
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure scrollbar
        scrollbar.config(command=self.listbox.yview)

        # Populate the listbox
        for account in vulnerable_user_accounts:
            self.listbox.insert(tk.END, account)
