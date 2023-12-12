# src/python/services/installed_apps_service.py
import os
import subprocess
import json


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
        raise Exception(f"Subprocess execution failed: {e.stderr}")

    except json.JSONDecodeError as e:
        raise Exception(f"JSON decode error: {e}")
