import os
import subprocess
import json
import logging


def get_password_policy():
    script_path = os.path.join(os.path.dirname(__file__), '..', '..', 'powershell', 'get_password_policy.ps1')
    script_path = os.path.abspath(script_path)

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], capture_output=True,
                                text=True, encoding='utf-8')
        policy_data = json.loads(result.stdout)
        logging.info("Password policy data retrieved [service]")
        return policy_data
    except Exception as e:
        logging.error("Error retrieving password policy [service]", exc_info=True)
        raise
