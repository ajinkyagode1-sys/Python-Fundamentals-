
# Day 21: Calculator Mini Project
# Operations: Addition, Subtraction, Multiplication, Division, Average

# Arithmetic functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def average(a, b):
    return (a + b) / 2


# Map menu choices to their respective functions

OPERATIONS = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Average", average),
}


def main():

    while True:

        print("\n========== SIMPLE CALCULATOR ==========")

        for key, (label, _) in OPERATIONS.items():
            print(f"{key}. {label}")

        print("6. Exit")

        choice = input("\nSelect an operation (1-6): ").strip()

        # Exit the calculator

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        # Validate menu choice

        if choice not in OPERATIONS:
            print("Invalid operation. Please select between 1 and 6.")
            continue

        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))

            label, operation = OPERATIONS[choice]

            result = operation(first, second)

            print(f"\n{label}: {result:g}")

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

        except ZeroDivisionError as error:
            print(f"Error: {error}")


# Run the main program

if __name__ == "__main__":
    main()
