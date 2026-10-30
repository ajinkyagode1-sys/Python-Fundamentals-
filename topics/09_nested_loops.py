
# Day 9: Python Nested Loops
# A nested loop is a loop inside another loop.


# 1. Basic Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, "j =", j)


# 2. Nested Loop with Rows and Columns
for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()


# 3. Right-Angled Triangle Pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 4. Number Pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 5. Multiplication Tables
for i in range(2, 4):
    print("Multiplication Table:", i)

    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")

    print()


# 6. Nested while Loop
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(f"i = {i}, j = {j}")
        j += 1

    i += 1


# 7. break in Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i = {i}, j = {j}")


# 8. Practical Example: Sales by Region
sales_data = [
    [1200, 1500, 1800],
    [1000, 1300, 1600],
    [1400, 1700, 2000]
]

for region_index, region_sales in enumerate(sales_data, start=1):
    total = 0

    for sale in region_sales:
        total += sale

    print(f"Region {region_index} Total Sales: {total}")


# 9. Find a Value in a Nested List
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50
found = False

for row in numbers:
    for number in row:
        if number == target:
            found = True
            break

    if found:
        break

if found:
    print("Target found:", target)
else:
    print("Target not found.")


# Nested loops and a basic prime-number example.

for row in range(1, 4):
    for column in range(1, 4):
        print(f"row={row}, column={column}")

for number in range(2, 11):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is prime")
