#!/usr/bin/env python3

import sys
import subprocess

old_substring = "jane"
new_substring = "jdoe"

file = sys.argv[1]
with open(file, "r") as f:
  for line in f:
     subprocess.run(['mv', 'line.strip()', 'line.strip().replace(old_subpstring, new_substring)'])
     print("old_path: ",line.strip())
     print("new_path: ",line.strip().replace(old_substring, new_substring))
