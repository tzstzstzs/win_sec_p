import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.python.services.user_service import get_windows_users_with_powershell


class UserListWindow(tk.Toplevel):
    def __init__(self, parent, users_data):
        super().__init__(parent)
        self.title('User List')
        self.geometry('800x600')
        self.users_data = users_data
        self.create_user_list()

    def create_user_list(self):
        self.tree = ttk.Treeview(self)
        self.tree['columns'] = ('Username', 'Description', 'Enabled', 'LastLogon', 'Groups')

        for col in self.tree['columns']:
            self.tree.column(col, width=150)
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.populate_user_list()

    def populate_user_list(self):
        for user in self.users_data:
            self.tree.insert('', tk.END, values=(
            user['Username'], user['Description'], user['Enabled'], user['LastLogon'], user['Groups']))


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Windows Security Application')
        self.geometry('500x300')
        self.create_widgets()
        self.users_data = []

    def create_widgets(self):
        # Option 1 - User List
        frame1 = ttk.Frame(self)
        frame1.pack(fill=tk.X, padx=5, pady=5)

        self.option1_var = tk.BooleanVar()
        ttk.Checkbutton(frame1, text='User List', variable=self.option1_var).pack(side=tk.LEFT)

        # Store a reference to the button
        self.show_user_list_button = ttk.Button(frame1, text='Show User List', command=self.show_user_list, state='disabled')
        self.show_user_list_button.pack(side=tk.RIGHT)

        # Option 2
        frame2 = ttk.Frame(self)
        frame2.pack(fill=tk.X, padx=5, pady=5)

        self.option2_var = tk.BooleanVar()
        ttk.Checkbutton(frame2, text='Option 2', variable=self.option2_var).pack(side=tk.LEFT)

        # Store a reference to the button
        self.show_option2_button = ttk.Button(frame2, text='Show option2', command=self.show_option2, state='disabled')
        self.show_option2_button.pack(side=tk.RIGHT)

        # Option 3
        frame3 = ttk.Frame(self)
        frame3.pack(fill=tk.X, padx=5, pady=5)

        self.option3_var = tk.BooleanVar()
        ttk.Checkbutton(frame3, text='Option 3', variable=self.option3_var).pack(side=tk.LEFT)

        # Store a reference to the button
        self.show_option3_button = ttk.Button(frame3, text='Show option3', command=self.show_option3, state='disabled')
        self.show_option3_button.pack(side=tk.RIGHT)

        # Run Button
        self.run_button = ttk.Button(self, text='Run Selected Features', command=self.run_selected_features)
        self.run_button.pack(expand=True, padx=5, pady=5)

    def run_selected_features(self):
        if self.option1_var.get():
            try:
                self.users_data = get_windows_users_with_powershell()
                self.show_user_list_button['state'] = 'normal'
            except Exception as e:
                tk.messagebox.showerror("Error", f"Unable to retrieve user data: {e}")
        # Here, you would add logic for other options when they have associated actions

    def show_user_list(self):
        if self.users_data:
            UserListWindow(self, self.users_data)

    def show_option2(self):
        # Placeholder for showing results of Option 2
        pass

    def show_option3(self):
        # Placeholder for showing results of Option 3
        pass


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
