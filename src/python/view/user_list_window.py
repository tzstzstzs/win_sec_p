import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by  # Import the sort_by function


class UserListWindow(tk.Toplevel):
    def __init__(self, parent, users_data):
        super().__init__(parent)
        self.title('User List')
        self.geometry('800x600')
        self.users_data = users_data
        # Initialize sort order for all columns
        self.sort_order = {col: True for col in ('Username', 'Description', 'Enabled', 'LastLogon', 'Groups')}
        self.create_user_list()

    def create_user_list(self):
        self.tree = ttk.Treeview(self, columns=('Username', 'Description', 'Enabled', 'LastLogon', 'Groups'),
                                 show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            # Attach the sorting function to column headers
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_user_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    def populate_user_list(self):
        for user in self.users_data:
            self.tree.insert('', tk.END, values=(
                user['Username'], user['Description'], user['Enabled'], user['LastLogon'], user['Groups']))
