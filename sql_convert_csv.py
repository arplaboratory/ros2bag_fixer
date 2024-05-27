import argparse
import sqlite3
import csv
import re
import os

def extract_table_names(sql_script):
    # Regular expression to find CREATE TABLE statements
    create_table_pattern = re.compile(r'CREATE TABLE IF NOT EXISTS\s+"?(\w+)"?', re.IGNORECASE)
    table_names = create_table_pattern.findall(sql_script)
    return table_names

def convert_sql_to_csv(sql_file_path, csv_file_path):
    # Establish a connection to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Read the SQL file
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute the entire SQL script
    cursor.executescript(sql_script)

    # Extract table names
    table_names = extract_table_names(sql_script)
    if not table_names:
        print("No tables found in the SQL script.")
        return

    for table_name in table_names:
        # Retrieve the data from the table
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()

        # Get column names
        column_names = [description[0] for description in cursor.description]

        # Write data to CSV
        csv_file_table_path = f"{csv_file_path.rsplit('.', 1)[0]}_{table_name}.csv"
        with open(csv_file_table_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write header
            csv_writer.writerow(column_names)
            # Write data rows
            csv_writer.writerows(rows)

        print(f"Data from table '{table_name}' has been successfully written to {csv_file_table_path}")

    # Close the database connection
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Convert SQL file to CSV')
    parser.add_argument('--input', required=True, help='Path to the input SQL file')
    parser.add_argument('--output', required=True, help='Base path for the output CSV file(s)')

    args = parser.parse_args()

    # Check if the SQL file exists
    if not os.path.isfile(args.input):
        print(f"Error: SQL file '{args.input}' does not exist.")
        return

    # Run the conversion
    convert_sql_to_csv(args.input, args.output)

if __name__ == '__main__':
    main()

