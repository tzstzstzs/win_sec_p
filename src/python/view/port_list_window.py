import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by


class PortListWindow(tk.Toplevel):
    def __init__(self, parent, port_data):
        super().__init__(parent)
        self.title('Open Ports')
        self.geometry('800x600')
        self.port_data = port_data
        self.sort_order = {col: True for col in ('Local Address', 'Local Port', 'Remote Address', 'Remote Port',
                                                 'State')}  # Initialize sort order for all columns
        self.create_port_list()

    def create_port_list(self):
        self.tree = ttk.Treeview(self,
                                 columns=('Local Address', 'Local Port', 'Remote Address', 'Remote Port', 'State'),
                                 show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        # Set up each column in the treeview
        for col in self.tree['columns']:
            self.tree.column(col, width=120)
            # Corrected lambda to use 'c=col' for capturing current column name
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_port_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    def populate_port_list(self):
        # Clear the existing treeview contents
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Add sorted data to the treeview
        for port in self.port_data:
            self.tree.insert('', tk.END, values=(
            port['LocalAddress'], port['LocalPort'], port['RemoteAddress'], port['RemotePort'], port['State']))
