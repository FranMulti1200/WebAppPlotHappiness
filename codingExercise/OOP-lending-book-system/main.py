class BookLendingSystem:
    def __init__(self):
        self.available_books = {
            1: "The Great Gatsby",
            2: "To Kill a Mockingbird",
            3: "1984",
            4: "Pride and Prejudice"
        }
        self.borrowed_books = {}

        #self.borrow_book =

    def display_menu(self):
        print("\nWelcome to the Book Lending System!")
        print("\n1. View Available Books")
        print("\n2. Borrow a Book")
        print("\n3. Return a Book")
        print("\n4. View Borrowed Books")
        print("\n5. Exit")
        print("")

    def view_available_books(self):
        print("\n--- Available Books ---\n")
        if not self.available_books:
            print("No books available.")
        else:
            #for book_id in self.available_books:
            for book_id, title in self.available_books.items():
                #valor = self.available_books[book_id]
                print(f"{book_id}. {title}\n")

    def borrow_book(self):
        if not self.available_books:
            print("Book ID not found!")
        else:
            self.view_available_books()
            try:
                book_id = int(input("\nEnter the book number to borrow: ").strip())
                if book_id in self.available_books:
                    title = self.available_books.pop(book_id)
                    user_name = input("Enter your name: ").strip()
                    self.borrowed_books[book_id] = (title, user_name)
                    print((f"\nYou have borrowed '{title}'. Please return it on time"))
                else:
                    print("\nInvalid Book ID.")
            except ValueError:
                print("\nPlease enter a valid numeric Book ID.")

    def return_book(self):
        if not self.borrowed_books:
            print("\nNo books have been borrowed.")
        else:
            print("\nBorrowed Books:")
            self.view_borrowed_books()
            try:
                book_id = int(
                    input("\nEnter the Book ID you want to return: ").strip())
                if book_id in self.borrowed_books:
                    book_title, borrower_name = self.borrowed_books.pop(
                        book_id)
                    self.available_books[book_id] = book_title
                    print(f"\n'{book_title}' has been successfully returned.")
                else:
                    print("\nInvalid Book ID.")
            except ValueError:
                print("\nPlease enter a valid numeric Book ID.")


    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("\nNo books are currently borrowed.")
        else:
            print("\nBorrowed Books:")
            for book_id, (title, borrower) in self.borrowed_books.items():
                print(f"{book_id}. {title} (Borrowed by: {borrower})")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nChoose an option: ").strip()
            if choice == "1":
                self.view_available_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.view_borrowed_books()
            elif choice == "5":
                print("\nThank you for using the Book Lending System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")



system = BookLendingSystem()
system.run()