"""
Functions for adding, viewing, searching, updating, deleting,
and calculating student results.

Student records are stored in students.json in this project folder.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")
PASS_MARKS = 40
MAX_MARKS = 100


def load_students():
    """Load student records from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            students = json.load(file)
        if isinstance(students, list):
            return students
        print("Warning: the data file format is incorrect. Starting with an empty list.")
        return []
    except (json.JSONDecodeError, OSError):
        print("Warning: student data could not be read. Check students.json.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("Error: student records could not be saved.")
        return False


def get_non_empty_text(prompt):
    """Keep asking until the user enters non empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_integer(prompt, minimum=None, maximum=None):
    """Read an integer and optionally check its allowed range."""
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and number < minimum:
            print("The number must be at least", minimum)
            continue
        if maximum is not None and number > maximum:
            print("The number must not be more than", maximum)
            continue
        return number


def find_student_by_id(students, student_id):
    """Return a matching student dictionary, or None if not found."""
    for student in students:
        if student["id"].lower() == student_id.lower():
            return student
    return None


def add_student():
    """Ask for student details and save a new record."""
    students = load_students()
    print("\n--- Add Student ---")

    student_id = get_non_empty_text("Enter student ID: ")
    if find_student_by_id(students, student_id) is not None:
        print("That student ID already exists. Please use a unique ID.")
        return

    name = get_non_empty_text("Enter student name: ")
    age = get_integer("Enter student age: ", minimum=1, maximum=120)
    marks = get_integer("Enter marks (0 to 100): ", minimum=0, maximum=MAX_MARKS)

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks,
    }
    students.append(student)

    if save_students(students):
        print("Student added successfully.")


def view_students():
    """Display every saved student."""
    students = load_students()
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    print("{:<12} {:<24} {:<8} {:<8}".format("ID", "NAME", "AGE", "MARKS"))
    print("-" * 56)
    for student in students:
        print(
            "{:<12} {:<24} {:<8} {:<8}".format(
                student["id"],
                student["name"][:23],
                student["age"],
                student["marks"],
            )
        )


def search_student():
    """Search by student ID or by name."""
    students = load_students()
    if not students:
        print("No student records found.")
        return

    search_text = get_non_empty_text("Enter student ID or name to search: ").lower()
    matches = []

    for student in students:
        if (
            student["id"].lower() == search_text
            or search_text in student["name"].lower()
        ):
            matches.append(student)

    if not matches:
        print("No matching student found.")
        return

    print("\n--- Search Results ---")
    for student in matches:
        print_student_details(student)


def print_student_details(student):
    """Print one student's details and result."""
    result = "PASS" if student["marks"] >= PASS_MARKS else "FAIL"
    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Age        :", student["age"])
    print("Marks      :", str(student["marks"]) + "/" + str(MAX_MARKS))
    print("Result     :", result)
    print("-" * 30)


def update_student():
    """Update a student's name, age, or marks."""
    students = load_students()
    if not students:
        print("No student records found.")
        return

    student_id = get_non_empty_text("Enter the ID of the student to update: ")
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    new_name = input("Name [" + student["name"] + "]: ").strip()
    if new_name:
        student["name"] = new_name

    while True:
        age_text = input("Age [" + str(student["age"]) + "]: ").strip()
        if not age_text:
            break
        try:
            age = int(age_text)
        except ValueError:
            print("Please enter a whole number or press Enter to keep the current age.")
            continue
        if 1 <= age <= 120:
            student["age"] = age
            break
        print("Age must be between 1 and 120.")

    while True:
        marks_text = input("Marks [" + str(student["marks"]) + "]: ").strip()
        if not marks_text:
            break
        try:
            marks = int(marks_text)
        except ValueError:
            print("Please enter a whole number or press Enter to keep the current marks.")
            continue
        if 0 <= marks <= MAX_MARKS:
            student["marks"] = marks
            break
        print("Marks must be between 0 and 100.")

    if save_students(students):
        print("Student details updated successfully.")


def delete_student():
    """Delete a student after asking for confirmation."""
    students = load_students()
    if not students:
        print("No student records found.")
        return

    student_id = get_non_empty_text("Enter the ID of the student to delete: ")
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Selected student:", student["name"], "(", student["id"], ")")
    confirmation = input("Type YES to confirm deletion: ").strip()

    if confirmation == "YES":
        students.remove(student)
        if save_students(students):
            print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def show_results():
    """Display each student's marks, pass/fail result, and class average."""
    students = load_students()
    print("\n--- Marks and Results ---")

    if not students:
        print("No student records found.")
        return

    total_marks = 0
    passed = 0

    for student in students:
        marks = student["marks"]
        result = "PASS" if marks >= PASS_MARKS else "FAIL"
        print(
            student["id"],
            "|",
            student["name"],
            "| Marks:",
            str(marks) + "/" + str(MAX_MARKS),
            "|",
            result,
        )
        total_marks = total_marks + marks
        if marks >= PASS_MARKS:
            passed = passed + 1

    average = total_marks / len(students)
    print("-" * 42)
    print("Number of students:", len(students))
    print("Class average:", round(average, 2))
    print("Passed:", passed)
    print("Failed:", len(students) - passed)
    print("Passing marks:", PASS_MARKS)
