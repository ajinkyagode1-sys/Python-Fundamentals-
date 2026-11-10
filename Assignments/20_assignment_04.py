
# Day 20: Assignment 4 - Employee Management System
# Concepts: Lists, Dictionaries, Functions, Loops, Conditional Statements

employees = []


def add_employee():
    """Add a new employee."""

    emp_id = input("Enter Employee ID: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee ID already exists.")
            return

    name = input("Enter Employee Name: ").strip()
    department = input("Enter Department: ").strip()

    try:
        salary = float(input("Enter Monthly Salary: "))

        if salary <= 0:
            print("Salary must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid salary.")
        return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added successfully.")


def view_employees():
    """Display all employee records."""

    if not employees:
        print("No employee records available.")
        return

    print("\n--- Employee Records ---")

    for employee in employees:
        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Salary: ₹{employee['salary']:.2f}"
        )


def search_employee():
    """Search employee by ID."""

    emp_id = input("Enter Employee ID to search: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            print("\nEmployee Found:")
            print(f"Name: {employee['name']}")
            print(f"Department: {employee['department']}")
            print(f"Salary: ₹{employee['salary']:.2f}")
            return

    print("Employee not found.")


def update_salary():
    """Update an employee's salary."""

    emp_id = input("Enter Employee ID: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            try:
                new_salary = float(input("Enter New Salary: "))

                if new_salary <= 0:
                    print("Salary must be greater than zero.")
                    return

                employee["salary"] = new_salary
                print("Salary updated successfully.")
                return

            except ValueError:
                print("Please enter a valid salary.")
                return

    print("Employee not found.")


def delete_employee():
    """Delete an employee record."""

    emp_id = input("Enter Employee ID to delete: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")


def salary_summary():
    """Calculate overall salary statistics."""

    if not employees:
        print("No employee records available.")
        return

    total_employees = len(employees)

    total_salary = sum(
        employee["salary"] for employee in employees
    )

    average_salary = total_salary / total_employees

    highest_paid = max(
        employees,
        key=lambda employee: employee["salary"]
    )

    lowest_paid = min(
        employees,
        key=lambda employee: employee["salary"]
    )

    print("\n--- Salary Summary ---")
    print(f"Total Employees: {total_employees}")
    print(f"Total Monthly Salary: ₹{total_salary:.2f}")
    print(f"Average Salary: ₹{average_salary:.2f}")

    print(
        f"Highest Paid: {highest_paid['name']} "
        f"(₹{highest_paid['salary']:.2f})"
    )

    print(
        f"Lowest Paid: {lowest_paid['name']} "
        f"(₹{lowest_paid['salary']:.2f})"
    )


def department_summary():
    """Calculate department-wise employee and salary statistics."""

    if not employees:
        print("No employee records available.")
        return

    department_data = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department not in department_data:
            department_data[department] = {
                "employee_count": 0,
                "total_salary": 0
            }

        department_data[department]["employee_count"] += 1
        department_data[department]["total_salary"] += salary

    print("\n--- Department-wise Summary ---")

    for department, data in department_data.items():
        average_salary = (
            data["total_salary"] / data["employee_count"]
        )

        print(f"\nDepartment: {department}")
        print(f"Employees: {data['employee_count']}")
        print(f"Total Salary: ₹{data['total_salary']:.2f}")
        print(f"Average Salary: ₹{average_salary:.2f}")


# Main program
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Overall Salary Summary")
    print("7. Department-wise Summary")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        salary_summary()

    elif choice == "7":
        department_summary()

    elif choice == "8":
        print("Exiting Employee Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 8.")
