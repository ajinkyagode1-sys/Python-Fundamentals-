
# ============================================================
# DAY 15: MODULES, PACKAGES, LIBRARIES & PIP
# ============================================================

# A MODULE is a Python file containing reusable code.
# A PACKAGE is a collection of modules.
# A LIBRARY is a collection of reusable code/tools.
# pip is used to install and manage Python packages.


# ------------------------------------------------------------
# 1. Importing Built-in Modules
# ------------------------------------------------------------

import math
import random
import statistics
from datetime import date

print("--- Built-in Modules ---")

# math module
print("Square Root:", math.sqrt(64))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Value of Pi:", math.pi)

# random module
random_number = random.randint(1, 10)
print("Random Number:", random_number)

# statistics module
sales = [1200, 1500, 1800, 2000, 2500]

print("Mean Sales:", statistics.mean(sales))
print("Median Sales:", statistics.median(sales))

# datetime module
today = date.today()
print("Today's Date:", today)


# ------------------------------------------------------------
# 2. Importing a Module with an Alias
# ------------------------------------------------------------

import statistics as stats

monthly_sales = [10000, 15000, 18000, 22000]

average_sales = stats.mean(monthly_sales)

print("\nAverage Monthly Sales:", average_sales)


# ------------------------------------------------------------
# 3. Importing Specific Functions
# ------------------------------------------------------------

from math import sqrt, pow

print("\nSquare Root of 81:", sqrt(81))
print("2 Raised to 3:", pow(2, 3))


# ------------------------------------------------------------
# 4. Creating and Using Your Own Module
# ------------------------------------------------------------

# Suppose we create another Python file:
#
# File: sales_utils.py
#
# def calculate_revenue(units, price):
#     return units * price
#
# def calculate_discount(amount, discount_percent):
#     return amount * discount_percent / 100
#
# We can import these functions into another Python file:
#
# from sales_utils import calculate_revenue
#
# revenue = calculate_revenue(10, 500)
# print(revenue)
#
# This example is shown as comments because sales_utils.py
# is a separate file and is not created by this script.


# ------------------------------------------------------------
# 5. Understanding __name__ == "__main__"
# ------------------------------------------------------------

# This condition is commonly used to prevent code from
# running automatically when a module is imported.

def display_message():
    print("This function is running directly.")


if __name__ == "__main__":
    display_message()


# ------------------------------------------------------------
# 6. Understanding Packages
# ------------------------------------------------------------

# Example package structure:
#
# my_project/
# |
# |-- main.py
# |
# |-- sales_package/
#     |
#     |-- __init__.py
#     |-- calculations.py
#     |-- reports.py
#
# calculations.py might contain:
#
# def calculate_revenue(units, price):
#     return units * price
#
# main.py might use:
#
# from sales_package.calculations import calculate_revenue
#
# revenue = calculate_revenue(10, 500)


# ------------------------------------------------------------
# 7. External Libraries
# ------------------------------------------------------------

# External libraries are installed separately.
#
# Examples:
#
# NumPy      -> Numerical computing
# Pandas     -> Data manipulation and analysis
# Matplotlib -> Data visualization
# Seaborn    -> Statistical visualization
#
# Installation commands are shown below in the notes.


# ------------------------------------------------------------
# 8. Practical Data Analytics Example
# ------------------------------------------------------------

# statistics is a built-in module.
# We can use it to calculate basic business metrics.

daily_revenue = [12000, 15000, 18000, 14000, 22000, 25000]

total_revenue = sum(daily_revenue)
average_revenue = stats.mean(daily_revenue)
median_revenue = stats.median(daily_revenue)
highest_revenue = max(daily_revenue)
lowest_revenue = min(daily_revenue)

print("\n--- Revenue Analysis ---")
print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Median Revenue:", median_revenue)
print("Highest Revenue:", highest_revenue)
print("Lowest Revenue:", lowest_revenue)


# Import styles


# Import the full module
import math
math.sqrt(25)

# Import a specific function
from math import sqrt
sqrt(25)

# Import with an alias
import statistics as stats
stats.mean([10, 20, 30])

# pip commands Use in Windows PowerShell
# Use these commands in your terminal, not inside the Python file:

# Check Python version
py --version

# Check pip version
py -m pip --version

# Install a package
py -m pip install numpy

# Install multiple packages
py -m pip install pandas matplotlib seaborn

# Check installed packages
py -m pip list

# Show details of a package
py -m pip show pandas

# Upgrade a package
py -m pip install --upgrade pandas

# Uninstall a package
py -m pip uninstall pandas

# ============================================================
# END OF DAY 15
# ============================================================
