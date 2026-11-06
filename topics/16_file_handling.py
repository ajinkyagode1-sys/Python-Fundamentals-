
# ============================================================
# DAY 16: PYTHON FILE HANDLING
# ============================================================

from pathlib import Path

# Create a folder for today's file handling examples.
# Files will be created inside this folder when the script runs.

folder = Path("day16_files")
folder.mkdir(exist_ok=True)


# ------------------------------------------------------------
# 1. Creating and Writing a File
# ------------------------------------------------------------

# "w" mode creates a file if it does not exist.
# If the file exists, its previous content is overwritten.

file_path = folder / "sample.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Python File Handling!\n")
    file.write("Learning Python is useful for Data Analytics.\n")

print("--- File Written ---")


# ------------------------------------------------------------
# 2. Reading a File
# ------------------------------------------------------------

# "r" mode opens a file for reading.

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print("\n--- File Content ---")
print(content)


# ------------------------------------------------------------
# 3. Reading One Line
# ------------------------------------------------------------

with open(file_path, "r", encoding="utf-8") as file:
    first_line = file.readline()

print("First Line:", first_line.strip())


# ------------------------------------------------------------
# 4. Reading All Lines
# ------------------------------------------------------------

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

print("\n--- All Lines ---")

for line in lines:
    print(line.strip())


# ------------------------------------------------------------
# 5. Appending Data to a File
# ------------------------------------------------------------

# "a" mode adds content at the end of the file.
# It does not overwrite existing content.

with open(file_path, "a", encoding="utf-8") as file:
    file.write("This line was added using append mode.\n")

print("\n--- Content Appended ---")


# Read the updated file
with open(file_path, "r", encoding="utf-8") as file:
    updated_content = file.read()

print(updated_content)


# ------------------------------------------------------------
# 6. Writing Multiple Lines
# ------------------------------------------------------------

# writelines() writes multiple strings.
# It does not automatically add newline characters.

multiple_lines = [
    "Python\n",
    "SQL\n",
    "Power BI\n",
    "Excel\n"
]

skills_file = folder / "skills.txt"

with open(skills_file, "w", encoding="utf-8") as file:
    file.writelines(multiple_lines)

print("--- Skills File Created ---")


# ------------------------------------------------------------
# 7. File Modes
# ------------------------------------------------------------

# "r"  -> Read
# "w"  -> Write; overwrites existing content
# "a"  -> Append
# "x"  -> Create a new file; raises an error if it exists
# "r+" -> Read and write
# "w+" -> Read and write; overwrites existing content
# "a+" -> Read and append


# Example of exclusive creation using "x"
new_file = folder / "new_file.txt"

if not new_file.exists():
    with open(new_file, "x", encoding="utf-8") as file:
        file.write("This file was created using x mode.\n")

print("\nNew file created:", new_file.name)


# ------------------------------------------------------------
# 8. Checking File Existence
# ------------------------------------------------------------

print("\nDoes sample.txt exist?", file_path.exists())
print("File Name:", file_path.name)
print("File Suffix:", file_path.suffix)
print("File Size:", file_path.stat().st_size, "bytes")


# ------------------------------------------------------------
# 9. Handling File Errors
# ------------------------------------------------------------

missing_file = folder / "missing.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("\nError: The requested file does not exist.")


# ------------------------------------------------------------
# 10. Using try-except with User Input
# ------------------------------------------------------------

# This example safely converts user input into a number.

try:
    amount = float(input("\nEnter sales amount: "))

    if amount >= 0:
        print("Sales Amount:", amount)
    else:
        print("Sales amount cannot be negative.")

except ValueError:
    print("Please enter a valid numeric amount.")


# ------------------------------------------------------------
# 11. Practical Data Analytics Example
# ------------------------------------------------------------

# Store daily sales data in a text file.

sales_data = [
    "12000\n",
    "15000\n",
    "18000\n",
    "14000\n",
    "22000\n"
]

sales_file = folder / "sales.txt"

with open(sales_file, "w", encoding="utf-8") as file:
    file.writelines(sales_data)

# Read sales data from the file
with open(sales_file, "r", encoding="utf-8") as file:
    sales = [float(line.strip()) for line in file]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sales = max(sales)
lowest_sales = min(sales)

print("\n--- Sales Analysis from File ---")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)


# ------------------------------------------------------------
# 12. Using Path to List Files
# ------------------------------------------------------------

print("\n--- Files in day16_files Folder ---")

for path in folder.iterdir():
    if path.is_file():
        print(path.name)


# ============================================================
# END OF DAY 16
# ============================================================
