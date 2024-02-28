import tkinter as tk
from tkinter import ttk

class UpdatesAnalysisWindow(tk.Toplevel):
    def __init__(self, parent, missing_updates_data):
        super().__init__(parent)
        self.title('Missing Updates')
        self.geometry('400x600')
        # Assuming missing_updates_data is now a list of HotFixIDs as strings
        self.missing_updates_data = missing_updates_data
        self.create_widgets()

    def create_widgets(self):
        # Adjusting the Treeview to have only one column for HotFixID
        self.tree = ttk.Treeview(self, columns=('HotFixID',), show='headings')
        self.tree.heading('HotFixID', text='HotFixID')

        # Inserting each HotFixID into the Treeview
        for hotfix_id in self.missing_updates_data:
            self.tree.insert('', tk.END, values=(hotfix_id,))

        self.tree.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    def sample_missing_updates():
        # Sample list of missing updates represented by their HotFixIDs
        return ['KB123456', 'KB654321']

    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = UpdatesAnalysisWindow(root, sample_missing_updates())
    app.mainloop()
