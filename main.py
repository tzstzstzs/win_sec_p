import ctypes
import logging
import os
from tkinter import messagebox

from src.python.controllers.main_controller import MainController
from src.python.view.main_window import MainWindow
from src.python.models.check_user_privileges import is_admin

# Configure the root logger
logging.basicConfig(filename='application.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def relaunch_with_admin_rights():
    try:
        script = os.path.abspath(__file__)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "pythonw", script, None, 1)
    except Exception as e:
        logging.error(f"Error relaunching with admin rights: {e}")
        messagebox.showerror("Error", "Failed to relaunch with administrative privileges.")


if __name__ == '__main__':
    admin_status = is_admin()
    if admin_status:
        try:
            main_window = MainWindow(admin_status = admin_status)
            main_controller = MainController(main_window)
            logging.info("Application launched")
            main_controller.run()
        except Exception as e:
            logging.error(f"Unhandled exception: {e}")
            messagebox.showerror("Fatal Error", "An unexpected error occurred. Please check the log file.")
    else:
        relaunch_with_admin_rights()
