import tkinter as tk
from src.python.view.data_window_base import DataWindowBase


class PortAnalysisWindow(DataWindowBase):
    def __init__(self, parent, vulnerable_ports):
        title = "Possible Vulnerable Ports"
        geometry = '500x400'
        columns = ('Port',)
        super().__init__(parent, vulnerable_ports, title, geometry, columns)

    def get_column_width(self, column):
        return 200

    def populate_list(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Populate the treeview with vulnerable ports data
        for port in self.data:
            self.tree.insert('', tk.END, values=(port,))
