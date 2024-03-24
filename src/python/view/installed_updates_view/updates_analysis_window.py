import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class UpdatesAnalysisWindow(DataWindowBase):
    def __init__(self, parent, missing_updates_data):
        title = 'Missing Updates'
        geometry = '400x600'
        columns = ('HotFixID',)
        super().__init__(parent, missing_updates_data, title, geometry, columns)

    def get_column_width(self, column):
        if column == 'HotFixID':
            return 150
        return 100

    def populate_list(self):
        # Clear existing data in the list
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Populate the treeview with the missing updates data
        for hotfix_id in self.data:
            self.tree.insert('', tk.END, values=(hotfix_id,))
