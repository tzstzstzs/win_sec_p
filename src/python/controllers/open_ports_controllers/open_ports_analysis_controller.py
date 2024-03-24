import logging
from src.python.view.open_ports_view.open_ports_analysis_window import PortAnalysisWindow
from src.python.models.open_ports_models.open_ports_analysis_service import PortAnalysisService
from src.python.view.open_ports_view.open_ports_analysis_settings_window import PortAnalysisSettingsWindow
from tkinter import messagebox
from src.python.controllers.base_analysis_controller import BaseAnalysisController


class PortAnalysisController(BaseAnalysisController):
    def __init__(self, main_window):
        super().__init__(main_window, 'suspicious_ports')

    def perform_analysis(self, port_data):
        logging.info("Attempting to analyze ports data [controller].")
        try:
            analysis_service = PortAnalysisService(port_data, self.analysis_settings)
            self.analysis_results = analysis_service.analyze()
            self.main_window.enable_button(self.main_window.port_list_section[4])
            logging.info("Successfully analyzed ports data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze ports data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing ports data: {e}")
            return None

    def show_analysis_results(self):
        if self.analysis_results:
            try:
                PortAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying ports analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the ports analysis.")
        else:
            logging.warning("No ports analysis data available to display [controller].")
            messagebox.showinfo("User Analysis", "No port analysis data available.")

    def open_settings_window(self):
        super().open_settings_window(PortAnalysisSettingsWindow, 'suspicious_ports')

    def save_analysis_settings(self, settings):
        self.settings_manager.update_setting('suspicious_ports', settings)
        self.port_analysis_settings = settings
        logging.info(f"Port analysis settings saved: {self.port_analysis_settings}")
