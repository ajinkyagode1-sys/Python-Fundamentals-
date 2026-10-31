
# Day 10: Python Lists
# Lists are ordered, mutable collections that allow duplicate values.


# 1. Creating Lists
numbers = [10, 20, 30, 40, 50]
names = ["Ajinkya", "Rahul", "Priya"]
mixed_list = [10, "Python", 25.5, True]
empty_list = []

print("Numbers:", numbers)
print("Names:", names)
print("Mixed List:", mixed_list)
print("Empty List:", empty_list)


# 2. Accessing List Elements (Indexing)
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("First Element:", fruits[0])
print("Last Element:", fruits[-1])


# 3. List Slicing
numbers = [10, 20, 30, 40, 50, 60]

print("First Three:", numbers[:3])
print("From Index 2:", numbers[2:])
print("Middle Elements:", numbers[1:4])
print("Reverse List:", numbers[::-1])


# 4. Updating List Elements
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"
print("Updated List:", fruits)


# 5. Adding Elements
numbers = [10, 20, 30]

numbers.append(40)
print("After append:", numbers)

numbers.extend([50, 60])
print("After extend:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)


# 6. Removing Elements
fruits = ["Apple", "Banana", "Mango", "Banana"]

fruits.remove("Banana")
print("After remove:", fruits)

removed_item = fruits.pop()
print("Popped Item:", removed_item)
print("After pop:", fruits)

del fruits[0]
print("After del:", fruits)

fruits.clear()
print("After clear:", fruits)


# 7. Searching and Counting
numbers = [10, 20, 30, 20, 40, 20]

print("Index of 30:", numbers.index(30))
print("Count of 20:", numbers.count(20))
print("Is 50 present?", 50 in numbers)


# 8. Sorting and Reversing
numbers = [50, 10, 40, 20, 30]

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

numbers.reverse()
print("Reversed:", numbers)


# 9. List Concatenation and Repetition
list_a = [1, 2, 3]
list_b = [4, 5, 6]

combined_list = list_a + list_b
print("Combined List:", combined_list)

repeated_list = list_a * 2
print("Repeated List:", repeated_list)


# 10. Copying Lists
original = [10, 20, 30]

copied_list = original.copy()
copied_list.append(40)

print("Original List:", original)
print("Copied List:", copied_list)


# 11. List Comprehension
numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]
print("Squares:", squares)

even_numbers = [number for number in numbers if number % 2 == 0]
print("Even Numbers:", even_numbers)


# 12. Nested Lists
sales_data = [
    [1000, 1500, 2000],
    [1200, 1800, 2200],
    [900, 1400, 1900]
]

print("First Region Sales:", sales_data[0])
print("First Sale of First Region:", sales_data[0][0])


# 13. Flattening a Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]

flattened_list = [
    item
    for sublist in nested_list
    for item in sublist
]

print("Flattened List:", flattened_list)


# 14. Practical Example: Calculate Total and Average Sales
daily_sales = [1200, 1500, 1800, 1000, 2000]

total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
highest_sales = max(daily_sales)
lowest_sales = min(daily_sales)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)


# Lists: ordered, mutable collections.

numbers = [10, 20, 30, 40]
print(numbers[0], numbers[-1], numbers[1:3])
numbers[1] = 25
numbers.append(50)
numbers.extend([60, 70])
numbers.insert(1, 15)
print("Updated:", numbers)

numbers.remove(30)
last_item = numbers.pop()
print("Popped:", last_item)
print("Index of 40:", numbers.index(40))
print("Count of 10:", numbers.count(10))
numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)
print("Copy:", numbers.copy())

squares = [value ** 2 for value in range(1, 6)]
evens = [value for value in range(1, 11) if value % 2 == 0]
upper_names = [name.upper() for name in ["ajinkya", "madhav"]]
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [value for sublist in nested for value in sublist]
print(squares, evens, upper_names, flattened)

for fruit in ["apple", "banana", "cherry", "mango"]:
    print(fruit)
