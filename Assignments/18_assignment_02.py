
# ============================================================
# DAY 18: ASSIGNMENT 2 - EXPENSE TRACKER
# ============================================================

# This program allows users to:
# 1. Add expenses
# 2. View all expenses
# 3. Calculate total and average expenses
# 4. Display category-wise summary
# 5. Find highest and lowest expenses
# 6. Exit the program


# ------------------------------------------------------------
# 1. Function to Get Valid Amount
# ------------------------------------------------------------

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount > 0:
                return amount

            print("Amount must be greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")


# ------------------------------------------------------------
# 2. Function to Add Expense
# ------------------------------------------------------------

def add_expense(expenses):
    print("\n--- Add Expense ---")

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    amount = get_valid_amount()

    description = input("Enter description: ").strip()

    expense = {
        "category": category.title(),
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


# ------------------------------------------------------------
# 3. Function to Display All Expenses
# ------------------------------------------------------------

def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"Category: {expense['category']} | "
            f"Amount: {expense['amount']:.2f} | "
            f"Description: {expense['description']}"
        )


# ------------------------------------------------------------
# 4. Function to Calculate Total and Average
# ------------------------------------------------------------

def calculate_summary(expenses):
    if not expenses:
        print("\nNo expenses available for analysis.")
        return

    amounts = [expense["amount"] for expense in expenses]

    total_expense = sum(amounts)
    average_expense = total_expense / len(amounts)

    print("\n--- Expense Summary ---")
    print("Number of Expenses:", len(expenses))
    print("Total Expense:", round(total_expense, 2))
    print("Average Expense:", round(average_expense, 2))
    print("Highest Expense:", max(amounts))
    print("Lowest Expense:", min(amounts))


# ------------------------------------------------------------
# 5. Function for Category-wise Summary
# ------------------------------------------------------------

def category_summary(expenses):
    if not expenses:
        print("\nNo expenses available for category analysis.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n--- Category-wise Expense Summary ---")

    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")


# ------------------------------------------------------------
# 6. Main Program
# ------------------------------------------------------------

def main():
    expenses = []

    while True:
        print("\n" + "=" * 35)
        print("         EXPENSE TRACKER")
        print("=" * 35)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            calculate_summary(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")


# Execute the main program
if __name__ == "__main__":
    main()


# ============================================================
# END OF DAY 18
# ============================================================
