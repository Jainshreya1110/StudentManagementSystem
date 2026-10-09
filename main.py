"""
Student Management System
A beginner friendly console application.
"""

from student_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    show_results,
)


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 42)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. View marks and results")
    print("7. Exit")
    print("=" * 42)


def get_menu_choice():
    """Read and validate the menu choice."""
    while True:
        choice = input("Enter your choice (1 to 7): ").strip()
        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            return choice
        print("Invalid choice. Please enter a number from 1 to 7.")


def main():
    """Run the application until the user chooses Exit."""
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_results()
        elif choice == "7":
            print("Thank you for using Student Management System. Goodbye!")
            break


if __name__ == "__main__":
    main()
