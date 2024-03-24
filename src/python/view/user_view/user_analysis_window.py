import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class UserAnalysisWindow(DataWindowBase):
    def __init__(self, parent, vulnerable_user_accounts):
        title = "Vulnerable User Accounts"
        geometry = '300x400'
        columns = ('Username',)
        super().__init__(parent, vulnerable_user_accounts, title, geometry, columns)

    def get_column_width(self, column):
        return 200

    def populate_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for user in self.data:
            self.tree.insert('', tk.END, values=(user,))
