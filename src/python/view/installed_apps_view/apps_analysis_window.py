import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by  # Assuming the sort_by function is available


class AppsAnalysisWindow(tk.Toplevel):
    def __init__(self, parent, unauthorized_apps_data):
        super().__init__(parent)
        self.title('Unauthorized Applications')
        self.geometry('800x600')
        self.unauthorized_apps_data = unauthorized_apps_data
        self.sort_order = {col: True for col in ('Name', 'Version', 'Vendor', 'InstallDate')}
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=('Name', 'Version', 'Vendor', 'InstallDate'), show='headings')
        for col in ('Name', 'Version', 'Vendor', 'InstallDate'):
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by_column(c))

        for app in self.unauthorized_apps_data:
            self.tree.insert('', tk.END, values=(app['Name'], app['Version'], app['Vendor'], app['InstallDate']))

        self.tree.pack(expand=True, fill=tk.BOTH)

    def sort_by_column(self, col):
        self.unauthorized_apps_data.sort(key=lambda app: app[col], reverse=self.sort_order[col])
        for i in self.tree.get_children():
            self.tree.delete(i)
        for app in self.unauthorized_apps_data:
            self.tree.insert('', tk.END, values=(app['Name'], app['Version'], app['Vendor'], app['InstallDate']))
        self.sort_order[col] = not self.sort_order[col]


if __name__ == "__main__":
    def sample_unauthorized_apps():
        return [
            {'Name': 'App1', 'Version': '1.0', 'Vendor': 'Vendor1', 'InstallDate': '20230101'},
            {'Name': 'App2', 'Version': '2.0', 'Vendor': 'Vendor2', 'InstallDate': '20230202'},
            # Add more sample data as needed
        ]


    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = AppsAnalysisWindow(root, sample_unauthorized_apps())
    app.mainloop()
