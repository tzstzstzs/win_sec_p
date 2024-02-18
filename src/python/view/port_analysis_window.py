import tkinter as tk
from tkinter import ttk


class PortAnalysisWindow(tk.Toplevel):
    def __init__(self, parent, vulnerable_ports):
        super().__init__(parent)
        self.title("Port Analysis")
        self.geometry('300x400')
        self.parent = parent
        self.vulnerable_ports = vulnerable_ports

        # Create a frame for the label, list, and scrollbar
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a label to display the specified text
        label = ttk.Label(frame, text="The following ports may be vulnerable:")
        label.pack(side=tk.TOP, fill=tk.X)

        # Create a frame for the listbox and scrollbar
        list_frame = ttk.Frame(frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox to display vulnerable ports
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure scrollbar
        scrollbar.config(command=self.listbox.yview)

        # Populate the listbox
        for port in vulnerable_ports:
            self.listbox.insert(tk.END, port)
