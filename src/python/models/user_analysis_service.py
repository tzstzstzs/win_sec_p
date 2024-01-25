import logging

class UserAnalysisService:
    def __init__(self, user_data):
        self.user_data = user_data
        logging.info("UserListAnalysisService initialized with user data [service]")

    def analyze_users(self):
        vulnerabilities = []
        default_users = ["Alapértelmezett fiók", "Rendszergazda", "Vendég", "VDAGUtilityAccount", "test_project1"]

        for user in self.user_data:
            if user['Username'] in default_users and user['Enabled']:
                vulnerabilities.append(user['Username'])

        return vulnerabilities
