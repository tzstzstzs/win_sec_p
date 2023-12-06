import ctypes
import os
import sys
from src.python.controllers.main_controller import MainController
from src.python.view.main_window import MainWindow


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':
    if is_admin():
        main_window = MainWindow()
        main_controller = MainController(main_window)
        main_controller.run()
    else:
        # Relaunch the program with admin rights
        script = os.path.abspath(__file__)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "pythonw", script, None, 1)
