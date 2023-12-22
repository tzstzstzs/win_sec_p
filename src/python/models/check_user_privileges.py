import ctypes
import logging

logging.basicConfig(level=logging.ERROR, filename='admin_check.log')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error("Failed to check admin status: %s", str(e))
        return False
