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
        # Label and entry for Maximum Logoff Time
        ttk.Label(self, text="Maximum Logoff Time (minutes):").pack(pady=(10, 0))
        self.logoff_time_entry = ttk.Entry(self)
        self.logoff_time_entry.pack(pady=(0, 10))
        self.logoff_time_entry.insert(0, self.defaults.get('logoff_time', ''))  # Set default

        # Label and entry for Minimum Password Age
        ttk.Label(self, text="Minimum Password Age:").pack()
        self.min_age_entry = ttk.Entry(self)
        self.min_age_entry.pack(pady=10)
        self.min_age_entry.insert(0, self.defaults.get('min_age', ''))  # Set default

        # Label and entry for Maximum Password Age
        ttk.Label(self, text="Maximum Password Age:").pack()
        self.max_age_entry = ttk.Entry(self)
        self.max_age_entry.pack(pady=10)
        self.max_age_entry.insert(0, self.defaults.get('max_age', ''))  # Set default

        # Label and entry for Minimum Password Length
        ttk.Label(self, text="Minimum Password Length:").pack(pady=(10, 0))
        self.min_length_entry = ttk.Entry(self)
        self.min_length_entry.pack(pady=(0, 10))
        self.min_length_entry.insert(0, self.defaults.get('min_length', ''))  # Set default

        # Label and entry for Password History
        ttk.Label(self, text="Password History:").pack()
        self.history_entry = ttk.Entry(self)
        self.history_entry.pack(pady=10)
        self.history_entry.insert(0, self.defaults.get('history', ''))  # Set default

        # Label and entry for Lockout Threshold
        ttk.Label(self, text="Lockout Threshold:").pack()
        self.lockout_threshold_entry = ttk.Entry(self)
        self.lockout_threshold_entry.pack(pady=10)
        self.lockout_threshold_entry.insert(0, self.defaults.get('lockout_threshold', ''))  # Set default

        # Label and entry for Lockout Duration
        ttk.Label(self, text="Lockout Duration:").pack()
        self.lockout_duration_entry = ttk.Entry(self)
        self.lockout_duration_entry.pack(pady=10)
        self.lockout_duration_entry.insert(0, self.defaults.get('lockout_duration', ''))  # Set default

        # Label and entry for Lockout Observation Window
        ttk.Label(self, text="Lockout Observation Window:").pack()
        self.lockout_obs_win_entry = ttk.Entry(self)
        self.lockout_obs_win_entry.pack(pady=10)
        self.lockout_obs_win_entry.insert(0, self.defaults.get('lockout_obs_win', ''))  # Set default

        # Save Button
        save_button = ttk.Button(self, text="Save", command=self.save_settings)
        save_button.pack(side='left', padx=10, pady=10)

        # Cancel Button
        cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        cancel_button.pack(side='right', padx=10, pady=10)

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

        # You can now use these values to update your settings
        print(f"Settings saved: logoff time: {settings['logoff_time']}, min length: {settings['min_length']}, max age: {settings['max_age']}, min age: {settings['min_age']}, history: {settings['history']}, lockout threshold {settings['lockout_threshold']}, lockout duration {settings['lockout_duration']}, lockout observation window {settings['lockout_obs_win']}")
        self.destroy()  # Close the window after saving
