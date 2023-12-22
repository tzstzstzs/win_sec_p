import subprocess
import json
import os

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
        raise Exception(f"JSON decode error: {e}")
    except Exception as e:
        raise Exception(f"PowerShell script execution error: {e}")

