# CSV to JSON Converter

This script converts all CSV files in the `csv_files` directory to JSON format in the `json_output` directory, using options specified in `config.yaml`.

## Features
- Batch converts all CSVs in a folder
- Configurable JSON output style (indentation, key sorting, orientation)
- Outputs JSON files with the same base name as the CSVs

## Usage
1. Place your CSV files in the `csv_files` directory.
2. Configure your desired JSON output style in `config.yaml` (see below).
3. Run the script:
   ```bash
   python csv_to_json.py
   ```
4. Find the resulting JSON files in the `json_output` directory.

## Configuration (`config.yaml`)
- `indent`: Number of spaces for JSON indentation (default: 4)
- `sort_keys`: Whether to sort keys in JSON output (default: true)
- `orient`: Output orientation, either `records` (list of dicts) or `columns` (dict of columns)

Example:
```yaml
indent: 4
sort_keys: true
orient: records
```

## Requirements
Install dependencies with:
```bash
pip install -r requirements.txt
```

## License
MIT #   c s v 2 j s o n  
 