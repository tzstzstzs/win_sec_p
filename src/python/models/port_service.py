import subprocess
import json
import os
import logging


def get_active_ports_with_powershell():
    current_dir = os.path.dirname(__file__)
    script_path = os.path.join(current_dir, '..', '..', 'powershell', 'get_active_ports.ps1')

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
                                capture_output=True, text=True)
        ports_data = json.loads(result.stdout)

        # Handle single object result
        if isinstance(ports_data, dict):
            ports_data = [ports_data]

        return ports_data

    except json.JSONDecodeError as e:
        logging.error("JSON decoding failed", exc_info=True)
        raise Exception(f"Failed to parse ports data: {e}")
    except subprocess.CalledProcessError as e:
        logging.error("PowerShell script execution failed", exc_info=True)
        raise Exception(f"PowerShell script execution error: {e.stderr}")
    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        raise Exception(f"Unexpected error: {e}")


# Initialize logging
logging.basicConfig(level=logging.ERROR, filename='active_ports_error.log')