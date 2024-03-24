import os.path
import subprocess
import json
import logging
import locale


def get_windows_users_with_powershell():
    current_dir = os.path.dirname(__file__)
    get_users_ps_script_path = os.path.join(current_dir, '../..', '..', 'powershell', 'get_users.ps1')
    get_users_ps_script_path = os.path.abspath(get_users_ps_script_path)

    with open(get_users_ps_script_path, 'r') as script_file:
        script_content = script_file.read()

    try:
        locale.getpreferredencoding(False)
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", script_content],
                                capture_output=True, text=True, encoding='utf-8', errors='ignore')

        if result.returncode != 0:
            logging.error(f"PowerShell script execution failed [service]: {result.stderr}")
            raise Exception(f"PowerShell script execution failed: {result.stderr}")

        users_data = json.loads(result.stdout)

        # If the data is a dictionary (single user), convert it to a list
        if isinstance(users_data, dict):
            users_data = [users_data]

        logging.info("User data retrieved [service]")

        return users_data

    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error [service]: {e}")
        raise
    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess error [service]: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error [service]: {e}")
        raise