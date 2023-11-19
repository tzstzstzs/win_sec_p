import psutil

def get_running_processes_with_psutil():
    processes_data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        processes_data.append({
            'Name': proc.info['name'],
            'Id': proc.info['pid'],
            'CPU': proc.info['cpu_percent'],
            'WorkingSet': proc.info['memory_info'].rss  # This is in bytes
        })
    return processes_data
