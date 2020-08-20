#!/bin/bash

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for file in $files; do
  if test -e  ..$file; then echo pwd$file >> oldFiles.txt
  fi
done
