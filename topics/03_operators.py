
# Day 3: Python Operators
# Operators perform operations on variables and values.


# 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. Comparison Operators
x = 10
y = 5

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# 3. Logical Operators
age = 25
has_license = True

print("AND:", age >= 18 and has_license)
print("OR:", age >= 18 or has_license)
print("NOT:", not has_license)


# 4. Assignment Operators
number = 10

number += 5
print("After +=:", number)

number -= 3
print("After -=:", number)

number *= 2
print("After *=:", number)

number /= 4
print("After /=:", number)


# 5. Membership Operators
languages = ["Python", "SQL", "Excel"]

print("Python exists:", "Python" in languages)
print("Java does not exist:", "Java" not in languages)


# 6. Identity Operators
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("list_a is list_b:", list_a is list_b)
print("list_a is list_c:", list_a is list_c)
print("list_a == list_c:", list_a == list_c)


# 7. Bitwise Operators
p = 5   # Binary: 0101
q = 3   # Binary: 0011

print("Bitwise AND:", p & q)
print("Bitwise OR:", p | q)
print("Bitwise XOR:", p ^ q)
print("Left Shift:", p << 1)
print("Right Shift:", p >> 1)


# Arithmetic operators
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Comparison and logical operators
print(a > b, a == b)
print(a > 5 and b < 5)
print(a < 5 or b < 5)
print(not (a > b))

# Assignment operators
counter = 5
counter += 2
print(counter)

# Identity compares object identity; == compares values.
first = [1, 2]
second = [1, 2]
third = first
print(first == second, first is second, first is third)

# Membership and bitwise operators
print(2 in first, 9 not in first)
print("5 & 3 =", 5 & 3)  # 0101 & 0011 = 0001
print("5 & 8 =", 5 & 8)  # 0101 & 1000 = 0000
