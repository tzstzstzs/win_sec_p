import logging
from src.python.models.analysis_service_base import AnalysisServiceBase


class AppsAnalysisService(AnalysisServiceBase):
    def analyze(self):
        unauthorized_apps = []

        # Check each installed app against the authorized apps list
        for app in self.data:
            try:
                if not any(app['DisplayName'] == authorized_app['Name'] and
                           app.get('DisplayVersion') == authorized_app['Version'] and
                           app.get('Publisher') == authorized_app['Vendor']
                           for authorized_app in self.settings):
                    unauthorized_apps.append({
                        'Name': app['DisplayName'],
                        'Version': app.get('DisplayVersion'),
                        'Vendor': app.get('Publisher'),
                        'InstallDate': app.get('InstallDate')
                    })
            except KeyError as e:
                logging.error(f"KeyError during apps analysis: {e} [service]")
            except TypeError as e:
                logging.error(f"TypeError during apps analysis: {e} [service]")
            except Exception as e:
                logging.exception(
                    f"Unexpected error during apps analysis for app {app.get('DisplayName', 'Unknown')} [service]")

        return unauthorized_apps
