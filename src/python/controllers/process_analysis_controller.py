import logging
from src.python.view.process_analysis_window import ProcessAnalysisWindow
from src.python.models.process_analysis_service import ProcessAnalysisService
from src.python.view.process_settings_window import ProcessSettingsWindow
from src.python.models.settings_manager import SettingsManager
from tkinter import messagebox


class ProcessAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = {}
        self.settings_manager = SettingsManager()
        # Load 'default_processes' settings using SettingsManager
        self.process_analysis_settings = self.settings_manager.get_setting('default_processes')

    def perform_process_analysis(self, process_data):
        logging.info("Attempting to analyze process data [controller].")
        try:
            analysis_service = ProcessAnalysisService(process_data, self.process_analysis_settings)
            self.analysis_results = analysis_service.analyze_processes()
            self.main_window.enable_button(self.main_window.running_processes_section[4])
            logging.info("Successfully analyzed process data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze process data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing process data: {e}")
            return None

    def show_process_analysis(self):
        if self.analysis_results:
            try:
                ProcessAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying process analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the process analysis.")
        else:
            logging.warning("No process analysis data available to display [controller].")
            messagebox.showinfo("Process Analysis", "No process analysis data available.")

    def open_process_analysis_settings(self):
        # Load current 'default_processes' settings for display
        current_settings = self.settings_manager.get_setting('default_processes')
        self.settings_window = ProcessSettingsWindow(
            self.main_window,
            save_callback=self.save_process_analysis_settings,
            defaults=current_settings  # Pass current settings to settings window
        )
        self.settings_window.grab_set()  # Make the settings window modal

    def save_process_analysis_settings(self, settings):
        # Save the updated 'default_processes' settings
        self.settings_manager.update_setting('default_processes', settings)
        self.process_analysis_settings = settings
        logging.info(f"Process analysis settings saved: {self.process_analysis_settings}")