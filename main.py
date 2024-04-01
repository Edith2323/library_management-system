#!/usr/bin/python3

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available Books:")
            for book in self.books:
                if book.available:
                    print(f"{book.title} by {book.author}")

    def borrow_book(self, title):
        if not self.books:
            print("No books available in the library.")
            return
        
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You have borrowed '{book.title}' by {book.author}.")
                return
        print("Book not available for borrowing.")

    def return_book(self, title):
        if not self.books:
            print("No books available in the library.")
            return
        
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You have returned '{book.title}' by {book.author}.")
                return
        print("Book not found or already returned.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Available Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            new_book = Book(title, author)
            library.add_book(new_book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter title of the book you want to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter title of the book you want to return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
