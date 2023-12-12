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
        self.tree = ttk.Treeview(self)
        self.tree['columns'] = ('Name', 'Version', 'Vendor', 'InstallDate')

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_apps_list()

    def populate_apps_list(self):
        for app in self.apps_data:
            self.tree.insert('', tk.END, values=(
                app['DisplayName'],
                app['DisplayVersion'],
                app['Publisher'],
                app['InstallDate']
            ))