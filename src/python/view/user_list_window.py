import tkinter as tk
from tkinter import ttk


class UserListWindow(tk.Toplevel):
    def __init__(self, parent, users_data):
        super().__init__(parent)
        self.title('User List')
        self.geometry('800x600')
        self.users_data = users_data
        self.create_user_list()

    def create_user_list(self):
        self.tree = ttk.Treeview(self, columns=('Username', 'Description', 'Enabled', 'LastLogon', 'Groups'),
                                 show='headings')

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_user_list()

    def populate_user_list(self):
        for user in self.users_data:
            self.tree.insert('', tk.END, values=(
                user['Username'], user['Description'], user['Enabled'], user['LastLogon'], user['Groups']))
