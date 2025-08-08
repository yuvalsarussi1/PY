class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.borrow()
                    print(f"\n✅ You have borrowed '{book.title}'")
                    return
                else:
                    print(f"\n❌ '{book.title}' is already borrowed.")
                    return
        print("\n❌ Book not found.")

library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("The Alchemist", "Paulo Coelho"))
library.add_book(Book("Dune", "Frank Herbert"))

while True:
    print("\nLibrary Menu:")
    print("1. Show available books")
    print("2. Borrow a book")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable books:")
        for book in library.books:
            if not book.is_borrowed:
                print(f"- {book.title} by {book.author}")
    elif choice == "2":
        title = input("Enter the title of the book you want to borrow: ")
        library.borrow_book(title)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")