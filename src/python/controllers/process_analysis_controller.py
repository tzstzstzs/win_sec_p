import logging
from src.python.view.process_analysis_window import ProcessAnalysisWindow
from src.python.models.process_analysis_service import ProcessAnalysisService
from src.python.view.process_settings_window import ProcessSettingsWindow
from tkinter import messagebox


class ProcessAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = {}
        self.default_processes = {
            'cpu_threshold': '8000.0',
            'memory_threshold': '1024.0',
            'trusted_directories': ['C:\\Windows\\', 'C:\\Program Files\\'],
            'common_parent_ids': ['4', '68', '100', '884'] # TBD
        }

        self.process_analysis_settings = self.default_processes

    def perform_process_analysis(self, process_data):
        logging.info("Attempting to analyze process data [controller].")
        try:
            # Pass the user data to the analysis service
            analysis_service = ProcessAnalysisService(process_data, self.process_analysis_settings)
            self.analysis_results = analysis_service.analyze_processes()
            self.main_window.enable_button(self.main_window.running_processes_section[4])
            logging.info("Successfully analyzed process data [controller].")
            print(self.process_analysis_settings)
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
        self.settings_window = ProcessSettingsWindow(
            self.main_window,
            save_callback=self.save_process_analysis_settings,
            defaults=self.default_processes
        )
        self.settings_window.grab_set()  # Make the settings window modal

    def save_process_analysis_settings(self, settings):
        self.process_analysis_settings = settings
        logging.info(f"Process analysis settings saved: {self.process_analysis_settings}")