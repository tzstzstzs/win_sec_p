import logging
from src.python.models.analysis_service_base import AnalysisServiceBase


class PortAnalysisService(AnalysisServiceBase):
    def analyze(self):
        self.settings = [int(port) for port in self.settings if port.isdigit()] if self.settings else []
        vulnerabilities = []
        for port in self.data:
            try:
                if port['LocalPort'] in self.settings:
                    vulnerabilities.append(port['LocalPort'])
            except KeyError as e:
                logging.error(f"KeyError during port analysis: {e} [service]")
            except TypeError as e:
                logging.error(f"TypeError during port analysis: {e} [service]")
            except Exception as e:
                logging.exception(
                    f"Unexpected error during port analysis for port {port.get('PortNumber', 'Unknown')} [service]")
        return vulnerabilities
