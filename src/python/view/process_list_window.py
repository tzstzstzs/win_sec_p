import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by

class ProcessListWindow(tk.Toplevel):
    def __init__(self, parent, processes_data):
        super().__init__(parent)
        self.title('Running Processes')
        self.geometry('1200x600')
        self.processes_data = processes_data
        # Initialize sort order for all columns
        self.sort_order = {col: True for col in ('Name', 'Id', 'CPU', 'WorkingSet', 'Parent')}
        self.create_process_list()

    def create_process_list(self):
        self.tree = ttk.Treeview(self, columns=('Name', 'Id', 'CPU', 'WorkingSet', 'Parent'), show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.tree['columns']:
            self.tree.column(col, width=200)
            # Attach the sorting function to column headers
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_process_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    def populate_process_list(self):
        # Create a dictionary to store parent processes
        parent_nodes = {}

        for proc in self.processes_data:
            parent_id = proc['Parent']
            proc_id = proc['Id']

            # If the process has a parent, and the parent is not already in the tree, add it
            if parent_id and parent_id not in parent_nodes:
                parent_info = next((p for p in self.processes_data if p['Id'] == parent_id), None)
                if parent_info:
                    parent_node = self.tree.insert('', tk.END, text=parent_info['Name'],
                                                   values=(parent_info['Name'], parent_info['Id'],
                                                           parent_info['CPU'], parent_info['WorkingSet'],
                                                           'N/A'))  # Parent of the parent is 'N/A'
                    parent_nodes[parent_id] = parent_node

            # Insert the process either as a child of its parent or as a top-level item
            if parent_id and parent_id in parent_nodes:
                self.tree.insert(parent_nodes[parent_id], tk.END, text=proc['Name'],
                                 values=(proc['Name'], proc['Id'], proc['CPU'],
                                         proc['WorkingSet'], parent_id))
            else:
                self.tree.insert('', tk.END, text=proc['Name'],
                                 values=(proc['Name'], proc['Id'], proc['CPU'],
                                         proc['WorkingSet'],
                                         parent_id or 'N/A'))  # 'N/A' for processes without a parent
