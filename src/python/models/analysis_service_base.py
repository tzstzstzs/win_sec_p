from abc import ABC, abstractmethod
import logging


class AnalysisServiceBase(ABC):
    def __init__(self, data, settings):
        self.data = data
        self.settings = settings
        self.log_initialization()

    def log_initialization(self):
        logging.info(f"{self.__class__.__name__} initialized with data and settings [service]")

    @abstractmethod
    def analyze(self):
        """
        Perform the analysis specific to the service.
        """
        pass
