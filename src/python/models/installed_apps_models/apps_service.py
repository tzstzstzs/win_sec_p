# src/python/services/apps_service.py
import os
import subprocess
import json
import logging


def get_installed_apps():
    current_dir = os.path.dirname(__file__)
    get_apps_ps_script_path = os.path.join(current_dir, '../..', '..', 'powershell', 'get_installed_apps.ps1')
    get_apps_ps_script_path = os.path.abspath(get_apps_ps_script_path)

    with open(get_apps_ps_script_path, 'r') as script_file:
        script_content = script_file.read()

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", script_content],
                                capture_output=True, text=True, check=True, encoding='utf-8')

        if result.stderr:
            raise Exception(f"PowerShell script execution error: {result.stderr}")

        apps_data = json.loads(result.stdout)
        logging.info("Installed apps data retrieved [service]")
        return apps_data

    except subprocess.CalledProcessError as e:
        logging.error("PowerShell execution failed [service]", exc_info=True)
        raise Exception(f"Subprocess execution failed with error: {e.stderr}")
    except json.JSONDecodeError as e:
        logging.error("JSON decoding failed [service]", exc_info=True)
        raise Exception(f"Failed to parse apps data: {e}")
    except Exception as e:
        logging.error("Unexpected error occurred in get_installed_apps [service]", exc_info=True)
        raise Exception(f"Unexpected error: {e}")
