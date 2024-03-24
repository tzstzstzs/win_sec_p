import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from src.python.view.sort_utils import sort_by
import datetime


class DataWindowBase(tk.Toplevel, ABC):
    def __init__(self, parent, data, title, geometry, columns):
        super().__init__(parent)
        self.title(title)
        self.geometry(geometry)
        self.data = data
        self.columns = columns
        self.sort_order = {col: True for col in columns}
        self.create_list()

    def create_list(self):
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        for col in self.columns:
            self.tree.column(col, width=self.get_column_width(col))
            self.tree.heading(col, text=col, command=lambda _col=col: self.on_column_click(_col))

        self.populate_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    @abstractmethod
    def get_column_width(self, column):
        """
        Abstract method to be implemented by subclasses to set the width of each column.
        """
        pass

    def on_column_click(self, col):
        self.sort_order = sort_by(self.tree, col, self.sort_order)

    @abstractmethod
    def populate_list(self):
        """
        Abstract method to be implemented by subclasses to populate the TreeView with data.
        """
        pass

    def format_date(self, date_str, input_format='%Y-%m-%d %H:%M:%S', output_format='%Y-%m-%d %H:%M:%S'):
        """
        Formats a date string from one format to another. If date_str is None or parsing fails,
        appropriate placeholders are returned.
        """
        if date_str is None:
            return 'N/A'
        try:
            date_obj = datetime.datetime.strptime(date_str, input_format)
            return date_obj.strftime(output_format)
        except ValueError:
            return 'Invalid Format'
