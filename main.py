from library_service import LibraryService

def main():
    library = LibraryService()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. View All Members")
        print("7. View Loan Records")
        print("8. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-8.")
            continue

        if choice == 1:
            print("\n--- Add New Book ---")
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            
            success, message = library.add_book(book_id, title, author)
            print(message)

        elif choice == 2:
            print("\n--- Register New Member ---")
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            email = input("Enter Member Email: ")
            
            success, message = library.register_member(member_id, name, email)
            print(message)

        elif choice == 3:
            print("\n--- Borrow Book ---")
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            
            success, message = library.borrow_book(book_id, member_id)
            print(message)

        elif choice == 4:
            print("\n--- Return Book ---")
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            
            success, message = library.return_book(book_id, member_id)
            print(message)

        elif choice == 5:
            print("\n" + library.view_books())

        elif choice == 6:
            print("\n" + library.view_members())

        elif choice == 7:
            print("\n" + library.view_loans())

        elif choice == 8:
            print("Program closed.")
            break

        else:
            print("Invalid choice! Please select between 1-8.")

if __name__ == "__main__":
    main()
