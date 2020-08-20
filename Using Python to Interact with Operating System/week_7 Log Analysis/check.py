#!/usr/bin/env python3

import operator
import re
from pprint import pprint
import csv

user = {}
error = {}
with open("syslog.log", "r") as file:
  for lines in file:
    line = lines.strip()
    if "ERROR" in line:
      error[re.search(r"ERROR ([\w ]*) ",line).group(0)[6:]] = error.get(re.search(r"ERROR ([\w ]*) ",line).group(0)[6:], 0) + 1
    #username = line[line.find('(')+1:-1]
    #if username not in user:
    #   user[username] = [0,0]
    #if re.search(r"INFO", line):
    #  user[username][0] += user.get(username[0], 0) + 1
    #elif re.search("ERROR", line):
    #  user[username][1] += user.get(username[1], 0) + 1

pprint(error)
#users = sorted(user.items(), key=operator.itemgetter(0))
#pprint(users)

#with open("check.csv", "w") as file:
#  file.write("Username,INFO,ERROR\n")
#  for items in users:
#    file.write("{},{},{}\n".format(items[0], items[1][0], items[1][1]))

