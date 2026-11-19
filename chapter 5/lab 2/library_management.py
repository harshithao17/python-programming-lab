class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        print("\nAVAILABLE BOOKS")

        for book in self.books:
            print(book)

    def search_book(self, book):
        if book in self.books:
            print("Book is available")
        else:
            print("Book not found")


library = Library()

while True:

    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book = input("Enter book name to search: ")
        library.search_book(book)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")