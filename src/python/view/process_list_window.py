import tkinter as tk
from tkinter import ttk


class ProcessListWindow(tk.Toplevel):
    def __init__(self, parent, processes_data):
        super().__init__(parent)
        self.title('Running Processes')
        self.geometry('800x600')
        self.processes_data = processes_data
        self.create_process_list()

    def create_process_list(self):
        self.tree = ttk.Treeview(self)
        self.tree['columns'] = ('Name', 'Id', 'CPU', 'WorkingSet')

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_process_list()

    def populate_process_list(self):
        for proc in self.processes_data:
            self.tree.insert('', tk.END, values=(proc['Name'], proc['Id'], proc['CPU'], proc['WorkingSet']))
