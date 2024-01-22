import tkinter as tk
from tkinter import ttk
from src.python.view.sort_utils import sort_by
import logging


class ProcessListWindow(tk.Toplevel):
    def __init__(self, parent, processes_data):
        super().__init__(parent)
        self.title('Running Processes')
        self.geometry('1400x600')  # Adjusted for additional columns
        self.processes_data = processes_data
        self.sort_order = {col: True for col in ('ProcessName', 'Id', 'CPU', 'WorkingSet', 'Parent', 'ExecutablePath', 'AssociatedUser')}
        self.create_process_list()

        # Bind the treeview click event
        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

    def create_process_list(self):
        columns = ('ProcessName', 'Id', 'CPU', 'WorkingSet', 'Parent', 'ExecutablePath', 'AssociatedUser')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in columns:
            self.tree.column(col, width=200 if col in ['ExecutablePath', 'AssociatedUser'] else 100)
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_process_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    def on_tree_click(self, event):
        # Get the item clicked
        item_id = self.tree.identify_row(event.y)
        if item_id:
            # Get the item's values
            item_values = self.tree.item(item_id, 'values')
            # Format the values as a string
            text_to_copy = ', '.join(map(str, item_values))
            # Copy the text to clipboard
            self.clipboard_clear()
            self.clipboard_append(text_to_copy)
            logging.info(f"Copied to clipboard: {text_to_copy}")

    def populate_process_list(self):
        parent_nodes = {}

        for proc in self.processes_data:
            try:
                parent_id = proc.get('ParentId', None)
                proc_id = proc.get('Id', None)

                working_set_mb = 0
                if proc.get('WorkingSet') is not None:
                    working_set_mb = proc['WorkingSet'] / (1024 * 1024)

                self.tree.insert('', tk.END, text=proc.get('ProcessName', ''),
                                 values=(proc.get('ProcessName', ''), proc_id, proc.get('CPU', ''),
                                         f"{working_set_mb:.2f} MB",
                                         parent_id or 'N/A',
                                         proc.get('ExecutablePath', 'N/A'),
                                         proc.get('AssociatedUser', 'N/A')))
            except Exception as e:
                logging.error(f"Error processing process data: {e}", exc_info=True)

