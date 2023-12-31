import ctypes
import logging


def is_admin():
    try:
        logging.info("Successfully checked admin status [service].")
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error("Failed to check admin status: %s", str(e))
        return False
