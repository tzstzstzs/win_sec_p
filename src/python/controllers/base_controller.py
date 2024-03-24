from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self, main_window):
        self.main_window = main_window
        self.data = []

    @abstractmethod
    def retrieve_data(self):
        """
        Retrieve data from a source.
        """
        pass

    @abstractmethod
    def show_data(self):
        """
        Display the data in UI.
        """
        pass
