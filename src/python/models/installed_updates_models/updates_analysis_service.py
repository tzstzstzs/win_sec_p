import logging
from src.python.models.analysis_service_base import AnalysisServiceBase


class UpdatesAnalysisService(AnalysisServiceBase):
    def analyze(self):
        missing_updates = []

        try:
            # self.settings must list of strings (KB numbers)
            authorized_updates_set = set(self.settings)
            installed_updates_set = set()
            for update in self.data:
                try:
                    installed_updates_set.add(update['HotFixID'])
                except KeyError as e:
                    logging.error(f"KeyError accessing 'HotFixID' in update data: {e} [service]")
                except TypeError as e:
                    logging.error(f"TypeError with update data, expected dict got {type(update)}: {e} [service]")

            # Identify missing updates by comparing the sets
            missing_updates_set = authorized_updates_set - installed_updates_set
            missing_updates.extend(list(missing_updates_set))

        except Exception as e:
            logging.exception(f"Unexpected error during updates analysis: {e} [service]")

        return missing_updates
