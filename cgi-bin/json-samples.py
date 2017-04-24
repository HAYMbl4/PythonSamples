import json
from pprint import pprint

with open("..\wishes.json", "r") as old_wishes_file:
    old_wishes = json.load(old_wishes_file)

with open("..\wishes.json", "w") as new_wishes_file:
    try:
        old_wishes["wishes"].append({"name": "test", "wish": "test"})
        json.dump(old_wishes, new_wishes_file)
    except Exception:
        print("can not write to file")
        json.dump(old_wishes, new_wishes_file)

pprint(old_wishes["wishes"])
