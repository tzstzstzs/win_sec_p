import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class UpdateListWindow(DataWindowBase):
    def __init__(self, parent, updates_data):
        title = 'Installed Updates'
        geometry = '1400x600'
        columns = ('Description', 'HotFixID', 'InstalledOn', 'InstalledBy')
        super().__init__(parent, updates_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {'Description': 250, 'HotFixID': 250, 'InstalledOn': 250, 'InstalledBy': 250}
        return column_widths.get(column, 250)

    def populate_list(self):
        # Clear the existing treeview contents
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Add sorted data to the treeview
        for update in self.data:
            self.tree.insert('', tk.END, values=(
                update.get('Description', 'N/A'), update.get('HotFixID', 'N/A'),
                update.get('InstalledOn', 'N/A'), update.get('InstalledBy', 'N/A')))
