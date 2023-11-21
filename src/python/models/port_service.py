import socket


def is_port_open(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # Timeout for the operation
            result = sock.connect_ex((host, port))
            return result == 0  # Returns True if port is open, False otherwise
    except socket.error as e:
        print(f"Socket error: {e}")
        return False


def scan_open_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports


def run_port_scan(host, start_port, end_port, update_callback, complete_callback, error_callback):
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            if is_port_open(host, port):
                open_ports.append(port)
            update_callback(port - start_port + 1)
        complete_callback(open_ports)
    except Exception as e:
        error_callback(e)
