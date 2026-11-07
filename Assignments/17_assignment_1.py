
# ============================================================
# DAY 17: ASSIGNMENT 1 - STUDENT MARKS ANALYZER
# ============================================================

# Problem:
# Create a program to analyze a student's marks in 5 subjects.
#
# Requirements:
# 1. Take the student's name.
# 2. Take marks in 5 subjects.
# 3. Validate marks between 0 and 100.
# 4. Calculate total, average, and percentage.
# 5. Assign a grade.
# 6. Display pass/fail status.
# 7. Display highest and lowest marks.


# ------------------------------------------------------------
# 1. Function to Get Valid Marks
# ------------------------------------------------------------

def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# ------------------------------------------------------------
# 2. Function to Calculate Grade
# ------------------------------------------------------------

def calculate_grade(average):
    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


# ------------------------------------------------------------
# 3. Function to Analyze Student Marks
# ------------------------------------------------------------

def analyze_marks(student_name, marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    # Since each subject is out of 100,
    # average marks are also the percentage.
    percentage = average_marks

    grade = calculate_grade(average_marks)

    # A student must score at least 35 in every subject
    # to pass.
    if all(mark >= 35 for mark in marks):
        result = "Pass"
    else:
        result = "Fail"

    print("\n" + "=" * 40)
    print("        STUDENT MARKS REPORT")
    print("=" * 40)

    print("Student Name:", student_name)

    print("\nSubject-wise Marks:")

    for index, mark in enumerate(marks, start=1):
        print(f"Subject {index}: {mark}")

    print("\nTotal Marks:", total_marks)
    print("Average Marks:", round(average_marks, 2))
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    print("=" * 40)


# ------------------------------------------------------------
# 4. Main Program
# ------------------------------------------------------------

def main():
    print("STUDENT MARKS ANALYZER")
    print("-" * 30)

    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    subjects = [
        "Python",
        "SQL",
        "Statistics",
        "Excel",
        "Power BI"
    ]

    marks = []

    for subject in subjects:
        mark = get_valid_marks(subject)
        marks.append(mark)

    analyze_marks(student_name, marks)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()


# ============================================================
# END OF DAY 17
# ============================================================
