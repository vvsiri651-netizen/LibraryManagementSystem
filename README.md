# Library Management System

## Project Description

The Library Management System is a menu-driven Python application developed to manage books in a library.

The system allows the user to add, view, search, issue, return, and delete books. It also provides file handling functionality to save and load library data.

## Objectives

- To manage library books using Python.
- To understand Object-Oriented Programming concepts.
- To implement file handling.
- To use exception handling for invalid input.
- To store and retrieve book information.
- To create a simple real-world Python application.

## Features

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Save Data
8. Exit

## Python Concepts Used

### 1. Classes and Objects

The project uses classes such as `Book` and `Library` to organize the program.

### 2. Inheritance

The `Book` class inherits from the abstract `LibraryItem` class.

### 3. Abstraction

`LibraryItem` is an abstract class containing the abstract method `display_info()`.

### 4. Encapsulation

The book status is stored using the private variable `__status`.

### 5. Polymorphism

The `display_info()` method is implemented differently in `Book` and `ReferenceBook`.

### 6. File Handling

The project uses `library_data.txt` to save and load book information.

### 7. Exception Handling

`try-except` blocks are used to handle invalid book IDs and file errors.

### 8. Date and Time

Python's `datetime` module is used to record book issue and return dates.

## Project Structure

```text
LibraryManagementSystem
│
├── main.py
├── library_data.txt
└── README.md
```

## How to Run

Open the project folder in Visual Studio Code.

Open the terminal and run:

```text
python main.py
```

The Library Management System menu will appear.

## Menu Options

| Option | Function |
|---|---|
| 1 | Add Book |
| 2 | View Books |
| 3 | Search Book |
| 4 | Issue Book |
| 5 | Return Book |
| 6 | Delete Book |
| 7 | Save Data |
| 8 | Exit |

## Sample Output

```text
==========================================
       LIBRARY MANAGEMENT SYSTEM
==========================================
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Save Data
8. Exit
==========================================
Enter your choice:
```

## Example

A user can add a book by selecting option 1:

```text
Enter your choice: 1
Enter Book ID: 101
Enter Book Title: Python Programming
Enter Author Name: John
Book added successfully!
```

The book can then be issued:

```text
Enter your choice: 4
Enter Book ID to issue: 101
Book issued successfully!
Issue Date: 26-11-2026 13:05:20
```

## Conclusion

This project demonstrates how Python can be used to develop a simple real-world Library Management System using Object-Oriented Programming, file handling, exception handling, and date-time functionality.