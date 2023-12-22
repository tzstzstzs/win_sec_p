# src/python/services/user_service.py
import os.path
import subprocess
import json


def get_windows_users_with_powershell():
    # TODO: ha nem lehet futtatni a ps file-t vagy commandot, akkor futtasson egy scriptet, amely átállítja a ps script futtatási beállításokat, majd a végén visszaállítja.

    # Read the PowerShell script content from the file
    current_dir = os.path.dirname(__file__)
    get_users_ps_script_path = os.path.join(current_dir, '..', '..', 'powershell', 'get_users.ps1')
    get_users_ps_script_path = os.path.abspath(get_users_ps_script_path)

    with open(get_users_ps_script_path, 'r') as script_file:
        script_content = script_file.read()
        print(script_content)

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", script_content],
                                capture_output=True, text=True, encoding='utf-8', errors='ignore')

        if result.returncode != 0:
            raise Exception(f"PowerShell script execution failed: {result.stderr}")

        users_data = json.loads(result.stdout)

        # If the data is a dictionary (single user), convert it to a list
        if isinstance(users_data, dict):
            users_data = [users_data]

        return users_data
    except json.JSONDecodeError as e:
        raise Exception(f"JSON decode error: {e}")
