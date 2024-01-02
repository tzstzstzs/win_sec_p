import tkinter as tk
from tkinter import ttk


class InstalledAppsWindow(tk.Toplevel):
    def __init__(self, parent, apps_data):
        super().__init__(parent)
        self.title('Installed Applications')
        self.geometry('800x600')
        self.apps_data = apps_data
        self.create_apps_list()

    def create_apps_list(self):
        self.tree = ttk.Treeview(self, columns=('Name', 'Version', 'Vendor', 'InstallDate'), show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            self.tree.heading(col, text=col)

        self.populate_apps_list()

        # Pack (or grid) the treeview and scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def populate_apps_list(self):
        for app in self.apps_data:
            self.tree.insert('', tk.END, values=(
                app['DisplayName'],
                app['DisplayVersion'],
                app['Publisher'],
                app['InstallDate']
            ))