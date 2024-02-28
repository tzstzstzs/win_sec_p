import os.path
import subprocess
import json
import logging


def get_installed_updates_with_powershell():
    # Read the PowerShell script content from the file
    current_dir = os.path.dirname(__file__)
    get_updates_ps_script_path = os.path.join(current_dir, '../..', '..', 'powershell', 'get_installed_updates.ps1')
    get_updates_ps_script_path = os.path.abspath(get_updates_ps_script_path)

    with open(get_updates_ps_script_path, 'r') as script_file:
        script_content = script_file.read()

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", script_content], capture_output=True, text=True, encoding='utf-8', errors='ignore')

        if result.returncode != 0:
            logging.error(f"PowerShell script execution failed [service]: {result.stderr}")
            raise Exception(f"PowerShell script execution failed: {result.stderr}")

        updates_data = json.loads(result.stdout)

        # If the data is a dictionary (single update), convert it to a list
        if isinstance(updates_data, dict):
            updates_data = [updates_data]

        logging.info("Update data retrieved [service]")

        return updates_data

    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error [service]: {e}")
        raise
    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess error [service]: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error [service]: {e}")
        raise

# if __name__ == "__main__":
#     try:
#         # Test the get_installed_updates_with_powershell function
#         updates = get_installed_updates_with_powershell()
#         print("Retrieved installed updates:")
#         for update in updates:
#             print(update)
#     except Exception as e:
#         print("An error occurred:", e)