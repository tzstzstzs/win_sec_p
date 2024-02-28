import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class AppsAnalysisSettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title('Apps Analysis Settings')
        self.geometry('1000x600')  # Increased window size for better readability
        self.save_callback = save_callback
        self.authorized_apps = defaults if isinstance(defaults, list) else []
        # print(defaults)
        # # Initialize variables for authorized apps
        # self.authorized_apps = self.defaults.get('authorized_apps', [])

        self.create_widgets()

    def create_widgets(self):
        self.create_listbox_section('Authorized Apps:', self.authorized_apps, 0, 'authorized_apps')

        # Save and Cancel buttons
        ttk.Button(self, text="Save", command=self.save_settings).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self, text="Cancel", command=self.destroy).grid(row=1, column=1, padx=10, pady=10)

    def create_listbox_section(self, label_text, items, row, list_name):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky='w', padx=10, pady=10)
        listbox = tk.Listbox(self, width=80)  # Increased width for listbox
        listbox.grid(row=row, column=1, sticky='ew', padx=10, pady=10)

        for item in items:
            listbox.insert(tk.END, f"{item['Name']} - {item['Version']} - {item['Vendor']}")

        # Edit and Delete buttons for list items
        ttk.Button(self, text="Edit", command=lambda lb=listbox, ln=list_name: self.edit_list_item(lb, ln)).grid(row=row, column=2, padx=10, pady=10)
        ttk.Button(self, text="Delete", command=lambda lb=listbox, ln=list_name: self.delete_list_item(lb, ln)).grid(row=row, column=3, padx=10, pady=10)
        ttk.Button(self, text="Add", command=lambda lb=listbox, ln=list_name: self.add_list_item(lb, ln)).grid(row=row, column=4, padx=10, pady=10)

    def edit_list_item(self, listbox, list_name):
        selected = listbox.curselection()
        if selected:
            current_item = getattr(self, list_name)[selected[0]]
            new_item_name = simpledialog.askstring("Edit Item", "Edit item name:", initialvalue=current_item['Name'])
            new_item_version = simpledialog.askstring("Edit Item", "Edit item version:", initialvalue=current_item['Version'])
            new_item_vendor = simpledialog.askstring("Edit Item", "Edit item vendor:", initialvalue=current_item['Vendor'])
            if new_item_name and new_item_version and new_item_vendor:
                updated_item = {"Name": new_item_name, "Version": new_item_version, "Vendor": new_item_vendor}
                getattr(self, list_name)[selected[0]] = updated_item
                listbox.delete(selected[0])
                listbox.insert(selected[0], f"{new_item_name} - {new_item_version} - {new_item_vendor}")

    def delete_list_item(self, listbox, list_name):
        selected = listbox.curselection()
        if selected:
            getattr(self, list_name).pop(selected[0])
            listbox.delete(selected[0])

    def add_list_item(self, listbox, list_name):
        new_item_name = simpledialog.askstring("Add New Item", "Enter new item name:")
        new_item_version = simpledialog.askstring("Add New Item", "Enter new item version:")
        new_item_vendor = simpledialog.askstring("Add New Item", "Enter new item vendor:")
        if new_item_name and new_item_version and new_item_vendor:
            new_item = {"Name": new_item_name, "Version": new_item_version, "Vendor": new_item_vendor}
            getattr(self, list_name).append(new_item)
            listbox.insert(tk.END, f"{new_item_name} - {new_item_version} - {new_item_vendor}")

    def save_settings(self):
        # Prepare the data for saving
        settings = {
            'authorized_apps': self.authorized_apps
        }
        if self.save_callback:
            self.save_callback(settings)
        self.destroy()

#
# if __name__ == "__main__":
#     def save_callback(data):
#         print("Settings to save:", data)
#
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window
#     app = AppsAnalysisSettingsWindow(root, save_callback=save_callback, defaults={})
#     app.mainloop()
