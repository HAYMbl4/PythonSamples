#!/usr/bin/env python3
import cgi
import html
import json

form = cgi.FieldStorage()
name_for_wish = form.getfirst("name-for-wish", "empty")
wish = form.getfirst("wish", "empty")

name_for_wish = html.escape(name_for_wish)
wish = html.escape(wish)

with open("wish/wishes.json", "r") as old_wishes_file:
    old_wishes = json.load(old_wishes_file)

with open("wish/wishes.json", "w") as new_wishes_file:
    try:
        old_wishes["wishes"].append({"name": name_for_wish, "wish": wish})
        json.dump(old_wishes, new_wishes_file)
    except Exception:
        print("can not write to file")
        json.dump(old_wishes, new_wishes_file)
