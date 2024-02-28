import logging


class UserAnalysisService:
    def __init__(self, user_data, user_settings):
        self.user_data = user_data
        self.user_settings = user_settings
        logging.info("UserAnalysisService initialized with user data and settings [service]")

    def analyze_users(self):
        vulnerabilities = []
        for user in self.user_data:
            try:
                # Check if user is enabled and present in settings
                if user['Username'] in self.user_settings and user['Enabled']:
                    vulnerabilities.append(user['Username'])
            except KeyError as e:
                # Log missing key error
                logging.error(f"KeyError during user analysis: {e} [service]")
            except TypeError as e:
                # Log wrong data type error
                logging.error(f"TypeError during user analysis: {e} [service]")
            except Exception as e:
                # Log any other unexpected exception
                logging.exception(f"Unexpected error during user analysis for user {user.get('Username', 'Unknown')} [service]")

        return vulnerabilities
