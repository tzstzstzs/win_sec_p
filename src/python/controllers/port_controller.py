import logging
import threading
from tkinter import messagebox
from src.python.models import port_service
from src.python.view.port_list_window import PortListWindow


class PortController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.open_ports_data = []

    def check_ports(self):
        start_port = 440
        end_port = 460
        host = '127.0.0.1'
        self.main_window.start_progress(end_port - start_port + 1)
        logging.info("Starting port scan.")

        threading.Thread(
            target=self.run_port_scan_thread,
            args=(host, start_port, end_port),
            daemon=True
        ).start()

    def run_port_scan_thread(self, host, start_port, end_port):
        try:
            port_service.run_port_scan(
                host,
                start_port,
                end_port,
                self.main_window.update_progress,
                self.complete_port_scan,
                self.error_port_scan
            )
        except Exception as e:
            logging.error(f"Error during port scan: {e}", exc_info=True)
            self.error_port_scan(str(e))

    def complete_port_scan(self, open_ports):
        self.open_ports_data = open_ports
        self.main_window.stop_progress()
        self.main_window.enable_checkports_button()
        logging.info("Port scan completed.")

    def error_port_scan(self, error):
        self.main_window.stop_progress()
        messagebox.showerror("Error", f"Unable to complete port scan: {error}")
        logging.error(f"Port scan failed: {error}")

    def show_open_ports(self):
        if self.open_ports_data:
            try:
                PortListWindow(self.main_window, self.open_ports_data)
            except Exception as e:
                logging.error(f"Error displaying open ports: {e}", exc_info=True)
                messagebox.showerror("Error", "An error occurred while displaying the open ports.")
        else:
            messagebox.showinfo("Open Ports", "No open ports found.")
            logging.info("No open ports to display.")


# Initialize logging at the start of the application
logging.basicConfig(level=logging.INFO, filename='port.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')