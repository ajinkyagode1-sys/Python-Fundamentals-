
# Day 2: User Input
# Learn how to accept input from the user.

# 1. Basic user input
name = input("Enter your name: ")
print("Hello,", name)


# 2. Taking an integer input
age = int(input("Enter your age: "))
print("Your age is:", age)


# 3. Taking a float input
price = float(input("Enter the product price: "))
print("Product price:", price)


# 4. Taking multiple inputs
first_name = input("Enter your first name: ")
city = input("Enter your city: ")

print(f"My name is {first_name} and I live in {city}.")


# 5. Simple calculation using user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

total = num1 + num2
print("Sum:", total)

#---------------------------------------------------------------------------------------------------------------------------------

# input() returns a string; convert it before numeric calculations.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
print("Sum:", first_number + second_number)

subjects = ["Maths", "English", "Science", "History",
            "Geography", "Hindi", "Marathi", "Sanskrit"]
student_name = input("Student name: ")
marks = []

for subject in subjects:
    mark = float(input(f"Enter {subject} marks out of 100: "))
    if not 0 <= mark <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    marks.append(mark)

percentage = sum(marks) / (len(subjects) * 100) * 100
print(f"{student_name} scored {percentage:.2f}%.")

