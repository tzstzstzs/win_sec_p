import logging


class PasswordPolicyAnalysisService:
    def __init__(self, policy_data, settings):
        self.policy_data = policy_data
        self.settings = settings
        logging.info("PasswordPolicyAnalysisService initialized with policy data [service]")

    def analyze_password_policy(self):
        try:
            # Extract relevant policy values
            logoff_time = self._get_policy_value(1)  # Force logoff time (minutes)
            min_age = self._get_policy_value(2)  # Minimum password age (days)
            max_age = self._get_policy_value(3)  # Maximum password age (days)
            min_length = self._get_policy_value(4)  # Minimum password length
            history = self._get_policy_value(5)  # Length of password history maintained
            lockout_threshold = self._get_policy_value(6)  # Maximum number of login attempts
            lockout_duration = self._get_policy_value(7)  # Lockout duration (minutes)
            lockout_obs_win = self._get_policy_value(8)  # Lockout observation window (minutes)


            # Analyzing password policies based on specified rules
            results = {
                'logoff_time': self._analyze_logoff_time(logoff_time),
                'password_length': self._analyze_length(min_length),
                'max_age': self._analyze_max_age(max_age),
                'min_age': self._analyze_min_age(min_age),
                'history': self._analyze_history(history),
                'lockout_threshold': self._analyze_lockout_threshold(lockout_threshold),
                'lockout_duration': self._analyze_lockout_duration(lockout_duration),
                'lockout_observation_window': self._analyze_lockout_obs_win(lockout_obs_win)
            }
            logging.info("Password policy analysis completed [service]")
            return results

        except Exception as e:
            logging.error("Error in analyzing password policy", exc_info=True)
            raise


    def _get_policy_value(self, index):
        try:
            for policy in self.policy_data:
                if policy["Index"] == index:
                    return policy["Value"]
            logging.warning(f"Policy with Index {index} not found [service]")
            return None
        except Exception as e:
            logging.error(f"Error in getting policy value for index {index} [service]", exc_info=True)
            raise

    def _analyze_logoff_time(self, logoff_time):
        try:
            req_logoff_time = int(self.settings.get('logoff_time', 30))
            logoff_time = int(logoff_time)  # Convert history to an integer
        except ValueError as e:
            logging.error("Invalid data - Force logoff time is not a number", exc_info=True)
            return f"Not Compliant - Force logoff time should be at least {req_logoff_time} minutes"
        except Exception as e:
            logging.error("Unexpected error in _analyze_logoff_time", exc_info=True)
            return "Error analyzing force logoff time"

        if logoff_time <= req_logoff_time:
            return "Compliant"
        else:
            return f"Not Compliant - Force logoff time should be at least {req_logoff_time} minutes"

    def _analyze_length(self, length):
        try:
            required_length = int(self.settings.get('min_length', 8))  # Use the setting, default to 8 if not set
            length = int(length)
        except ValueError as e:
            logging.error("Invalid data - Password length or setting is not a number [service]", exc_info=True)
            return f"Not Compliant - Minimum password length should be at least {required_length} characters"
        except Exception as e:
            logging.error("Unexpected error in _analyze_length [service]", exc_info=True)
            return "Error analyzing password length"

        if length >= required_length:
            return "Compliant"
        else:
            return f"Not Compliant - Minimum password length should be at least {required_length} characters"
    def _analyze_max_age(self, age):
        try:
            required_max_age = int(self.settings.get('max_age', 90))
            age = int(age)  # Convert age to an integer
        except ValueError as e:
            logging.error("Invalid data - Password age is not a number [service]", exc_info=True)
            return f"Not Compliant - Maximum password age should not exceed {required_max_age} days"
        except Exception as e:
            logging.error("Unexpected error in _analyze_max_age [service]", exc_info=True)
            return "Error analyzing password max age"

        if age <= required_max_age:
            return "Compliant"
        else:
            return f"Not Compliant - Maximum password age should not exceed {required_max_age} days"

    def _analyze_min_age(self, age):
        try:
            required_min_age = int(self.settings.get('min_age', 1))
            age = int(age)  # Convert length to an integer
        except ValueError as e:
            logging.error("Invalid data - Password age is not a number [service]", exc_info=True)
            return f"Not Compliant - Minimum password age should be at least {required_min_age} day"
        except Exception as e:
            logging.error("Unexpected error in _analyze_min_age [service]", exc_info=True)
            return "Error analyzing password max age"

        if age >= required_min_age:
            return "Compliant"
        else:
            return f"Not Compliant - Minimum password age should be at least {required_min_age} day"

    def _analyze_history(self, history):
        try:
            required_history = int(self.settings.get('history', 5))
            history = int(history)
        except ValueError as e:
            logging.error("Invalid data - Password history is not a number", exc_info=True)
            return f"Not Compliant - Password history should maintain at least {required_history} unique passwords"
        except Exception as e:
            logging.error("Unexpected error in _analyze_history", exc_info=True)
            return "Error analyzing password history"

        if history >= required_history:
            return "Compliant"
        else:
            return f"Not Compliant - Password history should maintain at least {required_history} unique passwords"

    def _analyze_lockout_threshold(self, lockout_threshold):
        try:
            required_lockout_threshold = int(self.settings.get('lockout_threshold', 5))
            lockout_threshold = int(lockout_threshold)  # Convert lockout threshold to an integer
        except ValueError as e:
            logging.error("Invalid data - Lockout threshold is not a number [service]", exc_info=True)
            return f"Not Compliant - Lockout threshold should not exceed {required_lockout_threshold} attempts"
        except Exception as e:
            logging.error("Unexpected error in _analyze_lockout_threshold [service]", exc_info=True)
            return "Error analyzing lockout threshold"

        if lockout_threshold <= required_lockout_threshold:
            return "Compliant"
        else:
            return f"Not Compliant - Lockout threshold should not exceed {required_lockout_threshold} attempts"

    def _analyze_lockout_duration(self, duration):
        try:
            required_duration = int(self.settings.get('lockout_duration', 30))  # Use the setting, default to 30 if not set
            duration = int(duration)
        except ValueError as e:
            logging.error("Invalid data - Lockout duration or setting is not a number [service]", exc_info=True)
            return f"Not Compliant - Lockout duration should be at least {required_duration} minutes"
        except Exception as e:
            logging.error("Unexpected error in _analyze_lockout_duration [service]", exc_info=True)
            return "Error analyzing lockout duration"

        if duration >= required_duration:
            return "Compliant"
        else:
            return f"Not Compliant - Lockout duration should be at least {required_duration} minutes"

    def _analyze_lockout_obs_win(self, obs_win):
        try:
            required_obs_win = int(self.settings.get('lockout_obs_win', 30))  # Use the setting, default to 30 if not set
            obs_win = int(obs_win)
        except ValueError as e:
            logging.error("Invalid data - Lockout observation window or setting is not a number [service]", exc_info=True)
            return f"Not Compliant - Lockout observation window should be at least {required_obs_win} minutes"
        except Exception as e:
            logging.error("Unexpected error in _analyze_lockout_obs_win [service]", exc_info=True)
            return "Error analyzing lockout observation window"

        if obs_win >= required_obs_win:
            return "Compliant"
        else:
            return f"Not Compliant - Lockout observation window should be at least {required_obs_win} minutes"