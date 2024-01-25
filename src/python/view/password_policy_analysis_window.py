import tkinter as tk
from tkinter import ttk

class PasswordPolicyResultWindow(tk.Toplevel):
    def __init__(self, parent, analysis_result):
        super().__init__(parent)
        self.title('Password Policy Analysis Result')
        self.geometry('800x300')  # Adjust the window size as needed
        self.analysis_result = analysis_result
        self.create_result_list()

    def create_result_list(self):
        self.tree = ttk.Treeview(self, columns=('Policy', 'Status'), show='headings')
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        self.tree.column('Policy', width=250)
        self.tree.column('Status', width=550)
        self.tree.heading('Policy', text='Policy')
        self.tree.heading('Status', text='Status')

        self.populate_result_list()
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def populate_result_list(self):
        for policy, status in self.analysis_result.items():
            self.tree.insert('', tk.END, values=(policy.replace('_', ' ').capitalize(), status))
