import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class ProcessSettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title('Process Settings')
        self.geometry('600x400')
        self.save_callback = save_callback
        self.defaults = defaults or {}

        self.cpu_threshold = tk.StringVar(value=self.defaults.get('cpu_threshold', '8000.0'))
        self.memory_threshold = tk.StringVar(value=self.defaults.get('memory_threshold', '1024.0'))
        self.trusted_directories = self.defaults.get('trusted_directories', ['C:\\Windows\\', 'C:\\Program Files\\'])
        self.common_parent_ids = self.defaults.get('common_parent_ids', ['4', '68', '100', '884'])

        self.create_widgets()

    def create_widgets(self):
        # CPU and Memory Thresholds
        self.create_entry('CPU Threshold (MB):', self.cpu_threshold, 0)
        self.create_entry('Memory Threshold (bytes):', self.memory_threshold, 1)

        # Trusted Directories and Common Parent IDs
        self.create_listbox_section('Trusted Directories:', self.trusted_directories, 2, 'trusted_directories')
        self.create_listbox_section('Common Parent IDs:', self.common_parent_ids, 3, 'common_parent_ids')

        ttk.Button(self, text="Save", command=self.save_settings).grid(row=4, column=0, padx=10, pady=10)
        ttk.Button(self, text="Cancel", command=self.destroy).grid(row=4, column=1, padx=10, pady=10)

    def create_entry(self, label_text, string_var, row):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky='w', padx=10, pady=10)
        ttk.Entry(self, textvariable=string_var).grid(row=row, column=1, sticky='ew', padx=10)

    def create_listbox_section(self, label_text, items, row, list_name):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky='w', padx=10, pady=10)
        listbox = tk.Listbox(self, height=4)
        listbox.grid(row=row, column=1, sticky='ew', padx=10, pady=10)
        for item in items:
            listbox.insert(tk.END, item)

        ttk.Button(self, text="Add", command=lambda: self.add_item(listbox, list_name)).grid(row=row, column=2)
        ttk.Button(self, text="Delete", command=lambda: self.delete_item(listbox, list_name)).grid(row=row, column=3)
        ttk.Button(self, text="Edit", command=lambda: self.edit_item(listbox, list_name)).grid(row=row, column=4)

    def add_item(self, listbox, list_name):
        item = tk.simpledialog.askstring("Add Item", f"Enter a new item for {list_name}:")
        if item and item not in getattr(self, list_name):
            getattr(self, list_name).append(item)
            listbox.insert(tk.END, item)

    def delete_item(self, listbox, list_name):
        selected = listbox.curselection()
        if selected:
            getattr(self, list_name).pop(selected[0])
            listbox.delete(selected[0])

    def edit_item(self, listbox, list_name):
        selected = listbox.curselection()
        if selected:
            current_item = getattr(self, list_name)[selected[0]]
            new_item = tk.simpledialog.askstring("Edit Item", f"Edit item:", initialvalue=current_item)
            if new_item:
                getattr(self, list_name)[selected[0]] = new_item
                listbox.delete(selected[0])
                listbox.insert(selected[0], new_item)

    def is_valid_number(self, value):
        """Check if the value is a valid number (integer or float)."""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def all_are_valid_integers(self, values):
        """Check if all values in the list are valid integers."""
        return all(value.isdigit() for value in values)

    def is_valid_directory(self, directory):
        """Check if the directory string is a valid path format."""
        # Basic check for path structure - can be expanded based on requirements
        return os.path.sep in directory

    def save_settings(self):
        if not self.is_valid_number(self.cpu_threshold.get()) or not self.is_valid_number(self.memory_threshold.get()):
            messagebox.showerror("Error", "CPU and Memory Thresholds must be valid numbers.")
            return

        if not self.all_are_valid_integers(self.common_parent_ids):
            messagebox.showerror("Error", "All Common Parent IDs must be valid integers.")
            return

        if not all(self.is_valid_directory(dir_path) for dir_path in self.trusted_directories):
            messagebox.showerror("Error", "All Trusted Directories must have a valid path format.")
            return

        settings = {
            'cpu_threshold': self.cpu_threshold.get(),
            'memory_threshold': self.memory_threshold.get(),
            'trusted_directories': self.trusted_directories,
            'common_parent_ids': self.common_parent_ids
        }
        if self.save_callback:
            self.save_callback(settings)
        self.destroy()
