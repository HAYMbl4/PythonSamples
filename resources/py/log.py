from datetime import datetime
from os.path import isfile

LOG_FILE_PATH = "trace.log"


def create_file_if_does_not_exist():
    if not isfile(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, "w", -1, "UTF-8") as file:
            log_message = "%s INFO: %s \n" % (datetime.now().strftime("%Y-%m-%d %H:%M"), "Log created")
            file.write(log_message)


def info(message):
    create_file_if_does_not_exist()
    with open(LOG_FILE_PATH, "a", -1, "UTF-8") as log_file:
        log_message = "%s INFO: %s \n" % (datetime.now().strftime("%Y-%m-%d %H:%M"), message)
        log_file.write(log_message)


def error(message):
    create_file_if_does_not_exist()
    with open(LOG_FILE_PATH, "a", -1, "UTF-8") as log_file:
        log_message = "%s ERROR: %s \n" % (datetime.now().strftime("%Y-%m-%d %H:%M"), message)
        log_file.write(log_message)
