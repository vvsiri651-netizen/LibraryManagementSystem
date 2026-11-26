from abc import ABC, abstractmethod
from datetime import datetime


# ==========================================
# ABSTRACT CLASS
# ==========================================

class LibraryItem(ABC):

    @abstractmethod
    def display_info(self):
        pass


# ==========================================
# BOOK CLASS
# ==========================================

class Book(LibraryItem):

    def __init__(
        self,
        book_id,
        title,
        author,
        status="Available",
        issue_date="",
        return_date=""
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__status = status
        self.issue_date = issue_date
        self.return_date = return_date

    def display_info(self):

        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.__status}")

        if self.issue_date != "":
            print(f"Issue Date: {self.issue_date}")

        if self.return_date != "":
            print(f"Return Date: {self.return_date}")

        print("-" * 30)

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


# ==========================================
# REFERENCE BOOK CLASS
# ==========================================

class ReferenceBook(Book):

    def display_info(self):

        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("Type: Reference Book")
        print(f"Status: {self.get_status()}")

        if self.issue_date != "":
            print(f"Issue Date: {self.issue_date}")

        if self.return_date != "":
            print(f"Return Date: {self.return_date}")

        print("-" * 30)


# ==========================================
# LIBRARY CLASS
# ==========================================

class Library:

    def __init__(self):
        self.books = []

    # --------------------------------------
    # ADD BOOK
    # --------------------------------------

    def add_book(self):

        try:

            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            # Check duplicate ID
            for book in self.books:

                if book.book_id == book_id:

                    print("Book ID already exists!")
                    return

            book = Book(
                book_id,
                title,
                author
            )

            self.books.append(book)

            print("Book added successfully!")

        except ValueError:

            print("Invalid Book ID. Please enter a number.")

    # --------------------------------------
    # VIEW BOOKS
    # --------------------------------------

    def view_books(self):

        if len(self.books) == 0:

            print("No books available.")

        else:

            print("\n========== BOOK LIST ==========")

            for book in self.books:

                book.display_info()

    # --------------------------------------
    # SEARCH BOOK
    # --------------------------------------

    def search_book(self):

        try:

            book_id = int(
                input("Enter Book ID to search: ")
            )

            for book in self.books:

                if book.book_id == book_id:

                    print("\nBook Found!")

                    book.display_info()

                    return

            print("Book not found.")

        except ValueError:

            print("Invalid Book ID. Please enter a number.")

    # --------------------------------------
    # ISSUE BOOK
    # --------------------------------------

    def issue_book(self):

        try:

            book_id = int(
                input("Enter Book ID to issue: ")
            )

            for book in self.books:

                if book.book_id == book_id:

                    if book.get_status() == "Available":

                        book.set_status("Issued")

                        # Get current date and time
                        current_time = datetime.now()

                        book.issue_date = current_time.strftime(
                            "%d-%m-%Y %H:%M:%S"
                        )

                        # Clear previous return date
                        book.return_date = ""

                        print("Book issued successfully!")

                        print(
                            f"Issue Date: {book.issue_date}"
                        )

                    else:

                        print("Book is already issued.")

                    return

            print("Book not found.")

        except ValueError:

            print("Invalid Book ID. Please enter a number.")

    # --------------------------------------
    # RETURN BOOK
    # --------------------------------------

    def return_book(self):

        try:

            book_id = int(
                input("Enter Book ID to return: ")
            )

            for book in self.books:

                if book.book_id == book_id:

                    if book.get_status() == "Issued":

                        book.set_status("Available")

                        # Get current date and time
                        current_time = datetime.now()

                        book.return_date = current_time.strftime(
                            "%d-%m-%Y %H:%M:%S"
                        )

                        print("Book returned successfully!")

                        print(
                            f"Return Date: {book.return_date}"
                        )

                    else:

                        print("Book is already available.")

                    return

            print("Book not found.")

        except ValueError:

            print("Invalid Book ID. Please enter a number.")

    # --------------------------------------
    # DELETE BOOK
    # --------------------------------------

    def delete_book(self):

        try:

            book_id = int(
                input("Enter Book ID to delete: ")
            )

            for book in self.books:

                if book.book_id == book_id:

                    self.books.remove(book)

                    print("Book deleted successfully!")

                    return

            print("Book not found.")

        except ValueError:

            print("Invalid Book ID. Please enter a number.")

    # --------------------------------------
    # SAVE DATA
    # --------------------------------------

    def save_data(self):

        try:

            with open("library_data.txt", "w") as file:

                for book in self.books:

                    file.write(
                        f"{book.book_id}|"
                        f"{book.title}|"
                        f"{book.author}|"
                        f"{book.get_status()}|"
                        f"{book.issue_date}|"
                        f"{book.return_date}\n"
                    )

            print("Library data saved successfully!")

        except Exception as e:

            print("Error while saving data:", e)

    # --------------------------------------
    # LOAD DATA
    # --------------------------------------

    def load_data(self):

        try:

            with open("library_data.txt", "r") as file:

                for line in file:

                    line = line.strip()

                    if line == "":
                        continue

                    data = line.split("|")

                    if len(data) == 6:

                        book_id = int(data[0])
                        title = data[1]
                        author = data[2]
                        status = data[3]
                        issue_date = data[4]
                        return_date = data[5]

                        book = Book(
                            book_id,
                            title,
                            author,
                            status,
                            issue_date,
                            return_date
                        )

                        self.books.append(book)

            print("Library data loaded successfully!")

        except FileNotFoundError:

            print(
                "No saved data found. "
                "Starting with an empty library."
            )

        except Exception as e:

            print("Error while loading data:", e)


# ==========================================
# CREATE LIBRARY OBJECT
# ==========================================

library = Library()


# ==========================================
# LOAD SAVED DATA
# ==========================================

library.load_data()


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n==========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("==========================================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Save Data")
    print("8. Exit")

    print("==========================================")

    choice = input("Enter your choice: ")

    # OPTION 1
    if choice == "1":

        library.add_book()

    # OPTION 2
    elif choice == "2":

        library.view_books()

    # OPTION 3
    elif choice == "3":

        library.search_book()

    # OPTION 4
    elif choice == "4":

        library.issue_book()

    # OPTION 5
    elif choice == "5":

        library.return_book()

    # OPTION 6
    elif choice == "6":

        library.delete_book()

    # OPTION 7
    elif choice == "7":

        library.save_data()

    # OPTION 8
    elif choice == "8":

        library.save_data()

        print(
            "\nThank you for using "
            "Library Management System!"
        )

        break

    # INVALID CHOICE
    else:

        print("Invalid choice. Please try again.")