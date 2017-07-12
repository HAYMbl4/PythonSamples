#!/usr/bin/env python3
import cgi
import json
from os.path import isfile

from resources.py import backup
from resources.py import email_service
from resources.py import visitor_service

VISITORS_FILE_PATH = "visitor/visitors.json"
VISITORS_BACKUP_FILE_PATH = "visitor/visitors_backup.json"
VISITORS_REQUEST_BACK_FILE_PATH = "visitor/visitors_request_backup.json"

form = cgi.FieldStorage()
will_go_array = form.getfirst("visitors")
new_visitors = json.loads(will_go_array)

has_visitors_file = True

if not isfile(VISITORS_FILE_PATH):
    has_visitors_file = backup.create_file(VISITORS_FILE_PATH, {"visitors": []})

created_backup = backup.create_backup(VISITORS_FILE_PATH, VISITORS_BACKUP_FILE_PATH)
created_request_backup = backup.create_request_backup(VISITORS_REQUEST_BACK_FILE_PATH, new_visitors)

if has_visitors_file and created_backup and created_request_backup:
    try:
        visitor_service.add_visitors(new_visitors, VISITORS_FILE_PATH)
        visitor_service.send_success_response(new_visitors)
        email_service.notify_about_new_visitors(new_visitors)
    except Exception as e:
        visitor_service.send_error_responce(e)
        email_service.notify_about_error(e)
else:
    visitor_service.send_error_responce("Не удалось сделать резевную копию данных")
