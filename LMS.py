# 1_Basic Structure
library = {
    "Python Basics": {"author": "Test", "available": True, "issued_to": None},
    "Data Science": {"author": "Test1", "available": False, "issued_to": "John Doe"}
}

credentials = {"admin": "admin123", "librarian": "lib123"}

def display_welcome():
    print("\n" + "="*50)
    print("Welcome to Library Management System".center(50))
    print("="*50 + "\n")

def display_books():
    print("\n" + "-"*70)
    print("{:<30} {:<20} {:<15} {:<15}".format("Title", "Author", "Availability", "Issued To"))
    print("-"*70)
    for title, details in library.items():
        available = "Available" if details["available"] else "Issued"
        issued_to = details["issued_to"] if details["issued_to"] else "-"
        print("{:<30} {:<20} {:<15} {:<15}".format(
            title, details["author"], available, issued_to))
    print("-"*70 + "\n")

# 2_Adding Books
def add_book():
    while True:
        print("\nAdd a New Book")
        print("-"*30)
        print("1. Add a book")
        print("2. Back to Main Menu")
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            
            if title in library:
                print(f"\nError: Book '{title}' already exists in the library!")
            else:
                library[title] = {"author": author, "available": True, "issued_to": None}
                print(f"\nSuccess: Book '{title}' by {author} has been added to the library!")
        elif choice == "2":
            break
        else:
            print("\nInvalid choice! Please enter 1 or 2.")

# 3_Issuing Books
def issue_book():
    while True:
        print("\nIssue a Book")
        print("-"*30)
        print("1. Issue a book")
        print("2. Back to Main Menu")
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            title = input("Enter book title to issue: ").strip()
            if title not in library:
                print(f"\nError: Book '{title}' not found in the library!")
                continue
            
            if not library[title]["available"]:
                print(f"\nError: Book '{title}' is already issued to {library[title]['issued_to']}!")
                continue
            
            issuer_name = input("Enter your name: ").strip()
            library[title]["available"] = False
            library[title]["issued_to"] = issuer_name
            print(f"\nSuccess: Book '{title}' has been issued to {issuer_name}!")
        elif choice == "2":
            break
        else:
            print("\nInvalid choice! Please enter 1 or 2.")

# 4_Returning Books
def return_book():
    while True:
        print("\nReturn a Book")
        print("-"*30)
        print("1. Return a book")
        print("2. Back to Main Menu")
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            title = input("Enter book title to return: ").strip()
            if title not in library:
                print(f"\nError: Book '{title}' not found in the library!")
                continue
            
            if library[title]["available"]:
                print(f"\nError: Book '{title}' is already available in the library!")
                continue
            
            issuer_name = library[title]["issued_to"]
            library[title]["available"] = True
            library[title]["issued_to"] = None
            print(f"\nSuccess: Book '{title}' has been returned by {issuer_name}!")
        elif choice == "2":
            break
        else:
            print("\nInvalid choice! Please enter 1 or 2.")

# 5_Login System
def login():
    attempts = 3
    while attempts > 0:
        print("\nLogin to Library Management System")
        print("-"*40)
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username in credentials and credentials[username] == password:
            print(f"\nWelcome, {username}!")
            return True
        else:
            attempts -= 1
            print(f"\nInvalid credentials! {attempts} attempts remaining.")
    
    print("\nMaximum login attempts reached. Exiting...")
    return False

# 6_View Issued Books
def view_issued_books():
    while True:
        print("\n" + "-"*70)
        print("Currently Issued Books".center(70))
        print("-"*70)
        print("{:<30} {:<20} {:<15}".format("Title", "Author", "Issued To"))
        print("-"*70)
        
        issued_books = [book for book in library.values() if not book["available"]]
        if not issued_books:
            print("No books are currently issued.".center(70))
        else:
            for title, details in library.items():
                if not details["available"]:
                    print("{:<30} {:<20} {:<15}".format(
                        title, details["author"], details["issued_to"]))
        print("-"*70)
        
        print("\n1. Refresh List")
        print("2. Back to Main Menu")
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("\nInvalid choice! Please enter 1 or 2.")

# 7_Main Menu
def main_menu():
    while True:
        print("\nLibrary Management System - Main Menu")
        print("-"*40)
        print("1. View All Books")
        print("2. Add a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. View Issued Books")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_issued_books()
        elif choice == "6":
            print("\nThank you for using Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1-6.")

# Main_Program
if __name__ == "__main__":
    display_welcome()
    if login():
        main_menu()
