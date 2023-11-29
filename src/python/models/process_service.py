import psutil


def get_running_processes_with_psutil():
    processes_data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            parent_pid = proc.ppid()  # Get parent process ID
            parent_name = psutil.Process(parent_pid).name() if parent_pid != 0 else 'None'  # Get parent process name
            processes_data.append({
                'Name': proc.info['name'],
                'Id': proc.info['pid'],
                'CPU': proc.info['cpu_percent'],
                'WorkingSet': proc.info['memory_info'].rss,  # This is in bytes
                'Parent': f"{parent_name} ({parent_pid})" if parent_pid != 0 else "None"  # Parent process info
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle any exceptions that might occur due to inaccessible process information
            pass

    print(processes_data)
    return processes_data
