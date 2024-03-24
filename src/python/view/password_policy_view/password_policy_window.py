import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class PasswordPolicyWindow(DataWindowBase):
    def __init__(self, parent, policy_data):
        title = 'Password Policy'
        geometry = '800x600'
        columns = ('Index', 'Policy', 'Value')
        super().__init__(parent, policy_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {'Index': 20, 'Policy': 200, 'Value': 100}
        return column_widths.get(column, 250)

    def populate_list(self):
        # Clear the existing treeview contents
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Add sorted data to the treeview
        for policy in self.data:
            self.tree.insert('', tk.END, values=(policy['Index'], policy['Policy'], policy['Value']))
