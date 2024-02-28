import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class PortAnalysisSettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title('Port Analysis Settings')
        self.geometry('600x400')
        self.save_callback = save_callback
        self.vulnerable_ports = defaults or []
        self.create_widgets()

    def create_widgets(self):
        # Vulnerable Ports
        self.create_listbox_section('Vulnerable Ports:', self.vulnerable_ports, 0, 'vulnerable_ports')

        # Save and Cancel buttons
        ttk.Button(self, text="Save", command=self.save_settings).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self, text="Cancel", command=self.destroy).grid(row=1, column=1, padx=10, pady=10)

    def create_listbox_section(self, label_text, items, row, list_name):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky='w', padx=10, pady=10)
        self.listbox = tk.Listbox(self, height=4)
        self.listbox.grid(row=row, column=1, sticky='ew', padx=10, pady=10)
        for item in items:
            self.listbox.insert(tk.END, item)

        # Additional list management buttons
        ttk.Button(self, text="Add", command=lambda: self.add_item(self.listbox, list_name)).grid(row=row, column=2)
        ttk.Button(self, text="Delete", command=lambda: self.delete_item(self.listbox, list_name)).grid(row=row, column=3)
        ttk.Button(self, text="Edit", command=lambda: self.edit_item(self.listbox, list_name)).grid(row=row, column=4)

    def add_item(self, listbox, list_name):
        item = simpledialog.askstring("Add Item", f"Enter a new item for {list_name}:")
        if item and item.isdigit() and int(item) <= 65535:
            listbox.insert(tk.END, item)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid port number (0-65535).")

    def delete_item(self, listbox, list_name):
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected[0])

    def edit_item(self, listbox, list_name):
        selected = listbox.curselection()
        if selected:
            current_item = listbox.get(selected[0])
            new_item = simpledialog.askstring("Edit Item", f"Edit item:", initialvalue=current_item)
            if new_item and new_item.isdigit() and int(new_item) <= 65535:
                listbox.delete(selected[0])
                listbox.insert(selected[0], new_item)
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid port number (0-65535).")

    def save_settings(self):
        ports = [self.listbox.get(i) for i in range(self.listbox.size())]
        if self.save_callback:
            self.save_callback(ports)
        self.destroy()
