# src/python/services/installed_apps_service.py
import os
import subprocess
import json
import logging

# Initialize logging
logging.basicConfig(level=logging.ERROR, filename='installed_apps_error.log')


def get_installed_apps():
    # Define the PowerShell script path
    current_dir = os.path.dirname(__file__)
    get_apps_ps_script_path = os.path.join(current_dir, '..', '..', 'powershell', 'get_installed_apps.ps1')
    get_apps_ps_script_path = os.path.abspath(get_apps_ps_script_path)

    # Read the PowerShell script content from the file
    with open(get_apps_ps_script_path, 'r') as script_file:
        script_content = script_file.read()

    try:
        # Execute the PowerShell script
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", script_content],
                                capture_output=True, text=True, check=True)

        # Check for errors
        if result.stderr:
            raise Exception(f"PowerShell script execution error: {result.stderr}")

        # Process the output
        apps_data = json.loads(result.stdout)
        return apps_data

    except subprocess.CalledProcessError as e:
        logging.error("PowerShell execution failed", exc_info=True)
        raise Exception(f"Subprocess execution failed with error: {e.stderr}")
    except json.JSONDecodeError as e:
        logging.error("JSON decoding failed", exc_info=True)
        raise Exception(f"Failed to parse apps data: {e}")
    except Exception as e:
        logging.error("Unexpected error occurred in get_installed_apps", exc_info=True)
        raise Exception(f"Unexpected error: {e}")
