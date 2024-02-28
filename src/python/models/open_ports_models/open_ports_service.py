import subprocess
import json
import os
import logging


def get_active_ports_with_powershell():
    current_dir = os.path.dirname(__file__)
    script_path = os.path.join(current_dir, '../..', '..', 'powershell', 'get_active_ports.ps1')

    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
                                capture_output=True, text=True)
        ports_data = json.loads(result.stdout)

        # Handle single object result
        if isinstance(ports_data, dict):
            ports_data = [ports_data]

        # Convert port numbers to integers
        for port in ports_data:
            if 'LocalPort' in port:  # Assuming 'LocalPort' is a key in the dictionaries
                port['LocalPort'] = int(port['LocalPort'])
            if 'RemotePort' in port:  # Assuming 'RemotePort' is a key in the dictionaries
                port['RemotePort'] = int(port['RemotePort'])

        logging.info("Ports data retrieved [service]    ")
        return ports_data

    except json.JSONDecodeError as e:
        logging.error("JSON decoding failed [service]", exc_info=True)
        raise Exception(f"Failed to parse ports data: {e}")
    except subprocess.CalledProcessError as e:
        logging.error("PowerShell script execution failed [service]", exc_info=True)
        raise Exception(f"PowerShell script execution error: {e.stderr}")
    except Exception as e:
        logging.error("Unexpected error occurred [service]", exc_info=True)
        raise Exception(f"Unexpected error: {e}")
