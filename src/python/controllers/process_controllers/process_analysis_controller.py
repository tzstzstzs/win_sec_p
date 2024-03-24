import logging
from src.python.view.process_view.process_analysis_window import ProcessAnalysisWindow
from src.python.models.process_models.process_analysis_service import ProcessAnalysisService
from src.python.view.process_view.process_settings_window import ProcessSettingsWindow
from tkinter import messagebox
from src.python.controllers.base_analysis_controller import BaseAnalysisController


class ProcessAnalysisController(BaseAnalysisController):
    def __init__(self, main_window):
        super().__init__(main_window, 'default_processes')

    def perform_analysis(self, process_data):
        logging.info("Attempting to analyze process data [controller].")
        try:
            analysis_service = ProcessAnalysisService(process_data, self.analysis_settings)
            self.analysis_results = analysis_service.analyze()
            self.main_window.enable_button(self.main_window.running_processes_section[4])
            logging.info("Successfully analyzed process data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze process data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing process data: {e}")
            return None

    def show_analysis_results(self):
        if self.analysis_results:
            try:
                ProcessAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying process analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the process analysis.")
        else:
            logging.warning("No process analysis data available to display [controller].")
            messagebox.showinfo("Process Analysis", "No process analysis data available.")

    def open_settings_window(self):
        super().open_settings_window(ProcessSettingsWindow, 'default_processes')

    def save_analysis_settings(self, settings):
        self.settings_manager.update_setting('default_processes', settings)
        self.process_analysis_settings = settings
        logging.info(f"Process analysis settings saved: {self.process_analysis_settings}")