#!/usr/bin/env python3
import cgi
import html
import json

form = cgi.FieldStorage()
name_for_wish = form.getfirst("name-for-wish", "empty")
wish = form.getfirst("wish", "empty")

first_field = html.escape(name_for_wish)
second_field = html.escape(wish)

f = open("resources/wishes.txt", "a")
f.write("%s : %s\n" % (first_field, second_field))
f.close()
