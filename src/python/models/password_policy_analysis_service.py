import logging
# from password_policy_service import get_password_policy


class PasswordPolicyAnalysisService:
    def __init__(self, policy_data):
        self.policy_data = policy_data

    def analyze_password_policy(self):
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

        print(results)
        return results

    def _get_policy_value(self, index):
        for policy in self.policy_data:
            if policy["Index"] == index:
                return policy["Value"]
        return None

    def _analyze_length(self, length):
        try:
            length = int(length)  # Convert length to an integer
        except ValueError:
            return "Invalid data - Password length is not a number"

        if length >= 8:
            return "Compliant"
        else:
            return "Not Compliant - Minimum password length should be at least 8 characters"

    def _analyze_max_age(self, age):
        try:
            age = int(age)  # Convert length to an integer
        except ValueError:
            return "Invalid data - Password age is not a number"

        if age <= 30:
            return "Compliant"
        else:
            return "Not Compliant - Maximum password age should not exceed 30 days"

    def _analyze_min_age(self, age):
        try:
            age = int(age)  # Convert length to an integer
        except ValueError:
            return "Invalid data - Password age is not a number"

        if age >= 1:
            return "Compliant"
        else:
            return "Not Compliant - Minimum password age should be at least 1 day"

    def _analyze_history(self, history):
        try:
            length = int(history)  # Convert length to an integer
        except ValueError:
            return "Invalid data - Password history length is not a number"

        if history >= 12:
            return "Compliant"
        else:
            return "Not Compliant - Password history should be maintained for at least 12 months"
