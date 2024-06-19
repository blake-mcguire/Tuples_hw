# TASK 1 FLIGHTS

random_list_of_tuples = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def flights(records):
    for item in records:
        print(f"Iteninerary 1: {item[0]} - From {item[1]} to {item[2]}")
        
            
flights(random_list_of_tuples)



# TASK 2 LIBRARY SYSTEM
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def lib_sys(books):
    print('Here is our fine selection of books to choose from')
    for book in books:
        print(f"Book: {book[0]} ~ Written By {book[1]}")
    new_book = input("Enter a new book to add to the library: ")
    author = input('Who Wrote The book?: ')
    new_tup = (new_book, author)
    if new_tup not in books:
        books.append(new_tup)
    else:
        print('Book already in the library')
    print('Here is our updated library')
    for book in books:
        print(f"Book: {book[0]} ~ Written By {book[1]}")

lib_sys(library)