import csv

# Define the filename with a leading space
file_path = r"C:\Users\simon guo\Downloads\TestFiles\  mydata.csv"  # Leading space before "mydata.csv"

# Data to be written to the CSV file
data = [
    ['PostalCode', 'Count'],  # Header row
    ['A1A1A1', 100],
    ['B2B2B2', 75],
    ['C3C3C3', 50],
    ['D4D4D4', 200]
]

# Write data to the CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_path}' created successfully.")