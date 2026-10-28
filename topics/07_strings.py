
# Day 7: Python Strings
# Strings are used to store and manipulate text.


# 1. Creating Strings
single_quote = 'Hello Python'
double_quote = "Welcome to Python"
multiline_text = """This is
a multiline string."""

print(single_quote)
print(double_quote)
print(multiline_text)


# 2. String Indexing
text = "Python"

print("First character:", text[0])
print("Last character:", text[-1])


# 3. String Slicing
text = "Python Programming"

print("First six characters:", text[:6])
print("From index 7:", text[7:])
print("Characters from index 0 to 5:", text[0:6])
print("Reverse string:", text[::-1])


# 4. String Concatenation and Repetition
first_name = "Data"
last_name = "Analyst"

full_name = first_name + " " + last_name
print("Full name:", full_name)
print("Repeated text:", "Python " * 3)


# 5. String Formatting
name = "Ajinkya"
age = 22
salary = 25000

print(f"My name is {name} and I am {age} years old.")
print("Salary: {}".format(salary))
print("Age: %d" % age)


# 6. Escape Sequences and Raw Strings
print("Hello\nWorld")
print("Name:\tAjinkya")
print("He said, \"Python is useful.\"")

path = r"C:\Users\Student\Documents"
print("File path:", path)


# 7. Common String Methods
text = "  python programming  "

print("Original:", repr(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Stripped:", text.strip())
print("Replaced:", text.replace("python", "data"))
print("Count of 'm':", text.count("m"))
print("Position of 'programming':", text.find("programming"))
print("Split:", text.split())


# 8. String Membership and Length
language = "Python"

print("Length:", len(language))
print("'Py' exists:", "Py" in language)
print("'Java' does not exist:", "Java" not in language)


# 9. Strings Are Immutable
word = "Python"

# Strings cannot be changed character by character.
# word[0] = "J"  # This raises a TypeError.

word = "J" + word[1:]
print("Updated string:", word)


# 10. Practical Example: Cleaning Customer Data
customer_name = "  aJINKYA gode  "

cleaned_name = customer_name.strip().title()

print("Original name:", repr(customer_name))
print("Cleaned name:", cleaned_name)

# Strings: quoting, formatting, indexing, slicing, and methods.

single_quotes = 'Python'
double_quotes = "is fun"
multiline = '''Quotes: "double" and 'single'.'''
print(single_quotes, double_quotes)
print(multiline)

name, age = "Ajinkya", 27
print("Name: %s, age: %d" % (name, age))
print("Name: {}, age: {}".format(name, age))
print(f"Name: {name}, age: {age}")
print("First line\nSecond line")
print("Column 1\tColumn 2")
print(r"Raw string keeps \n as two characters")

word = "Python Course"
print("Concatenation:", "Hello" + " " + "Python")
print("Repetition:", "Hi! " * 3)
print("'Course' in word:", "Course" in word)
print("First character:", word[0])
print("First six characters:", word[:6])
print("Slice with step 2:", word[2:8:2])
print("Reverse:", word[::-1])

sample = "  python programming  "
print(len(sample), sample.upper(), sample.lower(), sample.title())
print(sample.count("p"), sample.find("gram"))
print(sample.replace("python", "data"))
print(sample.strip())
print("red,green,blue".split(","))
print(" - ".join(["red", "green", "blue"]))

def middle_characters(text):
    middle = len(text) // 2
    if len(text) % 2 == 0:
        return text[middle - 1:middle + 1]
    return text[middle]

print("Middle of Madhav:", middle_characters("Madhav"))
print("Remove first/last 3:", "Regression Analysis"[3:-3])
print("Last 4 characters:", "Classification"[-4:])
