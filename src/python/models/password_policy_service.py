import os
import subprocess
import json
import logging


# Mapping function to pair index with policy description
def map_policy_data(policy_data):
    policy_map = {
        1: "Force user logoff how long after time expires?",
        2: "Minimum password age (days)",
        3: "Maximum password age (days)",
        4: "Minimum password length",
        5: "Length of password history maintained",
        6: "Lockout threshold",
        7: "Lockout duration (minutes)",
        8: "Lockout observation window (minutes)",
        9: "Computer role"
    }
    return [{"Index": item['Index'], "Policy": policy_map.get(item['Index'], f"Policy {item['Index']}"), "Value": item['Value']} for item in policy_data]


def get_password_policy():
    script_path = os.path.join(os.path.dirname(__file__), '..', '..', 'powershell', 'get_password_policy.ps1')
    script_path = os.path.abspath(script_path)

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], capture_output=True,
                                text=True, encoding='utf-8')
        policy_data = json.loads(result.stdout)
        mapped_data = map_policy_data(policy_data)
        logging.info("Password policy data retrieved and mapped [service]")
        return mapped_data
    except Exception as e:
        logging.error("Error retrieving password policy [service]", exc_info=True)
        raise
