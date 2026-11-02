
# ============================================================
# DAY 12: PYTHON SETS
# ============================================================

# 1. Creating Sets

# Empty set
empty_set = set()

# Set with values
numbers = {10, 20, 30, 40, 50}

# Duplicate values are automatically removed
duplicate_numbers = {10, 20, 20, 30, 30, 40}

print("Numbers:", numbers)
print("Duplicates Removed:", duplicate_numbers)
print("Empty Set:", empty_set)


# 2. Set Properties

# Sets are:
# - Unordered
# - Mutable
# - Made of unique elements
# - Not indexable

print("\nNumber of Elements:", len(numbers))
print("Is 20 Present?", 20 in numbers)

# This will raise an error because sets do not support indexing:
# print(numbers[0])


# 3. Adding Elements

fruits = {"Apple", "Banana", "Mango"}

# Add one element
fruits.add("Orange")

# Add multiple elements
fruits.update(["Grapes", "Pineapple"])

print("\nUpdated Fruits:", fruits)


# 4. Removing Elements

fruits = {"Apple", "Banana", "Mango", "Orange"}

# remove() raises KeyError if element is absent
fruits.remove("Banana")

# discard() does not raise an error if element is absent
fruits.discard("Papaya")

# pop() removes an arbitrary element
removed_item = fruits.pop()

print("\nAfter Removal:", fruits)
print("Popped Item:", removed_item)

# clear() removes all elements
fruits.clear()
print("Cleared Set:", fruits)


# 5. Set Union

# Union combines all unique elements from both sets

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

union_result = set_a.union(set_b)

print("\nUnion:", union_result)
print("Union using |:", set_a | set_b)


# 6. Set Intersection

# Intersection returns common elements

intersection_result = set_a.intersection(set_b)

print("\nIntersection:", intersection_result)
print("Intersection using &:", set_a & set_b)


# 7. Set Difference

# Difference returns elements present in the first set
# but not in the second set

difference_result = set_a.difference(set_b)

print("\nDifference A - B:", difference_result)
print("Difference using -:", set_a - set_b)

print("Difference B - A:", set_b - set_a)


# 8. Symmetric Difference

# Returns elements present in either set,
# but not in both

symmetric_result = set_a.symmetric_difference(set_b)

print("\nSymmetric Difference:", symmetric_result)
print("Using ^:", set_a ^ set_b)


# 9. Set Comparison

small_set = {10, 20}
large_set = {10, 20, 30, 40}

print("\nIs Subset?", small_set.issubset(large_set))
print("Is Superset?", large_set.issuperset(small_set))
print("Are Disjoint?", small_set.isdisjoint({100, 200}))


# 10. Updating Sets

a = {1, 2, 3}
b = {3, 4, 5}

# Update a with union
a.update(b)
print("\nAfter update():", a)

# Intersection update
c = {1, 2, 3}
c.intersection_update({2, 3, 4})
print("After intersection_update():", c)

# Difference update
d = {1, 2, 3}
d.difference_update({2, 3})
print("After difference_update():", d)


# 11. Converting List to Set

customer_ids = [101, 102, 103, 101, 104, 102, 105]

unique_customer_ids = set(customer_ids)

print("\nOriginal Customer IDs:", customer_ids)
print("Unique Customer IDs:", unique_customer_ids)
print("Unique Customer Count:", len(unique_customer_ids))


# 12. Practical Data Analytics Example

# Customers who purchased in January
january_customers = {101, 102, 103, 104, 105}

# Customers who purchased in February
february_customers = {103, 104, 105, 106, 107}

# Customers who purchased in both months
repeat_customers = january_customers & february_customers

# Customers who purchased in January but not February
churned_or_inactive_customers = january_customers - february_customers

# Customers who purchased in February but not January
new_customers = february_customers - january_customers

# Customers who purchased in either month
all_customers = january_customers | february_customers

print("\n--- Customer Analysis ---")
print("Repeat Customers:", repeat_customers)
print("January Only Customers:", churned_or_inactive_customers)
print("February New Customers:", new_customers)
print("Total Unique Customers:", len(all_customers))



# Sets store unique hashable values; they are unordered and not indexed.

numbers = {1, 2, 3, 3, 2}
print("Duplicates removed:", numbers)
numbers.add(4)
numbers.discard(99)
print("After updates:", numbers)

left = {1, 2, 3, 4}
right = {3, 4, 5, 6}
print("Union:", left | right)
print("Intersection:", left & right)
print("Difference:", left - right)
print("Symmetric difference:", left ^ right)

for value in left:
    print(value)

cubes = {number ** 3 for number in range(1, 6)}
print("Cubes:", cubes)
# Set display order is not guaranteed.


# ============================================================
# END OF DAY 12
# ============================================================
