
# Day 8: Python Loops
# Loops help us execute a block of code repeatedly.


# 1. Basic for Loop
for number in range(1, 6):
    print(number)


# 2. Loop Through a List
languages = ["Python", "SQL", "Excel", "Power BI"]

for language in languages:
    print("Learning:", language)


# 3. Using range() with a Step
for number in range(2, 11, 2):
    print("Even number:", number)


# 4. Basic while Loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# 5. break Statement
for number in range(1, 10):
    if number == 5:
        break
    print("Number:", number)


# 6. continue Statement
for number in range(1, 6):
    if number == 3:
        continue
    print("Number:", number)


# 7. Loop else
for number in range(1, 4):
    print("Checking:", number)
else:
    print("Loop completed normally.")


# 8. Calculate the Sum of Numbers
total = 0

for number in range(1, 6):
    total += number

print("Total Sum:", total)


# 9. Calculate Total Sales
daily_sales = [1200, 1500, 900, 1800, 2100]
total_sales = 0

for sale in daily_sales:
    total_sales += sale

print("Total Sales:", total_sales)


# 10. Find a Target Value
sales = [500, 1200, 800, 2000, 1500]
target = 2000

for sale in sales:
    if sale == target:
        print("Target sale found:", sale)
        break
else:
    print("Target sale not found.")

# for / while, range, break, continue, and loop else.

for number in range(1, 6):
    print(number)

for number in range(2, 11, 2):
    print("Even:", number)

count = 1
while count <= 3:
    print("Count:", count)
    count += 1

for number in range(1, 6):
    if number == 3:
        continue
    print("Not skipped:", number)

for number in range(1, 10):
    if number == 5:
        break
    print("Before break:", number)

for number in range(3):
    print("Loop:", number)
else:
    print("Loop completed normally.")

while True:
    command = input("Type something (or 'exit' to stop): ")
    if command.strip().lower() == "exit":
        print("Goodbye!")
        break
    print("You typed:", command)
