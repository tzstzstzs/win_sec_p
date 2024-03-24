from abc import ABC, abstractmethod
from src.python.models.settings_manager import SettingsManager
import logging
from tkinter import messagebox


class BaseAnalysisController(ABC):
    def __init__(self, main_window, settings_key):
        self.main_window = main_window
        self.analysis_results = []
        self.settings_manager = SettingsManager()
        self.analysis_settings = self.settings_manager.get_setting(settings_key)
        self.settings_window = None

    @abstractmethod
    def perform_analysis(self, data):
        """
        Perform analysis based on the provided data. This method should set
        self.analysis_results with the result of the analysis.
        """
        pass

    @abstractmethod
    def show_analysis_results(self):
        """
        Display the analysis results in UI window. This method should use
        self.analysis_results to show the data.
        """
        pass


    def open_settings_window(self, settings_window_class, settings_key):
        """
        Open the settings window for analysis.
        """
        if not self.settings_window or not self.settings_window.winfo_exists():
            current_settings = self.settings_manager.get_setting(settings_key)
            self.settings_window = settings_window_class(
                self.main_window,
                save_callback=self.save_analysis_settings,
                defaults=current_settings
            )
            self.settings_window.grab_set()
        else:
            self.settings_window.focus_set()

    @abstractmethod
    def save_analysis_settings(self, settings):
        """
        Save the updated settings for the analysis.
        """
        pass