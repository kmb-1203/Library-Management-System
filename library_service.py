from book import Book
from member import Member
from datetime import datetime

class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            new_book = Book(book_id, title, author)
            self.books[book_id] = new_book
            return True, "Book added successfully!"
        return False, "Book ID already exists!"

    def register_member(self, member_id, name, email):
        if member_id not in self.members:
            new_member = Member(member_id, name, email)
            self.members[member_id] = new_member
            return True, "Member registered successfully!"
        return False, "Member ID already exists!"

    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            return False, "Error: Book not found!"

        if member_id not in self.members:
            return False, "Error: Member not found!"

        book = self.books[book_id]

        if not book.available:
            return False, "Error: Book is already borrowed!"

        book.available = False
        loan = {
            'book_id': book_id,
            'member_id': member_id,
            'borrow_date': datetime.now(),
            'return_date': None
        }
        self.loans.append(loan)
        return True, f"Success! Member {self.members[member_id].name} borrowed '{book.title}'"

    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            return False, "Error: Book not found!"

        if member_id not in self.members:
            return False, "Error: Member not found!"

        book = self.books[book_id]

        if book.available:
            return False, "Error: Book is not borrowed!"

        for loan in self.loans:
            if loan['book_id'] == book_id and loan['member_id'] == member_id and loan['return_date'] is None:
                loan['return_date'] = datetime.now()
                book.available = True
                return True, f"Success! '{book.title}' returned by {self.members[member_id].name}"

        return False, "Error: No active loan found for this book and member!"

    def view_books(self):
        if not self.books:
            return "No books found."
        
        output = ["=== Books in Library ==="]
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            output.append(f"ID: {book.book_id:3} | Title: {book.title:<30} | Author: {book.author:<20} | {status}")
        
        return "\n".join(output)

    def view_members(self):
        if not self.members:
            return "No members found."
        
        output = ["=== Registered Members ==="]
        for member in self.members.values():
            output.append(f"ID: {member.member_id:3} | Name: {member.name:<20} | Email: {member.email:<30}")
        
        return "\n".join(output)

    def view_loans(self):
        if not self.loans:
            return "No loan records found."
        
        output = ["=== Loan Records ==="]
        for idx, loan in enumerate(self.loans, 1):
            book = self.books[loan['book_id']]
            member = self.members[loan['member_id']]
            status = "Active" if loan['return_date'] is None else "Closed"
            
            output.append(
                f"{idx}. Book: {book.title:<25} | Borrower: {member.name:<20} | "
                f"Borrowed: {loan['borrow_date'].strftime('%Y-%m-%d %H:%M')} | "
                f"Returned: {loan['return_date'].strftime('%Y-%m-%d %H:%M') if loan['return_date'] else 'Not Returned'} | Status: {status}"
            )
        
        return "\n".join(output)
