from datetime import datetime, timedelta

# Predefined list of books (catalog)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "quantity": 3},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "quantity": 2},
    {"id": 3, "title": "1984", "author": "George Orwell", "quantity": 5},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "quantity": 4},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "quantity": 6}
]

# Dictionary to store user information
users = {}

# Dictionary to store book transactions
transactions = []

def display_catalog():
    print("Catalog:")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Quantity available: {book['quantity']}")

def register_user(user_id, name):
    if user_id in users:
        print("User already registered.")
    else:
        users[user_id] = {"name": name, "books_checked_out": []}
        print("User registered successfully.")

def checkout_book(user_id, book_id):
    user = users.get(user_id)
    if not user:
        print("User not found.")
        return
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("Book not found.")
        return
    if book["quantity"] == 0:
        print("Book not available for checkout.")
        return
    if len(user["books_checked_out"]) >= 3:
        print("Maximum limit reached for book checkout.")
        return
    user["books_checked_out"].append(book_id)
    book["quantity"] -= 1
    checkout_date = datetime.now()
    transactions.append({"user_id": user_id, "book_id": book_id, "checkout_date": checkout_date})
    print("Book checked out successfully.")

def return_book(user_id, book_id):
    user = users.get(user_id)
    if not user:
        print("User not found.")
        return
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("Book not found.")
        return
    if book_id not in user["books_checked_out"]:
        print("Book was not checked out by this user.")
        return
    user["books_checked_out"].remove(book_id)
    book["quantity"] += 1
    checkout_date = next((t["checkout_date"] for t in transactions if t["user_id"] == user_id and t["book_id"] == book_id), None)
    if checkout_date:
        due_date = checkout_date + timedelta(days=14)
        if datetime.now() > due_date:
            overdue_days = (datetime.now() - due_date).days
            overdue_fine = overdue_days * 1
            print(f"Book returned successfully. Overdue fine: ${overdue_fine}")
    else:
        print("Book return successful.")
    transactions[:] = [t for t in transactions if not (t["user_id"] == user_id and t["book_id"] == book_id)]

def list_overdue_books(user_id):
    user = users.get(user_id)
    if not user:
        print("User not found.")
        return
    overdue_books = []
    for transaction in transactions:
        if transaction["user_id"] == user_id:
            book_id = transaction["book_id"]
            book = next((b for b in books if b["id"] == book_id), None)
            if book:
                due_date = transaction["checkout_date"] + timedelta(days=14)
                if datetime.now() > due_date:
                    overdue_books.append(book)
    if overdue_books:
        print("Overdue Books:")
        for book in overdue_books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    else:
        print("No overdue books.")

def main():
    while True:
        print("\n1. Display catalog\n2. Register user\n3. Checkout book\n4. Return book\n5. List overdue books\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_catalog()
        elif choice == '2':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            register_user(user_id, name)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            book_id = int(input("Enter book ID: "))
            checkout_book(user_id, book_id)
        elif choice == '4':
            user_id = input("Enter user ID: ")
            book_id = int(input("Enter book ID: "))
            return_book(user_id, book_id)
        elif choice == '5':
            user_id = input("Enter user ID: ")
            list_overdue_books(user_id)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()