# Student Management System

A beginner friendly Python console project for managing student records.

## Features

1. Add a student with a unique ID, name, age, and marks.
2. View all student records.
3. Search by exact student ID or part of a name.
4. Update a student's name, age, or marks.
5. Delete a record after confirmation.
6. View marks, pass or fail status, class average, and pass/fail counts.
7. Validate input to reduce common errors.
8. Save records in `students.json`, so records remain after the program closes.

## Requirements

- Python 3.10 or newer is recommended.
- Visual Studio Code.
- No extra Python packages are required.

## Project files

```text
StudentManagementSystem/
|-- main.py
|-- student_manager.py
|-- students.json
|-- README.md
```

### What each file does

- `main.py`: shows the menu and calls the relevant functions.
- `student_manager.py`: contains functions for student operations and JSON file storage.
- `students.json`: stores student records. It starts empty.
- `README.md`: explains the project and how to run it.

## Run in Visual Studio Code

1. Download and extract `StudentManagementSystem.zip`.
2. Open Visual Studio Code.
3. Choose **File > Open Folder**.
4. Select the extracted `StudentManagementSystem` folder.
5. If Python is not installed, install Python from https://www.python.org/downloads/.
6. In VS Code, install the Microsoft Python extension if it is not already installed.
7. Open `main.py`.
8. Open the terminal using **Terminal > New Terminal**.
9. Run this command:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```bash
   py main.py
   ```

10. Choose an option from the menu by entering its number.

## Quick test

1. Choose `1` to add a student.
2. Example values: ID `S101`, name `Asha`, age `20`, marks `82`.
3. Choose `2` to view all students.
4. Choose `3` and search for `S101` or `Asha`.
5. Choose `6` to see marks and the class average.
6. Choose `7` to exit.
7. Run `python main.py` again and choose `2`. The student should still be there.

## Rules used by this project

- Student IDs must be unique, ignoring uppercase and lowercase differences.
- Age must be a whole number from 1 to 120.
- Marks must be a whole number from 0 to 100.
- A student passes with 40 marks or more.
- During an update, press Enter to keep the existing value.
- To confirm deletion, type `YES` in uppercase.

## Python concepts practised

- Variables and data types
- Lists and dictionaries
- `if`, `elif`, and `else`
- `while` and `for` loops
- Functions and arguments
- Returning values
- String methods such as `strip()` and `lower()`
- Input validation with `try` and `except`
- Reading and writing JSON files
- Importing functions from another Python file

## Troubleshooting

### `python` is not recognized

Try `py main.py` in the VS Code terminal. If that does not work, install Python and restart VS Code. During Windows installation, enable the option to add Python to PATH.

### The menu starts but records do not save

Make sure you have permission to write inside the project folder. Check that `students.json` is present and contains valid JSON. The initial content should be `[]`.

### I accidentally deleted the data

Deleted records are removed from `students.json`. Make a backup copy of this file if the records matter.

## Limitations

This is a learning project, not a secure production system. It stores data in a local JSON file and does not have user accounts, encryption, or a database.
