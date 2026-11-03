
# ============================================================
# DAY 13: PYTHON DICTIONARIES
# ============================================================

# 1. Creating Dictionaries

# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs
employee = {
    "emp_id": 101,
    "name": "Rahul",
    "department": "Analytics",
    "salary": 50000
}

print("Employee:", employee)
print("Empty Dictionary:", empty_dict)


# 2. Accessing Dictionary Values

print("\nEmployee Name:", employee["name"])
print("Employee Salary:", employee["salary"])

# get() returns None if the key is missing
print("Employee City:", employee.get("city"))

# get() can also return a custom default value
print("City with Default:", employee.get("city", "Not Available"))

# Accessing a missing key with [] raises KeyError
# print(employee["city"])


# 3. Adding and Updating Values

employee["city"] = "Pune"           # Add new key
employee["salary"] = 55000           # Update existing value

employee.update({
    "department": "Data Analytics",
    "experience": 2
})

print("\nUpdated Employee:", employee)


# 4. Removing Dictionary Elements

employee_copy = employee.copy()

# pop() removes a specified key and returns its value
removed_salary = employee_copy.pop("salary")

print("\nRemoved Salary:", removed_salary)
print("After pop():", employee_copy)

# popitem() removes the last inserted key-value pair
removed_item = employee_copy.popitem()

print("Removed Item:", removed_item)

# del removes a specified key
del employee_copy["city"]

print("After del:", employee_copy)

# clear() removes all elements
employee_copy.clear()

print("After clear():", employee_copy)


# 5. Dictionary Methods

student = {
    "name": "Priya",
    "age": 22,
    "course": "Data Science"
}

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Number of Items:", len(student))


# 6. Looping Through a Dictionary

sales = {
    "January": 12000,
    "February": 15000,
    "March": 18000
}

# Loop through keys
print("\nSales Months:")

for month in sales:
    print(month)

# Loop through values
print("\nSales Values:")

for amount in sales.values():
    print(amount)

# Loop through key-value pairs
print("\nMonthly Sales:")

for month, amount in sales.items():
    print(f"{month}: {amount}")


# 7. Checking Key Existence

employee = {
    "name": "Amit",
    "department": "Finance"
}

if "department" in employee:
    print("\nDepartment:", employee["department"])

if "salary" not in employee:
    print("Salary information is unavailable")


# 8. Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]

# Create a dictionary of number and square
squares = {number: number ** 2 for number in numbers}

print("\nSquares:", squares)

# Create a dictionary of even numbers and their squares
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("Even Squares:", even_squares)


# 9. Nested Dictionaries

employees = {
    101: {
        "name": "Rahul",
        "department": "Analytics",
        "salary": 50000
    },
    102: {
        "name": "Priya",
        "department": "Marketing",
        "salary": 60000
    },
    103: {
        "name": "Amit",
        "department": "Finance",
        "salary": 55000
    }
}

print("\nFirst Employee:", employees[101])
print("Second Employee Name:", employees[102]["name"])
print("Third Employee Salary:", employees[103]["salary"])


# 10. Looping Through Nested Dictionaries

print("\nEmployee Details:")

for emp_id, details in employees.items():
    print(
        f"ID: {emp_id}, "
        f"Name: {details['name']}, "
        f"Department: {details['department']}, "
        f"Salary: {details['salary']}"
    )


# 11. Practical Data Analytics Example

# Employee salary analysis

total_salary = 0
employee_count = len(employees)

for details in employees.values():
    total_salary += details["salary"]

average_salary = total_salary / employee_count

print("\n--- Employee Salary Analysis ---")
print("Total Salary:", total_salary)
print("Average Salary:", average_salary)

# Find employees earning above average salary
print("\nEmployees Earning Above Average:")

for emp_id, details in employees.items():
    if details["salary"] > average_salary:
        print(details["name"], details["salary"])


# 12. Department-wise Employee Count

department_count = {}

for details in employees.values():
    department = details["department"]

    if department in department_count:
        department_count[department] += 1
    else:
        department_count[department] = 1

print("\nDepartment-wise Employee Count:")

for department, count in department_count.items():
    print(f"{department}: {count}")


# ============================================================
# END OF DAY 13
# ============================================================
