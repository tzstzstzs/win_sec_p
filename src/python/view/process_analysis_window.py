import tkinter as tk
from tkinter import ttk


class ProcessAnalysisWindow(tk.Toplevel):
    def __init__(self, parent, analysis_result):
        super().__init__(parent)
        self.title('Process Analysis Result')
        self.geometry('800x300')  # Note the lowercase 'x' in the geometry string
        self.analysis_result = analysis_result
        self.create_result_list()

    def create_result_list(self):
        # Create a notebook widget
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        # High Resource Processes Tab
        high_resource_frame = ttk.Frame(notebook)
        notebook.add(high_resource_frame, text='High Resource Processes')
        self.create_process_tree(high_resource_frame, self.analysis_result['high_resource'], 'High Resource')

        # Unusual Processes Tab
        unusual_activity_frame = ttk.Frame(notebook)
        notebook.add(unusual_activity_frame, text='Unusual Activity Processes')
        self.create_process_tree(unusual_activity_frame, self.analysis_result['unusual_activity'], 'Unusual Activity')

    def create_process_tree(self, parent, processes, category):
        # Create the Treeview widget
        tree = ttk.Treeview(parent, columns=('Process Name', 'ID'), show='headings')
        tree.heading('Process Name', text='Process Name')
        tree.heading('ID', text='ID')
        tree.column('Process Name', width=400)
        tree.column('ID', width=100)

        # Add data to the tree
        for process in processes:
            tree.insert('', tk.END, values=(process['ProcessName'], process['Id']))

        # Pack the Treeview widget
        tree.pack(expand=True, fill='both')

# if __name__ == "__main__":
#     # Example usage
#     dummy_results = {
#         'high_resource': [{'ProcessName': 'ProcessA', 'Id': 1}],
#         'unusual_activity': [{'ProcessName': 'ProcessB', 'Id': 2}]
#     }
#     root = tk.Tk()
#     app = ProcessAnalysisWindow(root, analysis_result=dummy_results)
#     root.mainloop()