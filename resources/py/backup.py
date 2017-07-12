import json
from os.path import isfile

from resources.py import log
from resources.py.email_service import notify_about_error


def create_file(name, content):
    try:
        with open(name, "w") as file:
            json.dump(content, file)
            log.info("Создан файл: '%s'" % name)
            return True
    except Exception as e:
        log.error("Не удалось создать файл: '%s'.\n Ex: %s" % (name, str(e)))
        notify_about_error(e)
        return False


def create_backup(file_name, backup_file):
    try:
        with open(file_name, "r") as file:
            file_content = json.load(file)
        with open(backup_file, "w") as backup_file:
            json.dump(file_content, backup_file)
            log.info("Создан бэкап для файла: '%s'" % file_name)
            return True
    except Exception as e:
        log.error("Не удалось создать бэкап для файла: '%s'.\n Ex: %s" % (file_name, str(e)))
        notify_about_error(e)
        return False


def create_request_backup(backup_file, request):
    try:
        if not isfile(backup_file):
            create_file(backup_file, request)
            return True
        else:
            with open(backup_file, "a") as request_backup_file:
                json.dump(request, request_backup_file)
                log.info("Создан бэкап для request: \n '%s'" % request)
                return True
    except Exception as e:
        log.error("Не удалось создать бэкап для request: \n '%s'.\n Ex: %s" % (request, str(e)))
        notify_about_error(e)
        return False
