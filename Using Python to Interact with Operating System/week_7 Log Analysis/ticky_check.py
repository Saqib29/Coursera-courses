#!/usr/bin/env python3
import operator
import re
from pprint import pprint
import csv

users = dict()
errors = dict()

with open('syslog.log', "r") as file:
  for lines in file:
    line = lines.strip()
    #print(line)
    if re.search(r"ERROR", line):
       part = re.search(r"ERROR ([\w ]*) ", line).group(0)[6:]
       errors[part] = errors.get(part, 0) + 1
    username = line[line.find('(')+1:-1]
    if username not in users:
      users[username] = [0,0]
    if re.search(r"INFO", line):
      users[username][0] += users.get(username[0], 0) + 1
    elif re.search(r"ERROR", line):
      users[username][1] += users.get(username[1], 0) + 1


error = sorted(errors.items(), key=operator.itemgetter(1))
pprint(error)
per_user = sorted(users.items(), key=operator.itemgetter(0))
pprint(per_user)

with open("error_messages.csv", "w") as file:
  file.write("Error,Count\n")
  for row in error:
    file.write("{},{}\n".format(row[0], row[1]))

with open("user_statistics.csv", "w") as file:
  file.write("Username,INFO,ERROR\n")
  for row in per_user:
    file.write("{},{},{}\n".format(row[0], row[1][0], row[1][1]))
