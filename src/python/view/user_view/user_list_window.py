import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class UserListWindow(DataWindowBase):
    def __init__(self, parent, users_data):
        title = 'Users List'
        geometry = '800x600'
        columns = ('Username', 'Description', 'Enabled', 'LastLogon', 'Groups')
        super().__init__(parent, users_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {'Username': 150, 'Description': 150, 'Enabled': 150, 'LastLogon': 150, 'Groups': 150}
        return column_widths.get(column, 100)

    def populate_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for user in self.data:
            self.tree.insert('', tk.END, values=(
                user.get('Username', 'N/A'),
                user.get('Description', 'N/A'),
                user.get('Enabled', 'N/A'),
                self.format_date(user.get('LastLogon', 'N/A'), '%Y%m%d', '%Y-%m-%d'),
                user.get('Groups', 'N/A')
            ))
