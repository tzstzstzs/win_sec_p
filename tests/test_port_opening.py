import socket
import threading
import unittest
from src.python.models.port_service import run_port_scan

server_running = threading.Event()
server_running.set()  # Initially, the server is marked as running


def start_test_server(port):
    def server_logic():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', port))
            server_socket.listen()
            while server_running.is_set():  # Keep running until signaled to stop
                server_socket.settimeout(1)  # Timeout to check for the stop signal
                try:
                    with server_socket.accept()[0]:
                        pass  # Connection handling logic here
                except socket.timeout:
                    continue  # Continue the loop if the accept call times out

    server_thread = threading.Thread(target=server_logic)
    server_thread.daemon = True
    server_thread.start()
    return server_thread


# Mock callback functions
def update_progress_mock(value):
    pass  # For a unit test, we don't need to update any progress bar


def complete_scan_mock(open_ports):
    global ports_found  # Use a global variable to store the results for assertion
    ports_found = open_ports


def error_scan_mock(error):
    raise error  # If there's an error, raise it so the test can catch it


ports_found = []


class PortOpeningTestCase(unittest.TestCase):
    server_thread = None
    test_port = None

    @classmethod
    def setUpClass(cls):
        cls.test_port = 8080
        cls.server_thread = start_test_server(cls.test_port)

    @classmethod
    def tearDownClass(cls):
        server_running.clear()  # Signal the server to stop
        cls.server_thread.join()  # Wait for the server thread to finish

    def test_port_opening(self):
        # Give the server a moment to start up
        threading.Event().wait(0.5)

        # Run the port scan
        run_port_scan('127.0.0.1', self.test_port, self.test_port,
                      update_progress_mock, complete_scan_mock, error_scan_mock)

        # Wait for the scanning thread to complete
        threading.Event().wait(1.0)

        # Check if the test port is in the list of open ports
        self.assertIn(self.test_port, ports_found, f"Port {self.test_port} should be open but is not detected.")


if __name__ == '__main__':
    unittest.main()
