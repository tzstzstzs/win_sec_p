from src.python.view.main_window import MainWindow
from src.python.controllers.main_controller import MainController

if __name__ == '__main__':
    main_window = MainWindow()
    main_controller = MainController(main_window)
    main_controller.run()
