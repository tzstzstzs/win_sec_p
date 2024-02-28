import logging


class AppsAnalysisService:
    def __init__(self, installed_apps_data, authorized_apps_settings):
        self.installed_apps_data = installed_apps_data
        self.authorized_apps_settings = authorized_apps_settings
        logging.info("AppsAnalysisService initialized with installed apps data and authorized apps settings [service]")

    def analyze_apps(self):
        unauthorized_apps = []

        # Check each installed app against the authorized apps list
        for app in self.installed_apps_data:
            try:
                # Check if app is not in the list of authorized apps
                if not any(app['DisplayName'] == authorized_app['Name'] and
                           app.get('DisplayVersion') == authorized_app['Version'] and
                           app.get('Publisher') == authorized_app['Vendor']
                           for authorized_app in self.authorized_apps_settings):
                    unauthorized_apps.append({
                        'Name': app['DisplayName'],
                        'Version': app.get('DisplayVersion'),
                        'Vendor': app.get('Publisher'),
                        'InstallDate': app.get('InstallDate')
                    })
            except KeyError as e:
                # Log missing key error
                logging.error(f"KeyError during apps analysis: {e} [service]")
            except TypeError as e:
                # Log wrong data type error
                logging.error(f"TypeError during apps analysis: {e} [service]")
            except Exception as e:
                # Log any other unexpected exception
                logging.exception(
                    f"Unexpected error during apps analysis for app {app.get('DisplayName', 'Unknown')} [service]")

        return unauthorized_apps
