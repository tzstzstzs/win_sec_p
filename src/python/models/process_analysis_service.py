import logging


class ProcessAnalysisService:
    def __init__(self, process_data, settings):
        self.process_data = process_data
        self.settings = settings
        self.suspicious_processes = {'high_resource': [], 'unusual_activity': []}

    def is_high_resource_process(self, process):
        try:
            # Retrieve the thresholds and ensure they are not lists
            cpu_threshold = self.settings.get('cpu_threshold', ['8000.0'])
            memory_threshold = self.settings.get('memory_threshold', ['1024.0'])

            # If the thresholds are lists, take the first element
            cpu_threshold = cpu_threshold[0] if isinstance(cpu_threshold, list) else cpu_threshold
            memory_threshold = memory_threshold[0] if isinstance(memory_threshold, list) else memory_threshold

            # Parse the CPU and WorkingSet values, assuming they could be non-numeric
            cpu_usage = self._parse_value(process.get('CPU'))
            memory_usage = self._parse_value(process.get('WorkingSet'))

            if cpu_usage is None or memory_usage is None:
                # If parsing failed, log and return False
                logging.error(f"Could not parse CPU or memory usage for process: {process.get('ProcessName')}")
                return False

            return cpu_usage > float(cpu_threshold) or memory_usage > float(memory_threshold)
        except KeyError as e:
            logging.error(f"Key missing in process data: {e}")
            return False
        except Exception as e:
            logging.exception(
                f"Unexpected error in is_high_resource_process for process {process.get('ProcessName', 'Unknown')}: {e}")
            return False

    def is_unusual_process(self, process):
        # Checks if the process is unusual
        trusted_directories = self.settings.get('trusted_directories', ['C:\\Windows\\', 'C:\\Program Files\\'])
        common_parent_ids = self.settings.get('common_parent_ids', [0, 4])

        executable_path = process['ExecutablePath']
        parent_id = process['ParentId']
        return (not any(trusted_dir in executable_path for trusted_dir in trusted_directories)) or (
                    parent_id not in common_parent_ids)

    def analyze_processes(self):
        """
        Performs all analyses on each process and updates the suspicious_processes collection.
        """
        for process in self.process_data:
            try:
                simplified_process = {'ProcessName': process['ProcessName'], 'Id': process['Id']}

                if self.is_high_resource_process(process):
                    self.suspicious_processes['high_resource'].append(simplified_process)

                if self.is_unusual_process(process):
                    self.suspicious_processes['unusual_activity'].append(simplified_process)

            except KeyError as e:
                # Log an error when a process dictionary key is missing
                logging.error(f"KeyError in process analysis for process {process.get('ProcessName', 'Unknown')}: {e}",
                              exc_info=True)
            except TypeError as e:
                # Log an error when there is a type mismatch in comparisons
                logging.error(f"TypeError in process analysis for process {process.get('ProcessName', 'Unknown')}: {e}",
                              exc_info=True)
            except Exception as e:
                # Catch-all for any other exceptions that were not anticipated
                logging.error(
                    f"Unexpected error in process analysis for process {process.get('ProcessName', 'Unknown')}: {e}",
                    exc_info=True)

        return self.suspicious_processes

    def _parse_value(self, value):
        """Converts a value to a float if possible, otherwise logs and returns None."""
        try:
            return float(value)
        except (TypeError, ValueError):
            logging.error(f"Value cannot be converted to float: {value}")
            return None
