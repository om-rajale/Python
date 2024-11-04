class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False  # to track if the book is issued or not

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # list to hold Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                if not book.is_issued:
                    print(f"- {book}")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                print(f"Book '{title}' has been issued.")
                return
            elif book.title == title and book.is_issued:
                print(f"Book '{title}' is already issued.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                print(f"Book '{title}' has been returned.")
                return
            elif book.title == title and not book.is_issued:
                print(f"Book '{title}' was not issued.")
                return
        print(f"Book '{title}' not found in the library.")


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        library.issue_book(title)
        self.borrowed_books.append(title)

    def return_book(self, library, title):
        library.return_book(title)
        self.borrowed_books.remove(title)


# Example usage
library = Library("City Library")

# Adding books to the library
book1 = Book("Python Programming", "John Doe")
book2 = Book("Data Science", "Jane Doe")
library.add_book(book1)
library.add_book(book2)

# Creating a member
member = Member("Alice")

# Displaying available books
library.display_books()

# Member borrowing a book
member.borrow_book(library, "Python Programming")

# Displaying available books after issuing
library.display_books()

# Returning the book
member.return_book(library, "Python Programming")

# Displaying available books after returning
library.display_books()
