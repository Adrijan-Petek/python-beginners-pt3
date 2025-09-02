# csv_example.py

"""
📊 Tutorial 3: Working with CSV Files in Python
This script shows beginners how to read and write CSV (Comma-Separated Values) files.
"""

import csv

# Step 1: Write a CSV file
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])  # header
    writer.writerow(["Alice", 14, "A"])
    writer.writerow(["Bob", 15, "B"])
    writer.writerow(["Charlie", 13, "A"])

print("✅ students.csv created!")

# Step 2: Append more rows
with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["David", 16, "C"])
    writer.writerow(["Eva", 14, "B"])

print("➕ Added more students to students.csv")

# Step 3: Read and display CSV content
print("\n📂 Contents of students.csv:")
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Step 4 (Optional): Load into list of dictionaries
print("\n🔎 Reading as dictionaries:")
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and got grade {row['Grade']}.")
