import tkinter as tk


class UserAnalysisSettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title("User Analysis Settings")
        self.geometry("300x500")
        self.save_callback = save_callback
        self.defaults = defaults
        self.create_widgets()
        self.populate_default_users()

    def create_widgets(self):
        self.lbl_users = tk.Label(self, text="Default Users")
        self.lbl_users.grid(row=0, column=0, padx=10, pady=10)

        self.lst_users = tk.Listbox(self)
        self.lst_users.grid(row=1, column=0, padx=10, pady=10)

        self.user_entry = tk.Entry(self)
        self.user_entry.grid(row=2, column=0, padx=10, pady=10)

        self.btn_add_user = tk.Button(self, text="Add", command=self.add_user)
        self.btn_add_user.grid(row=2, column=1, padx=10, pady=10)

        self.btn_modify_user = tk.Button(self, text="Modify", command=self.modify_user)
        self.btn_modify_user.grid(row=3, column=1, padx=10, pady=10)

        self.btn_delete_user = tk.Button(self, text="Delete", command=self.delete_user)
        self.btn_delete_user.grid(row=4, column=1, padx=10, pady=10)

        self.btn_save = tk.Button(self, text="Save and exit", command=self.save_settings)
        self.btn_save.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cancel = tk.Button(self, text="Cancel", command=self.destroy)
        self.btn_cancel.grid(row=5, column=1, padx=10, pady=10)

    def populate_default_users(self):
        for user in self.defaults:
            self.lst_users.insert(tk.END, user)

    def add_user(self):
        user = self.user_entry.get()
        if user:
            self.lst_users.insert(tk.END, user)
            self.user_entry.delete(0, tk.END)

    def modify_user(self):
        selected = self.lst_users.curselection()
        if selected:
            user = self.user_entry.get()
            if user:
                self.lst_users.delete(selected[0])
                self.lst_users.insert(selected[0], user)
                self.user_entry.delete(0, tk.END)

    def delete_user(self):
        selected = self.lst_users.curselection()
        if selected:
            self.lst_users.delete(selected[0])

    def save_settings(self):
        users = [self.lst_users.get(i) for i in range(self.lst_users.size())]

        if self.save_callback:
            self.save_callback(users)

        self.destroy()
