import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class PortListWindow(DataWindowBase):
    def __init__(self, parent, port_data):
        title = 'Open Ports'
        geometry = '800x600'
        columns = ('Local Address', 'Local Port', 'Remote Address', 'Remote Port', 'State')
        super().__init__(parent, port_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {'Local Address': 120, 'Local Port': 120, 'Remote Address': 120, 'Remote Port': 120, 'State': 120}
        return column_widths.get(column, 150)

    def populate_list(self):
        # Clear the existing treeview contents
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Add sorted data to the treeview
        for port in self.data:
            self.tree.insert('', tk.END, values=(
            port['LocalAddress'], port['LocalPort'], port['RemoteAddress'], port['RemotePort'], port['State']))
