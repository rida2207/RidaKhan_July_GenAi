# Function to add a book
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book {book_id} borrowed successfully.")
        else:
            print("Book is already borrowed.")
    else:
        print("Book does not exist.")
# Function to return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print("Book was not borrowed.")
# Function to register a member
def register_member(members, member_id):
    members.add(member_id)
# Function to show available books
def show_available(catalog, borrowed_books):
    print("Available Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"Book ID: {book_id}")
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Year: {year}")
            print()
# Main function
def main():
    # Empty data structures
    catalog = {}
    borrowed_books = []
    members = set()
    # Add books
    add_book(catalog, 101, "Python Basics", "John", 2020)
    add_book(catalog, 102, "Data Structures", "Alice", 2021)
    add_book(catalog, 103, "Machine Learning", "Bob", 2022)
    add_book(catalog, 104, "AI Fundamentals", "David", 2023)
    # Register members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)      
    print("Members:", members)
    # Borrow books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 102)
    print("Borrowed Books:", borrowed_books)
    # Return one book
    return_book(borrowed_books, 101)
    print("Borrowed Books after return:", borrowed_books)
    # Display available books
    show_available(catalog, borrowed_books)

# Call the main function
main()