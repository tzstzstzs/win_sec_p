import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by  # Import the sort_by function


class PasswordPolicyWindow(tk.Toplevel):
    def __init__(self, parent, policy_data):
        super().__init__(parent)
        self.title('Password Policy')
        self.geometry('800x600')
        self.policy_data = policy_data
        # Initialize sort order for all columns
        self.sort_order = {col: True for col in ('Policy', 'Setting')}
        self.create_policy_list()

    def create_policy_list(self):
        self.tree = ttk.Treeview(self, columns=('Policy', 'Setting'), show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.tree['columns']:
            self.tree.column(col, width=250)
            # Attach the sorting function to column headers
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_policy_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    def populate_policy_list(self):
        for idx, policy in enumerate(self.policy_data, 1):
            self.tree.insert('', tk.END, values=(f"{policy['Line']}. {policy['Key']}", policy['Value']))
