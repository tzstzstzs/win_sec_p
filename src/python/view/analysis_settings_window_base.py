import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from abc import ABC, abstractmethod


class AnalysisSettingsWindowBase(tk.Toplevel, ABC):
    def __init__(self, parent, save_callback=None, defaults=None, title='Settings Window', geometry='1000x600'):
        super().__init__(parent)
        self.title(title)
        self.geometry(geometry)
        self.save_callback = save_callback
        self.defaults = defaults if defaults is not None else []
        self.create_widgets()

    @abstractmethod
    def create_widgets(self):
        """
        This method should be implemented by subclasses to create specific widgets
        for the settings window, such as listboxes and buttons.
        """
        pass

    def create_listbox_section(self, label_text, items, row, list_name):
        """
        Creates a section with a label and a listbox. This method can be called
        by subclasses in their create_widgets() implementation.
        """
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky='w', padx=10, pady=10)
        listbox = tk.Listbox(self, width=80)
        listbox.grid(row=row, column=1, sticky='ew', padx=10, pady=10)

        for item in items:
            listbox.insert(tk.END, item)

        ttk.Button(self, text="Add", command=lambda lb=listbox, ln=list_name: self.add_list_item(lb, ln)).grid(row=row,
                                                                                                               column=4,
                                                                                                               padx=10,
                                                                                                               pady=10)
        ttk.Button(self, text="Edit", command=lambda lb=listbox, ln=list_name: self.edit_list_item(lb, ln)).grid(
            row=row, column=2, padx=10, pady=10)
        ttk.Button(self, text="Delete", command=lambda lb=listbox, ln=list_name: self.delete_list_item(lb, ln)).grid(
            row=row, column=3, padx=10, pady=10)

        setattr(self, list_name, listbox)

    @abstractmethod
    def edit_list_item(self, listbox, list_name):
        """
        Subclasses should implement this method to edit an item in the listbox.
        """
        pass

    @abstractmethod
    def delete_list_item(self, listbox, list_name):
        """
        Subclasses should implement this method to delete an item from the listbox.
        """
        pass

    @abstractmethod
    def add_list_item(self, listbox, list_name):
        """
        Subclasses should implement this method to add a new item to the listbox.
        """
        pass

    def save_settings(self):
        """
        Subclasses should implement this method to save the settings when the
        Save button is clicked.
        """
        if self.save_callback:
            self.save_callback(self.get_settings())
        self.destroy()

    @abstractmethod
    def get_settings(self):
        """
        Subclasses should implement this method to return the settings to be saved.
        """
        pass
