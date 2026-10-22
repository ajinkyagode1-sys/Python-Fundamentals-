# Type casting: implicit and explicit conversion.

result = 10 + 25.5
print("Implicit conversion:", result, type(result))

age = int("27")
height = float("5.8")
name = str("Ajinkya")
is_active = bool(1)

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_active, type(is_active))

# int("AJ") raises ValueError because "AJ" is not a valid integer string.
