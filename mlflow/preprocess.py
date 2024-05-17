import json
import csv
import sys

def json_to_csv(json_file_path, csv_file_path):
    # Load JSON data
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Extract the metadata and time series data
    meta_data = data.get('Meta Data', {})
    time_series_data = data.get('Time Series (5min)', {})

    # Open CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write metadata
        writer.writerow(['Meta Data'])
        for key, value in meta_data.items():
            writer.writerow([key, value])
        
        # Write a blank row between metadata and time series data
        writer.writerow([])

        # Write time series data
        writer.writerow(['Time Series (5min)'])
        headers = ['timestamp'] + list(next(iter(time_series_data.values())).keys())
        writer.writerow(headers)
        
        for timestamp, values in time_series_data.items():
            row = [timestamp] + list(values.values())
            writer.writerow(row)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_json_file> <output_csv_file>")
        sys.exit(1)

    input_json_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    json_to_csv(input_json_file, output_csv_file)
