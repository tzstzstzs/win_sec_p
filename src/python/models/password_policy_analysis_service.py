import logging


class PasswordPolicyAnalysisService:
    def __init__(self, policy_data):
        self.policy_data = policy_data
        logging.info("PasswordPolicyAnalysisService initialized with policy data [service]")

    def analyze_password_policy(self):
        try:
            # Extract relevant policy values
            min_age = self._get_policy_value(2)  # Minimum password age (days)
            max_age = self._get_policy_value(3)  # Maximum password age (days)
            min_length = self._get_policy_value(4)  # Minimum password length
            history = self._get_policy_value(5)  # Length of password history maintained

            # Analyzing password policies based on specified rules
            results = {
                "password_length": self._analyze_length(min_length),
                "max_age": self._analyze_max_age(max_age),
                "min_age": self._analyze_min_age(min_age),
                "history": self._analyze_history(history)
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

    def _analyze_length(self, length):
        try:
            length = int(length)  # Convert length to an integer
        except ValueError as e:
            logging.error("Invalid data - Password length is not a number [service]", exc_info=True)
            return "Invalid data - Password length is not a number"
        except Exception as e:
            logging.error("Unexpected error in _analyze_length [service]", exc_info=True)
            return "Error analyzing password length"

        if length >= 8:
            return "Compliant"
        else:
            return "Not Compliant - Minimum password length should be at least 8 characters"

    def _analyze_max_age(self, age):
        try:
            age = int(age)  # Convert age to an integer
        except ValueError as e:
            logging.error("Invalid data - Password age is not a number [service]", exc_info=True)
            return "Invalid data - Password age is not a number"
        except Exception as e:
            logging.error("Unexpected error in _analyze_max_age [service]", exc_info=True)
            return "Error analyzing password max age"

        if age <= 30:
            return "Compliant"
        else:
            return "Not Compliant - Maximum password age should not exceed 30 days"

    def _analyze_min_age(self, age):
        try:
            age = int(age)  # Convert length to an integer
        except ValueError as e:
            logging.error("Invalid data - Password age is not a number [service]", exc_info=True)
            return "Invalid data - Password age is not a number"
        except Exception as e:
            logging.error("Unexpected error in _analyze_min_age [service]", exc_info=True)
            return "Error analyzing password max age"

        if age >= 1:
            return "Compliant"
        else:
            return "Not Compliant - Minimum password age should be at least 1 day"

    def _analyze_history(self, history):
        try:
            length = int(history)  # Convert history to an integer
        except ValueError as e:
            logging.error("Invalid data - Password history is not a number", exc_info=True)
            length = 0
        except Exception as e:
            logging.error("Unexpected error in _analyze_history", exc_info=True)
            return "Error analyzing password history"

        if length >= 12:
            return "Compliant"
        else:
            return "Not Compliant - Password history should be maintained for at least 12 months"

