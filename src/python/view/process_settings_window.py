import tkinter as tk
from tkinter import ttk, messagebox


class ProcessSettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title('Process Settings')
        self.geometry('600x400')
        self.defaults = defaults
        # Ensure defaults is a dictionary
        if defaults is None:
            defaults = {}

        # Convert numeric values to StringVar
        self.cpu_threshold = tk.StringVar(value=str(defaults.get('cpu_threshold', '8000.0')))
        self.memory_threshold = tk.StringVar(value=str(defaults.get('memory_threshold', '1024.0')))

        self.trusted_directories = defaults.get('trusted_directories', ['C:\\Windows\\', 'C:\\Program Files\\'])
        self.common_parent_ids = defaults.get('common_parent_ids', ['0', '4'])

        self.save_callback = save_callback

        self.lst_trusted_directories = tk.Listbox(self)
        self.lst_common_parent_ids = tk.Listbox(self)

        self.create_widgets()

    def create_widgets(self):
        # CPU Threshold
        ttk.Label(self, text='CPU Threshold (MB)').grid(row=0, column=0, sticky='w', padx=10, pady=10)
        ttk.Entry(self, textvariable=self.cpu_threshold).grid(row=0, column=1, sticky='ew', padx=10)

        # Memory Threshold
        ttk.Label(self, text='Memory Threshold (bytes)').grid(row=1, column=0, sticky='w', padx=10, pady=10)
        ttk.Entry(self, textvariable=self.memory_threshold).grid(row=1, column=1, sticky='ew', padx=10)

        # Trusted Directories
        ttk.Label(self, text='Trusted Directories').grid(row=2, column=0, sticky='w', padx=10, pady=10)
        # Assuming a method to manage (add, delete, edit) the trusted directories
        self.create_list_management_section(2, self.defaults.get('trusted_directories'))
        self.populate_listbox(self.lst_trusted_directories, self.defaults.get('trusted_directories', []))

        # Common Parent IDs
        ttk.Label(self, text='Common Parent IDs').grid(row=3, column=0, sticky='w', padx=10, pady=10)
        # Assuming a method to manage (add, delete, edit) the common parent IDs
        self.create_list_management_section(3, self.defaults.get('common_parent_ids'))
        self.populate_listbox(self.lst_common_parent_ids, self.defaults.get('common_parent_ids', []))

        # Save and Cancel buttons
        self.btn_save = tk.Button(self, text="Save and exit", command=self.save_settings)
        self.btn_save.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cancel = tk.Button(self, text="Cancel", command=self.destroy)
        self.btn_cancel.grid(row=5, column=1, padx=10, pady=10)

        # Initialize instance variables to track the current state of the lists
        self.current_trusted_directories = self.trusted_directories[:]
        self.current_common_parent_ids = self.common_parent_ids[:]

    def create_list_management_section(self, row, list_items):
        frame = ttk.Frame(self)
        frame.grid(row=row, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

          # Listbox to display items
        listbox = tk.Listbox(frame, height=6)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.populate_listbox(listbox, list_items)

        # Frame for buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Entry for adding/editing items
        entry = ttk.Entry(frame)
        entry.pack(side=tk.BOTTOM, fill=tk.X)

        # Add button
        add_btn = ttk.Button(btn_frame, text="Add", command=lambda: self.add_item(listbox, entry, list_items))
        add_btn.pack(fill=tk.X)

        # Delete button
        del_btn = ttk.Button(btn_frame, text="Delete", command=lambda: self.delete_item(listbox, list_items))
        del_btn.pack(fill=tk.X)

        # Edit button
        edit_btn = ttk.Button(btn_frame, text="Edit", command=lambda: self.edit_item(listbox, entry, list_items))
        edit_btn.pack(fill=tk.X)

    def populate_listbox(self, listbox, items):
        listbox.delete(0, tk.END)
        for item in items:
            listbox.insert(tk.END, item)

    # def add_item(self, listbox, entry, items):
    #     new_item = entry.get()
    #     if new_item and new_item not in items:
    #         items.append(new_item)
    #         self.populate_listbox(listbox, items)
    #         entry.delete(0, tk.END)

    def add_item(self, listbox, entry, current_items):
        new_item = entry.get()
        if new_item and new_item not in current_items:
            current_items.append(new_item)
            self.populate_listbox(listbox, current_items)
            entry.delete(0, tk.END)

    def delete_item(self, listbox, current_items):
        selected = listbox.curselection()
        if selected:
            current_items.pop(selected[0])
            self.populate_listbox(listbox, current_items)

    def edit_item(self, listbox, entry, current_items):
        selected = listbox.curselection()
        if selected:
            current_item = listbox.get(selected[0])
            new_item = entry.get()
            if new_item:
                current_items[current_items.index(current_item)] = new_item
                self.populate_listbox(listbox, current_items)
                entry.delete(0, tk.END)

    def save_settings(self):
        # Extract threshold values using StringVar's get() method
        cpu_threshold = self.cpu_threshold.get()
        memory_threshold = self.memory_threshold.get()

        # Use the current state of the lists for saving
        settings = {
            'cpu_threshold': cpu_threshold,
            'memory_threshold': memory_threshold,
            'trusted_directories': self.current_trusted_directories,
            'common_parent_ids': self.current_common_parent_ids
        }

        print(self.current_trusted_directories, self.current_common_parent_ids)

        if self.save_callback:
            self.save_callback(settings)

        print("Saving settings:", settings)
        self.destroy()

# if __name__ == "__main__":
#     # Example usage
#     defaults = {
#         'cpu_threshold': 1.5,
#         'memory_threshold': 50000000,
#         'trusted_directories': ['C:\\Windows\\', 'C:\\Program Files\\'],
#         'common_parent_ids': [0, 4]
#     }
#     root = tk.Tk()
#     app = ProcessSettingsWindow(root, defaults)
#     root.mainloop()
