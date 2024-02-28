import logging


class UpdatesAnalysisService:
    def __init__(self, installed_updates_data, authorized_updates_settings):
        self.installed_updates_data = installed_updates_data
        self.authorized_updates_settings = authorized_updates_settings
        logging.info(
            "UpdatesAnalysisService initialized with installed updates data and authorized updates settings [service]")

    def analyze_updates(self):
        missing_updates = []

        # If authorized_updates_settings is a list of strings (KB numbers), use directly
        authorized_updates_set = set(self.authorized_updates_settings)

        # Assuming installed_updates_data is a list of dictionaries where 'HotFixID' contains the KB number
        installed_updates_set = {update['HotFixID'] for update in self.installed_updates_data}

        # Identify missing updates by comparing sets
        missing_updates_set = authorized_updates_set - installed_updates_set

        # Return a list of missing HotFixID as strings
        missing_updates.extend(list(missing_updates_set))

        return missing_updates
