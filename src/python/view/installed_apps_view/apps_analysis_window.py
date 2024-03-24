import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class AppsAnalysisWindow(DataWindowBase):
    def __init__(self, parent, unauthorized_apps_data):
        title = 'Unauthorized Applications'
        geometry = '800x600'
        columns = ('Name', 'Version', 'Vendor', 'InstallDate')
        super().__init__(parent, unauthorized_apps_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {'Name': 200, 'Version': 100, 'Vendor': 200, 'InstallDate': 100}
        return column_widths.get(column, 150)

    def populate_list(self):
        # Clear the existing treeview contents
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Add sorted data to the treeview
        for app in self.data:
            self.tree.insert('', tk.END, values=(
                app['Name'],
                app['Version'],
                app['Vendor'],
                self.format_date(app['InstallDate'], '%Y%m%d', '%Y-%m-%d')
            ))
