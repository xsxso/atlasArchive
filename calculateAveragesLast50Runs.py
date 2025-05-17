import requests
import json
from pprint import pprint
from collections import defaultdict

# Load the JSON file and parse it into a Python structure
# Note: The JSON file should be in the same directory as this script
# or provide the full path to the file
# Example JSON file name
# json_file_name = "last50runs.json"
with open("last50runs.json", "r") as f:
    data = json.load(f)

# 	Sets up a dictionary that maps field names (e.g., "archiveQueryElapsedTimeMs") to a list of all values seen across documents.
# 	Iterates through the JSON data, collecting values for each field.
elapsed_fields = defaultdict(list)

# This function walks through any nested structure (dicts inside dicts, lists of dicts, etc.) and:
# Looks for any key containing the word "elapsed" (case-insensitive)
# Checks that the value is a number (int or float)
# Saves it under the key in the elapsed_fields dict
# It’s recursive, so it keeps drilling into nested structures.

def collect_elapsed_fields(obj):
    if isinstance(obj, dict):
        for key, val in obj.items():
            if "elapsed" in key.lower() and isinstance(val, (int, float)):
                elapsed_fields[key].append(val)
            collect_elapsed_fields(val)
    elif isinstance(obj, list):
        for item in obj:
            collect_elapsed_fields(item)

# Run collection on loaded JSON
collect_elapsed_fields(data)

# Compute and display averages
print("Average elapsed times per field:\n")
for key, values in elapsed_fields.items():
    avg = (sum(values) / len(values)/1000)
    print(f"{key}: {avg} s (based on {len(values)} samples)")