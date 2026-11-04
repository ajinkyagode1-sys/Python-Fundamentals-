
# ============================================================
# DAY 14: PYTHON OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================

# 1. Class and Object

# A class is a blueprint.
# An object is an instance of a class.

class Employee:
    pass


# Creating objects
employee1 = Employee()
employee2 = Employee()

print("Employee 1:", employee1)
print("Employee 2:", employee2)


# 2. Attributes and Methods

class Employee:
    # Class attribute
    company = "ABC Analytics"

    def display_details(self):
        print("Company:", self.company)


employee1 = Employee()
employee1.name = "Rahul"
employee1.salary = 50000

employee2 = Employee()
employee2.name = "Priya"
employee2.salary = 60000

employee1.display_details()

print("Name:", employee1.name)
print("Salary:", employee1.salary)


# 3. Constructor (__init__)

# The constructor initializes an object when it is created.

class Employee:
    company = "ABC Analytics"

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(
            f"ID: {self.emp_id}, "
            f"Name: {self.name}, "
            f"Department: {self.department}, "
            f"Salary: {self.salary}"
        )


employee1 = Employee(101, "Rahul", "Analytics", 50000)
employee2 = Employee(102, "Priya", "Marketing", 60000)

print("\n--- Employee Details ---")
employee1.display_details()
employee2.display_details()


# 4. Instance Methods

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def apply_raise(self, percentage):
        self.salary += self.salary * percentage / 100


employee = Employee("Amit", 50000)

print("\nAnnual Salary:", employee.annual_salary())

employee.apply_raise(10)

print("Salary After Raise:", employee.salary)


# 5. Class Method and Static Method

class Employee:
    company = "ABC Analytics"

    def __init__(self, name):
        self.name = name

    # Class method works with class-level data
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static method does not need self or cls
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


employee = Employee("Rahul")

print("\nCompany:", employee.company)

Employee.change_company("Data Solutions")

print("Updated Company:", employee.company)
print("Is Salary Valid?", Employee.is_valid_salary(50000))


# 6. Inheritance

# A child class can reuse attributes and methods
# from a parent class.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class DataAnalyst(Employee):
    def analyze_data(self):
        print(f"{self.name} is analyzing business data.")


analyst = DataAnalyst("Priya", 60000)

analyst.display()
analyst.analyze_data()


# 7. Method Overriding (Polymorphism)

class Employee:
    def work(self):
        print("Employee is working.")


class DataAnalyst(Employee):
    def work(self):
        print("Data Analyst is analyzing data.")


class DataScientist(Employee):
    def work(self):
        print("Data Scientist is building models.")


employees = [DataAnalyst(), DataScientist()]

print("\n--- Polymorphism ---")

for employee in employees:
    employee.work()


# 8. Encapsulation

# A leading underscore indicates an internal attribute
# by convention. It is not strict privacy.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 10000)

account.deposit(2500)

print("\nAccount Holder:", account.account_holder)
print("Account Balance:", account.get_balance())

# Direct access to the name-mangled attribute
# is not normally used:
# print(account.__balance)


# 9. Practical Data Analytics Example

class SalesRecord:
    def __init__(self, product, units_sold, price):
        self.product = product
        self.units_sold = units_sold
        self.price = price

    def calculate_revenue(self):
        return self.units_sold * self.price

    def display_record(self):
        revenue = self.calculate_revenue()

        print(
            f"Product: {self.product}, "
            f"Units Sold: {self.units_sold}, "
            f"Revenue: {revenue}"
        )


sales_records = [
    SalesRecord("Laptop", 10, 50000),
    SalesRecord("Mobile", 20, 20000),
    SalesRecord("Tablet", 15, 15000)
]

total_revenue = 0

print("\n--- Sales Analysis ---")

for record in sales_records:
    record.display_record()
    total_revenue += record.calculate_revenue()

print("Total Revenue:", total_revenue)


# ============================================================
# END OF DAY 14
# ============================================================
