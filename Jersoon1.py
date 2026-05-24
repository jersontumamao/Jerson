# Listing datas
books = []
members = []
loans = []

# add book funtion
def add_book():
    print("\n" + "=" * 40)
    print("ADD BOOK")
    print("=" * 40)

    book_id = input("ENTER BOOK ID: ")
    book_title = input("ENTER BOOK TITLE: ")
    book_author = input("ENTER BOOK AUTHOR: ")

    book = {
        "id": book_id,
        "title": book_title,
        "author": book_author,
        "available": True
    }

    books.append(book)

    print("\nBOOK ADDED SUCCESSFULLY!")
    print(f"BOOK TITLE: {book_title}")

# register member function
def register_member():
    print("\n" + "=" * 40)
    print("REGISTER MEMBER")
    print("=" * 40)

    member_id = input("ENTER MEMBER ID: ")
    member_name = input("ENTER MEMBER NAME: ")

    member = {
        "id": member_id,
        "name": member_name
    }

    members.append(member)

    print("\nMEMBER REGISTERED SUCCESSFULLY!")
    print(f"MEMBER NAME: {member_name}")

# borrow book function
def borrow_book():
    print("\n" + "=" * 40)
    print("BORROW BOOK")
    print("=" * 40)

    member_id = input("ENTER MEMBER ID: ")
    book_id = input("ENTER BOOK ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["available"]:

                loan = {
                    "member_id": member_id,
                    "book_id": book_id,
                    "book_title": book["title"]
                }

                loans.append(loan)

                # Set unavailable
                book["available"] = False

                print(f"\nBOOK BORROWED: {book['title']}")
                return

            else:
                print("\nBOOK IS NOT AVAILABLE.")
                return

    print("\nBOOK NOT FOUND.")

# return book funtion
def return_book():
    print("\n" + "=" * 40)
    print("RETURN BOOK")
    print("=" * 40)

    book_id = input("ENTER BOOK ID TO RETURN: ")

    for loan in loans:
        if loan["book_id"] == book_id:

            loans.remove(loan)

            for book in books:
                if book["id"] == book_id:
                    book["available"] = True

            print("\nBOOK RETURNED SUCCESSFULLY!")
            return

    print("\nLOAN RECORD NOT FOUND.")

# view book funtion
def view_books():
    print("\n" + "=" * 40)
    print("LIST OF BOOKS")
    print("=" * 40)

    if len(books) == 0:
        print("NO BOOKS AVAILABLE.")
    else:
        for book in books:
            status = "Available" if book["available"] else "Borrowed"

            print(f"""
BOOK ID: {book['id']}
TITLE: {book['title']}
AUTHOR: {book['author']}
STATUS: {status}
------------------------------
""")

# view member function
def view_members():
    print("\n" + "=" * 40)
    print("LIST OF MEMBERS")
    print("=" * 40)

    if len(members) == 0:
        print("NO MEMBERS REGISTERED.")
    else:
        for member in members:
            print(f"""
MEMBER ID: {member['id']}
MEMBER NAME: {member['name']}
------------------------------
""")

# view loans function
def view_loans():
    print("\n" + "=" * 40)
    print("LIST OF LOANS")
    print("=" * 40)

    if len(loans) == 0:
        print("NO ACTIVE LOANS.")
    else:
        for loan in loans:
            print(f"""
MEMBER ID: {loan['member_id']}
BOOK ID: {loan['book_id']}
BOOK TITLE: {loan['book_title']}
------------------------------
""")

# Mmenu
while True:

    print("\n" + "=" * 40)
    print("===== Library Management System =====")
    print("=" * 40)

    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")

    print("=" * 40)

    choice = input("Select an option: ")

    print("=" * 40)

    if choice == '1':
        add_book()

    elif choice == '2':
        register_member()

    elif choice == '3':
        borrow_book()

    elif choice == '4':
        return_book()

    elif choice == '5':
        view_books()

    elif choice == '6':
        view_members()

    elif choice == '7':
        view_loans()

    elif choice == '8':
        print("\nYou have exited the system!")
        break

    else:
        print("\nInvalid option. Please try again.")