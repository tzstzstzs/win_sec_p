import tkinter as tk
from tkinter import ttk


class UpdateListWindow(tk.Toplevel):
    def __init__(self, parent, updates_data):
        super().__init__(parent)
        self.title('Installed Updates List')
        self.geometry('1400x600')
        self.updates_data = updates_data
        self.create_update_list()

    def create_update_list(self):
        self.tree = ttk.Treeview(self, columns=('PropertyDescription', 'HotFixID', 'InstalledOn', 'InstalledBy'),
                                 show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.tree['columns']:
            self.tree.column(col, width=250)  # Adjust width as needed
            self.tree.heading(col, text=col)

        self.populate_update_list()

        # Pack (or grid) the treeview and scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def populate_update_list(self):
        for update in self.updates_data:
            # Ensure that these keys align with how your updates data is structured
            self.tree.insert('', tk.END, values=(
                update.get('HotFixID', 'N/A'), update.get('Description', 'N/A'),
                update.get('InstalledOn', 'N/A'), update.get('InstalledBy', 'N/A')))
