import tkinter as tk
from tkinter import ttk

class PortListWindow(tk.Toplevel):
    def __init__(self, parent, open_ports):
        super().__init__(parent)
        self.title('Open Ports')
        self.geometry('300x200')
        self.create_widgets(open_ports)

    def create_widgets(self, open_ports):
        if open_ports:
            self.listbox = tk.Listbox(self)
            self.listbox.pack(fill=tk.BOTH, expand=True)
            for port in open_ports:
                self.listbox.insert(tk.END, f'Port {port}: OPEN')
        else:
            tk.Label(self, text='No open ports found.').pack(pady=20)
