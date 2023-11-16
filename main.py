# main.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.python.services.user_service import get_windows_users_with_powershell

class UserListApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Windows Security Application')
        self.geometry('800x600')

        self.tree = ttk.Treeview(self)
        self.tree['columns'] = ('Username', 'Description', 'Enabled', 'LastLogon', 'Groups')

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = ttk.Button(self, text='Refresh User List', command=self.populate_user_list)
        self.refresh_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.populate_user_list()

    def populate_user_list(self):
        try:
            users_data = get_windows_users_with_powershell()
            if isinstance(users_data, list):  # Check if the returned data is a list
                for i in self.tree.get_children():
                    self.tree.delete(i)  # Clear the current list
                for user in users_data:
                    if isinstance(user, dict):  # Check if each user is a dictionary
                        # Unpack user details safely
                        self.tree.insert('', tk.END, values=(
                            user.get('Username', ''),
                            user.get('Description', ''),
                            user.get('Enabled', ''),
                            user.get('LastLogon', ''),
                            user.get('Groups', '')
                        ))
            else:
                raise TypeError("The returned data is not a list.")
        except Exception as e:
            print(f"Error retrieving users: {e}")
            messagebox.showerror("Error", f"Unable to retrieve user data: {e}")  # Corrected usage

if __name__ == '__main__':
    app = UserListApplication()
    app.mainloop()
