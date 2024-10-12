# library_management.py

class Book:
    """Class to represent a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return whether the book is available for checkout."""
        return not self._is_checked_out

class Library:
    """Class to represent a library containing multiple books."""
    
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"{title} has been checked out.")
                return
        print(f"{title} is not available.")

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"{title} has been returned.")
                return
        print(f"{title} is not checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
