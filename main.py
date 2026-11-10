
books = [    
    {"id": 1,        
    "name": "Harry Potter",
    "author": "J.K. Rowling",
    "year": 1997,
    "available": True    },

    {"id": 2,
    "name": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "available": True    },

    {"id": 3,
    "name": "Clean Code",
    "author": "Robert Martin",
    "year": 2008,
    "available": False    },

    {"id": 4,
    "name": "Atomic Habits",
    "author": "James Clear",
    "year": 2018,
    "available": True    },

    {"id": 5,
    "name": "The Pragmatic Programmer",
    "author": "David Thomas",
    "year": 1999,
    "available": False    }]

def display_books(books):  
    for book in books:
        print(book)

def get_book_by_search(books):  
    name = get_book_input()
    book = search_book(books, name)
    if book is not None:
        print(f"Book : {book}")

def get_book_input():  
    while True:
        search_input = input("enter a book:")
        if search_input.strip() == "":
            print("invalid input")
            continue
        return search_input

def search_book(books, name):
    for book in books:
        if name.strip().lower() in book["name"].lower():
            return book
    print("book not found")




def add_book(books, name, author, year):
    new_id = get_next_book_id(books)    
    
    new_book = {"id":new_id,
                "name":name,
                "author":author,
                "year":year,
                "available":  True
                }

    books.append(new_book)
    return True
    
def get_new_book(books):
    while True:
        name = input("enter a book name:")
        if name.strip() == "":
            print("book must be with name")
            continue
        break
       

    while True:
        author = input("enter author name:")
        if author.strip() == "":
            print("book must be with author")
            continue
        break

    while True:
        try:
            year = int(input("enter year:"))

            if year <= 0:
                print("invalid year")
                continue
            break

        except ValueError:
            print("please enter a valid number")
        

    success = add_book(books, name, author, year)

    if success:
        print("Book added successfully")
    else:
        print("Book already exists or invalid details")


def get_next_book_id(books):
    if not books:
        return 1

    highest_id = 0

    for book in books:
        if book["id"] > highest_id:
            highest_id = book["id"]

    return highest_id + 1


def get_book_id():
    while True:
        try:
            book_id = int(input("Enter book ID: "))
            if book_id <= 0:
                print("Invalid book ID")
                continue
            return book_id
        except ValueError:
            print("Please enter a valid number")

def get_borrow_book(books):
    book_id = get_book_id()
    success = borrow_book(books, book_id)

    if success:
        print("Book borrowed successfully")
    else:
        print("Book not found or unavailable")

def borrow_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return True
    return False
def get_return_book(books):
    book_id = get_book_id()
    success = return_book(books, book_id)

    if success:
        print("Book returned successfully")
    else:
        print("Book not found or already available")

def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                book["available"] = True
                return True

    return False
   

def get_available_books(books):
    available_books = []

    for book in books:
        if book["available"] == True:
            available_books.append(book)

    return available_books

def show_available_book(books):
    available_books = get_available_books(books)

    for book in available_books:
        print(book)


def get_author_by_search(books):
    author = get_author_input()
    found_books = get_books_by_author(books, author)

    if found_books:
        for book in found_books:
            print(book)
    else:
        print("author not found")

def get_author_input():  
    while True:
        search_input = input("enter a author:")
        if search_input.strip() == "":
            print("invalid input")
            continue
        return search_input

def get_books_by_author(books, author):
    found_books = []

    for book in books:
        if author.strip().lower() in book["author"].lower():
            found_books.append(book)

    return found_books
        

def main():
    escape = False
    while not escape:
        user_choice = input("""
        ================================
            LIBRARY MANAGEMENT
        ================================

        1. Display all books
        2. Search book by name
        3. Add new book
        4. Borrow a book
        5. Return a book
        6. Display available books
        7. Display books by author
        8. Exit

        Choose an option:

                """)
                
        if user_choice == "1":
            display_books(books)

        elif user_choice == "2":
            get_book_by_search(books)

        elif user_choice == "3":
            get_new_book(books)

        elif user_choice == "4":
            get_borrow_book(books)

        elif user_choice == "5":
            get_return_book(books)

        elif user_choice == "6":
            show_available_book(books)

        elif user_choice == "7":
            get_author_by_search(books)

        elif user_choice == "8":
            escape = True

        else:
            print("Invalid choice")
        
main()









