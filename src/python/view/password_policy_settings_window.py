import tkinter as tk
from tkinter import ttk


class PasswordPolicySettingsWindow(tk.Toplevel):
    def __init__(self, parent, save_callback=None, defaults=None):
        super().__init__(parent)
        self.title("Password Policy Settings")
        self.geometry("500x600")  # Adjusted size for additional fields
        self.save_callback = save_callback
        self.defaults = defaults if defaults is not None else {}

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Configure the grid layout
        self.columnconfigure(1, weight=1)  # Makes the entry fields expand

        # Add widgets using grid
        ttk.Label(self, text="Maximum Logoff Time (minutes):").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.logoff_time_entry = ttk.Entry(self)
        self.logoff_time_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        self.logoff_time_entry.insert(0, self.defaults.get('logoff_time', ''))

        ttk.Label(self, text="Minimum Password Age:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.min_age_entry = ttk.Entry(self)
        self.min_age_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
        self.min_age_entry.insert(0, self.defaults.get('min_age', ''))

        ttk.Label(self, text="Maximum Password Age:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.max_age_entry = ttk.Entry(self)
        self.max_age_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=5)
        self.max_age_entry.insert(0, self.defaults.get('max_age', ''))

        ttk.Label(self, text="Minimum Password Length:").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.min_length_entry = ttk.Entry(self)
        self.min_length_entry.grid(row=3, column=1, sticky='ew', padx=5, pady=5)
        self.min_length_entry.insert(0, self.defaults.get('min_length', ''))

        ttk.Label(self, text="Password History:").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        self.history_entry = ttk.Entry(self)
        self.history_entry.grid(row=4, column=1, sticky='ew', padx=5, pady=5)
        self.history_entry.insert(0, self.defaults.get('history', ''))

        ttk.Label(self, text="Lockout Threshold:").grid(row=5, column=0, sticky='e', padx=5, pady=5)
        self.lockout_threshold_entry = ttk.Entry(self)
        self.lockout_threshold_entry.grid(row=5, column=1, sticky='ew', padx=5, pady=5)
        self.lockout_threshold_entry.insert(0, self.defaults.get('lockout_threshold', ''))

        ttk.Label(self, text="Lockout Duration:").grid(row=6, column=0, sticky='e', padx=5, pady=5)
        self.lockout_duration_entry = ttk.Entry(self)
        self.lockout_duration_entry.grid(row=6, column=1, sticky='ew', padx=5, pady=5)
        self.lockout_duration_entry.insert(0, self.defaults.get('lockout_duration', ''))

        ttk.Label(self, text="Lockout Observation Window:").grid(row=7, column=0, sticky='e', padx=5, pady=5)
        self.lockout_obs_win_entry = ttk.Entry(self)
        self.lockout_obs_win_entry.grid(row=7, column=1, sticky='ew', padx=5, pady=5)
        self.lockout_obs_win_entry.insert(0, self.defaults.get('lockout_obs_win', ''))

        # Save and Cancel Buttons
        save_button = ttk.Button(self, text="Save", command=self.save_settings)
        save_button.grid(row=8, column=0, padx=10, pady=20, sticky='e')
        cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        cancel_button.grid(row=8, column=1, padx=10, pady=20, sticky='w')

    def save_settings(self):
        # Gather settings into a dictionary
        settings = {
            'logoff_time': self.logoff_time_entry.get(),
            'min_length': self.min_length_entry.get(),
            'max_age': self.max_age_entry.get(),
            'min_age': self.min_age_entry.get(),
            'history': self.history_entry.get(),
            'lockout_threshold': self.lockout_threshold_entry.get(),
            'lockout_duration': self.lockout_duration_entry.get(),
            'lockout_obs_win': self.lockout_obs_win_entry.get()
        }

        # Call the save callback function if it's set
        if self.save_callback:
            self.save_callback(settings)

        print(f"Settings saved: logoff time: {settings['logoff_time']}, min length: {settings['min_length']}, max age: {settings['max_age']}, min age: {settings['min_age']}, history: {settings['history']}, lockout threshold {settings['lockout_threshold']}, lockout duration {settings['lockout_duration']}, lockout observation window {settings['lockout_obs_win']}")
        self.destroy()  # Close the window after saving
