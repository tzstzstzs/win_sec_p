import tkinter as tk
from tkinter import ttk


class UpdateListWindow(tk.Toplevel):
    def __init__(self, parent, updates_data):
        super().__init__(parent)
        self.title('Installed Updates List')
        self.geometry('800x600')
        self.updates_data = updates_data
        self.create_update_list()

    def create_update_list(self):
        self.tree = ttk.Treeview(self, columns=('PropertyDescription', 'HotFixID', 'InstalledOn', 'InstalledBy'),
                                 show='headings')

        for col in self.tree['columns']:
            self.tree.column(col, width=250)  # Adjust width as needed
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_update_list()

    def populate_update_list(self):
        for update in self.updates_data:
            # Ensure that these keys align with how your updates data is structured
            self.tree.insert('', tk.END, values=(
                update.get('HotFixID', 'N/A'), update.get('Description', 'N/A'),
                update.get('InstalledOn', 'N/A'), update.get('InstalledBy', 'N/A')))
