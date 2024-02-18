import logging
from src.python.view.port_analysis_window import PortAnalysisWindow
from src.python.models.port_analysis_service import PortAnalysisService
from src.python.view.port_analysis_settings_window import PortAnalysisSettingsWindow
from src.python.models.settings_manager import SettingsManager
from tkinter import messagebox


class PortAnalysisController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.analysis_results = []
        self.settings_manager = SettingsManager()

        # Load settings
        self.port_analysis_settings = self.settings_manager.get_setting('suspicious_ports')
        self.settings_window = None

    def perform_port_analysis(self, port_data):
        logging.info("Attempting to analyze ports data [controller].")
        try:
            analysis_service = PortAnalysisService(port_data, self.port_analysis_settings)
            self.analysis_results = analysis_service.analyze_ports()
            self.main_window.enable_button(self.main_window.port_list_section[4])
            logging.info("Successfully analyzed ports data [controller].")
            return self.analysis_results
        except Exception as e:
            logging.error(f"Failed to analyze ports data [controller]: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred while analyzing ports data: {e}")
            return None

    def open_analysis_window(self):
        if self.analysis_results:
            try:
                PortAnalysisWindow(self.main_window, self.analysis_results)
            except Exception as e:
                logging.error(f"Error displaying ports analysis [controller]: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the ports analysis.")
        else:
            logging.warning("No ports analysis data available to display [controller].")
            messagebox.showinfo("User Analysis", "No user analysis data available.")

    def open_ports_settings_window(self):
        # Check if the settings window is already open
        if not self.settings_window or not self.settings_window.winfo_exists():
            current_settings = self.settings_manager.get_setting('suspicious_ports')
            self.settings_window = PortAnalysisSettingsWindow(
                self.main_window,
                save_callback=self.save_port_analysis_settings,
                defaults=current_settings
            )
            self.settings_window.grab_set()
        else:
            # Bring the existing settings window to focus
            self.settings_window.focus_set()

    def save_port_analysis_settings(self, settings):
        # Save the updated 'default_users' settings
        self.settings_manager.update_setting('suspicious_ports', settings)
        self.port_analysis_settings = settings
        logging.info(f"Port analysis settings saved: {self.port_analysis_settings}")
