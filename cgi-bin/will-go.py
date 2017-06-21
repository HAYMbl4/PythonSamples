#!/usr/bin/env python3
import cgi
import json
from os.path import isfile

from resources.py import backup

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
    with open(VISITORS_FILE_PATH, "r") as old_visitors_file:
        old_visitors = json.load(old_visitors_file)

    with open(VISITORS_FILE_PATH, "w") as new_visitors_file:
        for v in new_visitors:
            old_visitors["visitors"].append(v)
            json.dump(old_visitors, new_visitors_file)

    result = {'success': 'true', 'message': 'The Command Completed Successfully'}
    print('Content-Type: application/json\n\n')
    print(json.dumps(old_visitors))
