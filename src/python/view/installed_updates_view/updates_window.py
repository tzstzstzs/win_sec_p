import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by  # Import the sort_by function


class UpdateListWindow(tk.Toplevel):
    def __init__(self, parent, updates_data):
        super().__init__(parent)
        self.title('Installed Updates List')
        self.geometry('1400x600')
        self.updates_data = updates_data
        # Initialize sort order for all columns
        self.sort_order = {col: True for col in ('Description', 'HotFixID', 'InstalledOn', 'InstalledBy')}
        self.create_update_list()

    def create_update_list(self):
        print(self.updates_data)
        self.tree = ttk.Treeview(self, columns=('Description', 'HotFixID', 'InstalledOn', 'InstalledBy'),
                                 show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.tree['columns']:
            self.tree.column(col, width=250)
            # Attach the sorting function to column headers
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_update_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    def populate_update_list(self):
        for update in self.updates_data:
            self.tree.insert('', tk.END, values=(
                update.get('Description', 'N/A'), update.get('HotFixID', 'N/A'),
                update.get('InstalledOn', 'N/A'), update.get('InstalledBy', 'N/A')))
