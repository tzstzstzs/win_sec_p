import ctypes
import logging
import os
from tkinter import messagebox

from src.python.controllers.main_controller import MainController
from src.python.view.main_window import MainWindow

# Setup logging
logging.basicConfig(level=logging.ERROR, filename='error.log')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error(f"Error checking admin status: {e}")
        return False


def relaunch_with_admin_rights():
    try:
        script = os.path.abspath(__file__)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", script, None, 1)
    except Exception as e:
        logging.error(f"Error relaunching with admin rights: {e}")
        messagebox.showerror("Error", "Failed to relaunch with administrative privileges.")


if __name__ == '__main__':
    if is_admin():
        try:
            main_window = MainWindow()
            main_controller = MainController(main_window)
            main_controller.run()
        except Exception as e:
            logging.error(f"Unhandled exception: {e}")
            messagebox.showerror("Fatal Error", "An unexpected error occurred. Please check the log file.")
    else:
        relaunch_with_admin_rights()
