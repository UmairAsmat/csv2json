import os
import csv
import json
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

INDENT = config.get('indent', 4)
SORT_KEYS = config.get('sort_keys', True)
ORIENT = config.get('orient', 'records')

INPUT_DIR = 'csv_files'
OUTPUT_DIR = 'json_output'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process each CSV file in the input directory
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith('.csv'):
        csv_path = os.path.join(INPUT_DIR, filename)
        json_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '.json')
        with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            if ORIENT == 'columns':
                # Convert to dict of columns
                if rows:
                    columns = {key: [row[key] for row in rows] for key in rows[0].keys()}
                    data = columns
                else:
                    data = {}
            else:
                # Default: list of records
                data = rows
        with open(json_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=INDENT, sort_keys=SORT_KEYS, ensure_ascii=False)
        print(f'Converted {csv_path} -> {json_path}')
