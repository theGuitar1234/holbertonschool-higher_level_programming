#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    csv_file = "data.csv"
    success = convert_csv_to_json(csv_file)
    if success:
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert data from {csv_file}")
