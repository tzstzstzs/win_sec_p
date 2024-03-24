import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class PasswordPolicyAnalysisWindow(DataWindowBase):
    def __init__(self, parent, password_policy_data):
        title = 'Password Policy Analysis Result'
        geometry = '800x600'
        columns = ('Policy', 'Status')
        super().__init__(parent, password_policy_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {
            'Policy': 150,
            'Status': 250,
        }
        return column_widths.get(column, 150)

    def populate_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for policy, status in self.data.items():
            self.tree.insert('', tk.END, values=(policy.replace('_', ' ').capitalize(), status))
