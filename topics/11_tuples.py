
# ============================================================
# DAY 11: PYTHON TUPLES
# ============================================================

# 1. Creating Tuples

# Empty tuple
empty_tuple = ()

# Tuple with multiple values
numbers = (10, 20, 30, 40, 50)

# Tuple without parentheses
colors = "Red", "Green", "Blue"

# Tuple with different data types
employee = (101, "Rahul", 45000.50, True)

print("Numbers:", numbers)
print("Colors:", colors)
print("Employee:", employee)


# 2. Single Element Tuple

# A comma is necessary for a single-element tuple
single_item = (10,)
not_a_tuple = (10)

print("\nSingle Item:", single_item)
print("Type:", type(single_item))
print("Without comma:", type(not_a_tuple))


# 3. Accessing Tuple Elements

sales = (1200, 1500, 1800, 2000, 2200)

print("\nFirst Sale:", sales[0])
print("Last Sale:", sales[-1])
print("Third Sale:", sales[2])


# 4. Tuple Slicing

print("\nFirst Three Sales:", sales[:3])
print("Last Two Sales:", sales[-2:])
print("Middle Sales:", sales[1:4])
print("Reversed Tuple:", sales[::-1])


# 5. Tuple Immutability

# Tuples cannot be modified after creation.

# The following operation will raise a TypeError:
# sales[0] = 5000

print("\nOriginal Sales:", sales)


# 6. Tuple Methods

values = (10, 20, 30, 20, 40, 20, 50)

# count() returns the number of occurrences
print("\nCount of 20:", values.count(20))

# index() returns the first occurrence position
print("Index of 30:", values.index(30))


# 7. Tuple Operations

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# Concatenation
combined = tuple1 + tuple2
print("\nCombined Tuple:", combined)

# Repetition
repeated = tuple1 * 2
print("Repeated Tuple:", repeated)

# Membership
print("Is 20 present?", 20 in tuple1)
print("Is 100 present?", 100 in tuple1)

# Length
print("Length:", len(combined))

# Minimum and Maximum
print("Minimum:", min(combined))
print("Maximum:", max(combined))

# Sum
print("Total:", sum(combined))


# 8. Tuple Unpacking

employee = (101, "Rahul", "Data Analyst", 50000)

emp_id, emp_name, designation, salary = employee

print("\nEmployee ID:", emp_id)
print("Employee Name:", emp_name)
print("Designation:", designation)
print("Salary:", salary)


# 9. Extended Unpacking

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("\nFirst:", first)
print("Middle:", middle)
print("Last:", last)


# 10. Converting Between List and Tuple

# List to Tuple
sales_list = [1000, 1500, 2000, 2500]
sales_tuple = tuple(sales_list)

print("\nTuple from List:", sales_tuple)

# Tuple to List
updated_sales = list(sales_tuple)
updated_sales.append(3000)

print("Updated List:", updated_sales)


# 11. Nested Tuples

employees = (
    (101, "Rahul", 45000),
    (102, "Priya", 55000),
    (103, "Amit", 50000)
)

print("\nFirst Employee:", employees[0])
print("Second Employee Name:", employees[1][1])
print("Third Employee Salary:", employees[2][2])


# 12. Looping Through a Tuple

departments = ("Sales", "Marketing", "Finance", "HR")

print("\nDepartments:")

for department in departments:
    print(department)


# 13. Practical Data Analytics Example

# Monthly sales data (January to June)
monthly_sales = (12000, 15000, 18000, 14000, 22000, 25000)

total_sales = sum(monthly_sales)
average_sales = total_sales / len(monthly_sales)
highest_sales = max(monthly_sales)
lowest_sales = min(monthly_sales)

print("\n--- Monthly Sales Analysis ---")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)

# Identify months where sales exceeded 18000
print("\nMonths with Sales Above 18000:")

for month, sale in enumerate(monthly_sales, start=1):
    if sale > 18000:
        print(f"Month {month}: {sale}")


# ============================================================
# END OF DAY 11
# ============================================================
