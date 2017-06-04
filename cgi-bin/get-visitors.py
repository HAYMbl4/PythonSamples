import json

with open("visitor/visitors.json", "r") as visitors_file:
    visitors = json.load(visitors_file)

print('Content-Type: application/json\n\n')
print(json.dumps(visitors))
