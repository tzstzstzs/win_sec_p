import tkinter as tk
from tkinter import ttk, simpledialog


class UpdatesAnalysisSettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title('Updates Analysis Settings')
        self.geometry('1000x600')
        self.save_callback = save_callback
        # Adjusted to expect a list of strings (KB numbers)
        self.authorized_updates = defaults if isinstance(defaults, list) else []

        self.create_widgets()

    def create_widgets(self):
        # Adjusted for handling a list of strings (KB numbers)
        self.create_listbox_section('Authorized KB Numbers:', self.authorized_updates, 0)

        # Save and Cancel buttons
        ttk.Button(self, text="Save", command=self.save_settings).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self, text="Cancel", command=self.destroy).grid(row=1, column=1, padx=10, pady=10)

    def create_listbox_section(self, label_text, items, row):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky='w', padx=10, pady=10)
        self.listbox = tk.Listbox(self, width=80)
        self.listbox.grid(row=row, column=1, sticky='ew', padx=10, pady=10)

        for kb in items:
            self.listbox.insert(tk.END, kb)

        # Adjusted buttons for direct string list manipulation
        ttk.Button(self, text="Edit", command=self.edit_list_item).grid(row=row, column=2, padx=10, pady=10)
        ttk.Button(self, text="Delete", command=self.delete_list_item).grid(row=row, column=3, padx=10, pady=10)
        ttk.Button(self, text="Add", command=self.add_list_item).grid(row=row, column=4, padx=10, pady=10)

    def edit_list_item(self):
        selected = self.listbox.curselection()
        if selected:
            current_kb = self.authorized_updates[selected[0]]
            new_kb = simpledialog.askstring("Edit KB Number", "Edit KB:", initialvalue=current_kb)
            if new_kb:
                self.authorized_updates[selected[0]] = new_kb
                self.listbox.delete(selected[0])
                self.listbox.insert(selected[0], new_kb)

    def delete_list_item(self):
        selected = self.listbox.curselection()
        if selected:
            self.authorized_updates.pop(selected[0])
            self.listbox.delete(selected[0])

    def add_list_item(self):
        new_kb = simpledialog.askstring("Add New KB Number", "Enter new KB:")
        if new_kb:
            self.authorized_updates.append(new_kb)
            self.listbox.insert(tk.END, new_kb)

    def save_settings(self):
        # Directly save the list of strings (KB numbers)
        if self.save_callback:
            self.save_callback(self.authorized_updates)
        self.destroy()
