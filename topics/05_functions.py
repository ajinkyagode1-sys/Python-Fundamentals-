
# Day 5: Python Functions
# Functions help us reuse code and organize programs.


# 1. Defining and Calling a Function
def greet():
    print("Hello! Welcome to Python.")


greet()


# 2. Function with Parameters
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Ajinkya")
greet_user("Rahul")


# 3. Function with Multiple Parameters
def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 20)
add_numbers(5, 15)


# 4. Function with a Return Value
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(250, 3)
print("Total Amount:", total)


# 5. Function with a Default Parameter
def calculate_discount(amount, discount_rate=0.10):
    discount = amount * discount_rate
    return discount


print("Default Discount:", calculate_discount(1000))
print("Custom Discount:", calculate_discount(1000, 0.20))


# 6. Returning Multiple Values
def calculate_stats(a, b):
    total = a + b
    difference = a - b
    return total, difference


result_sum, result_difference = calculate_stats(20, 8)

print("Sum:", result_sum)
print("Difference:", result_difference)


# 7. Practical Example: Sales Calculation
def calculate_revenue(units_sold, selling_price):
    revenue = units_sold * selling_price
    return revenue


product_revenue = calculate_revenue(50, 120)

print("Units Sold:", 50)
print("Selling Price:", 120)
print("Total Revenue:", product_revenue)

# Functions, parameters, return values, and pass.

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def future_feature():
    pass

greet("Ajinkya")
print("Sum:", add(10, 20))
print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))
