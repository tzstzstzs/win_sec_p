import logging

class UserAnalysisService:
    def __init__(self, user_data, settings):
        self.user_data = user_data
        self.settings = settings
        logging.info("UserListAnalysisService initialized with user data [service]")

    def analyze_users(self):
        vulnerabilities = []
        # default_users = ["Alapértelmezett fiók", "Rendszergazda", "Vendég", "VDAGUtilityAccount", "test_project1"]
        print(self.settings)
        for user in self.user_data:
            if user['Username'] in self.settings and user['Enabled']:
                vulnerabilities.append(user['Username'])

        return vulnerabilities
