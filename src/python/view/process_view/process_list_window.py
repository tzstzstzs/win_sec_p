import tkinter as tk
import logging
from src.python.view.data_window_base import DataWindowBase


class ProcessListWindow(DataWindowBase):
    def __init__(self, parent, processes_data):
        title = 'Running Processes'
        geometry = '1400x600'
        columns = ('ProcessName', 'Id', 'CPU', 'WorkingSet', 'Parent', 'ExecutablePath', 'AssociatedUser')
        super().__init__(parent, processes_data, title, geometry, columns)

    def get_column_width(self, column):
        column_widths = {'ProcessName': 150, 'Id': 100, 'CPU': 100, 'WorkingSet': 100, 'Parent': 100,
                         'ExecutablePath': 300, 'AssociatedUser': 150}
        return column_widths.get(column, 100)

    def populate_list(self):
        # Clear existing data in the list
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Populate the treeview with the applications data
        for proc in self.data:
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

