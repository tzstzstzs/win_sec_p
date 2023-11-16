import tkinter as tk
from tkinter import ttk
from src.python.services.user_service import get_windows_users
import os
os.environ['PYTHONIOENCODING'] = 'UTF-8'

class UserListApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Windows Security Application')
        self.geometry('600x400')

        unicode_font = ('Arial Unicode MS', 10)
        self.user_listbox = tk.Listbox(self, font=unicode_font)
        self.user_listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = ttk.Button(self, text='Refresh User List', command=self.populate_user_list)
        self.refresh_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.populate_user_list()

    def populate_user_list(self):
        try:
            users = get_windows_users()
            self.user_listbox.delete(0, tk.END)  # Clear the current list
            for user in users:
                self.user_listbox.insert(tk.END, user)  # Insert new user list
        except Exception as e:
            print(f"Error retrieving users: {e}")
            tk.messagebox.showerror("Error", f"Unable to retrieve user data: {e}")

if __name__ == '__main__':
    app = UserListApplication()
    app.mainloop()
