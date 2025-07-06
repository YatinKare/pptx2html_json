#!/bin/bash

echo "Line counts for files (excluding __init__.py and __pycache/):"

find . -maxdepth 1 -type f ! -name '__init__.py' -exec wc -l {} \; \
  | awk '{print $2 ": " $1}'

# Optionally count recursively, excluding __pycache__ and __init__.py
# Uncomment below for recursive search:
# find . -type f ! -path "*/__pycache__/*" ! -name '__init__.py' -exec wc -l {} \; \
#   | awk '{print $2 ": " $1}'

