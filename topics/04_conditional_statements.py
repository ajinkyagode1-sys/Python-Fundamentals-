
# Day 4: Conditional Statements
# Conditional statements execute code based on conditions.


# 1. Simple if Statement
age = 20

if age >= 18:
    print("You are eligible to vote.")


# 2. if-else Statement
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 3. if-elif-else Statement
marks = 76

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


# 4. Multiple Conditions Using Logical Operators
age = 24
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")


# 5. Nested if Statement
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")


# 6. Checking Positive, Negative, or Zero
number = -5

if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")


# 7. Practical Example: Discount Eligibility
purchase_amount = 2500

if purchase_amount >= 5000:
    discount = 0.20
elif purchase_amount >= 2000:
    discount = 0.10
else:
    discount = 0

discount_amount = purchase_amount * discount
final_amount = purchase_amount - discount_amount

print("Purchase Amount:", purchase_amount)
print("Discount:", discount_amount)
print("Final Amount:", final_amount)

# if / elif / else and nested conditions

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

marks = float(input("Enter marks out of 100: "))
if not 0 <= marks <= 100:
    print("Marks must be between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

number = int(input("Enter an integer: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
if number != 0:
    print("Even" if number % 2 == 0 else "Odd")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
