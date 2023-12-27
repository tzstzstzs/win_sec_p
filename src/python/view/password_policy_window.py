import tkinter as tk
from tkinter import ttk


class PasswordPolicyWindow(tk.Toplevel):
    def __init__(self, parent, policy_data):
        super().__init__(parent)
        self.title('Password Policy')
        self.geometry('800x600')
        self.policy_data = policy_data
        self.create_policy_list()

    def create_policy_list(self):
        self.tree = ttk.Treeview(self, columns=('Policy', 'Setting'), show='headings')

        for col in self.tree['columns']:
            self.tree.column(col, width=250)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_policy_list()

    def populate_policy_list(self):
        for idx, policy in enumerate(self.policy_data, 1):
            self.tree.insert('', tk.END, values=(f"{policy['Line']}. {policy['Key']}", policy['Value']))

