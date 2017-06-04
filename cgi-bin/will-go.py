#!/usr/bin/env python3
import cgi
import json

form = cgi.FieldStorage()
will_go_array = form.getfirst("will-go-array")
new_visitors = json.loads(will_go_array)

with open("visitors.json", "r") as old_visitors_file:
    old_visitors = json.load(old_visitors_file)

with open("visitors.json", "w") as new_visitors_file:
    for v in new_visitors:
        old_visitors["visitors"].append(v)
        json.dump(old_visitors, new_visitors_file)

result = {'success': 'true', 'message': 'The Command Completed Successfully'}
print('Content-Type: application/json\n\n')
print(json.dumps(old_visitors))
