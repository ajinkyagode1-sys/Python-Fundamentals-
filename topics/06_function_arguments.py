
# Day 6: Function Arguments
# Learn different ways to pass arguments to functions.


# 1. Positional Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Ajinkya", 22)


# 2. Keyword Arguments
def display_employee(name, department):
    print(f"Employee: {name}")
    print(f"Department: {department}")


display_employee(name="Rahul", department="Analytics")
display_employee(department="Finance", name="Priya")


# 3. Default Arguments
def calculate_price(price, tax_rate=0.18):
    return price + (price * tax_rate)


print("Price with default tax:", calculate_price(1000))
print("Price with custom tax:", calculate_price(1000, 0.05))


# 4. Variable-Length Positional Arguments (*args)
def calculate_total(*numbers):
    return sum(numbers)


print("Total:", calculate_total(10, 20))
print("Total:", calculate_total(10, 20, 30, 40))


# 5. Variable-Length Keyword Arguments (**kwargs)
def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_details(
    name="Ajinkya",
    role="Data Analyst",
    skill="SQL"
)


# 6. Combining Different Argument Types
def create_report(title, *values, currency="INR", **metadata):
    print("Report:", title)
    print("Values:", values)
    print("Currency:", currency)
    print("Metadata:", metadata)


create_report(
    "Monthly Sales",
    12000,
    15000,
    18000,
    currency="INR",
    region="Pune",
    month="October"
)


# 7. Practical Example: Calculate Order Total
def calculate_order_total(price, quantity, discount=0):
    subtotal = price * quantity
    discount_amount = subtotal * discount
    return subtotal - discount_amount


print("Order Total:", calculate_order_total(500, 3))
print("Discounted Total:", calculate_order_total(500, 3, 0.10))


# Required, default, positional, keyword, *args, and **kwargs arguments.

def introduce(name, age):
    print(f"{name} is {age} years old.")

def greet(name, message="Welcome!"):
    print(f"{message}, {name}.")

def show_numbers(*args):
    print("args:", args)
    print("Total:", sum(args))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce("Madhav", 27)
introduce(age=27, name="Madhav")
greet("Keshav")
greet("Ketki", message="Good morning")
show_numbers(10, 20, 30)
print_details(name="Madhav", age=27, city="Nagpur")
