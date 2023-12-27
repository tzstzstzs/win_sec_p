import tkinter as tk
from tkinter import ttk


class PortListWindow(tk.Toplevel):
    def __init__(self, parent, port_data):
        super().__init__(parent)
        self.title('Open Ports')
        self.geometry('800x600')
        self.port_data = port_data
        self.create_port_list()

    def create_port_list(self):
        self.tree = ttk.Treeview(self,
                                 columns=('Local Address', 'Local Port', 'Remote Address', 'Remote Port', 'State'),
                                 show='headings')

        for col in self.tree['columns']:
            self.tree.column(col, width=120)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_port_list()

    def populate_port_list(self):
        for port in self.port_data:
            self.tree.insert('', tk.END, values=(
                port['LocalAddress'], port['LocalPort'], port['RemoteAddress'], port['RemotePort'], port['State']))
