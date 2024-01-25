import os
import subprocess
import json
import logging

def custom_json_parser(obj):
    # Replace null with None or "N/A"
    return {k: (v if v is not None else "N/A") for k, v in obj.items()}

def get_running_processes():
    # Define the PowerShell script path
    current_dir = os.path.dirname(__file__)
    get_processes_ps_script_path = os.path.join(current_dir, '..', '..', 'powershell', 'get_process_info.ps1')
    get_processes_ps_script_path = os.path.abspath(get_processes_ps_script_path)

    # Read the PowerShell script content from the file
    with open(get_processes_ps_script_path, 'r') as script_file:
        script_content = script_file.read()

    try:
        # Execute the PowerShell script with UTF-8 encoding
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", script_content],
                                capture_output=True, text=True, check=True, encoding='utf-8')

        # Check for errors in stderr
        if result.stderr:
            raise Exception(f"PowerShell script execution error: {result.stderr}")

        # Check if stdout is empty
        if result.stdout:
            # Process the output
            processes_data = json.loads(result.stdout, object_hook=custom_json_parser)
            logging.info("Running processes data retrieved [service]")
            return processes_data
        else:
            logging.warning("No data received from PowerShell script")
            return None

    except subprocess.CalledProcessError as e:
        logging.error("PowerShell execution failed [service]", exc_info=True)
        raise Exception(f"Subprocess execution failed with error: {e.stderr}")
    except json.JSONDecodeError as e:
        logging.error("JSON decoding failed [service]", exc_info=True)
        raise Exception(f"Failed to parse process data: {e}")
    except TypeError as e:
        logging.error("TypeError in processing output [service]", exc_info=True)
        raise Exception(f"TypeError encountered: {e}")
    except Exception as e:
        logging.error("Unexpected error occurred in get_running_processes [service]", exc_info=True)
        raise Exception(f"Unexpected error: {e}")

