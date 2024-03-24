import logging
from src.python.models.analysis_service_base import AnalysisServiceBase


class UserAnalysisService(AnalysisServiceBase):
    def analyze(self):
        vulnerabilities = []
        for user in self.data:
            try:
                if user['Username'] in self.settings and user['Enabled']:
                    vulnerabilities.append(user['Username'])
            except KeyError as e:
                logging.error(f"KeyError during user analysis: {e} [service]")
            except TypeError as e:
                logging.error(f"TypeError during user analysis: {e} [service]")
            except Exception as e:
                logging.exception(f"Unexpected error during user analysis for user {user.get('Username', 'Unknown')}"
                                  f" [service]")

        return vulnerabilities
