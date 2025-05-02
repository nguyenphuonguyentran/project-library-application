'''
CPRG 216C

Project: Classes - Group7 OOP-Masters!

Part 2 Program :
.

Programmers:    Naz Zaamout
                Nguyen Phuong Uyen Tran
                Jasjot Singh
                Abrar Bala

Date: April 11, 2024
'''

import book,os

# CONSTANTS
HEADER_MENU =  "\nReader's Guild Library - Main Menu\n" + "=" * 34

HEADER_STAFF = "\nReader's Guild Library - Librarian Menu\n" + "=" * 39

CATALOG_HEADER = f"{'ISBN':14s} {'Title':25s} {'Author':25s} {'Genre':20s} {'Availability':s}\n{'-' * 14:14s} {'-' * 25:25s} {'-' * 25:25s} {'-' * 20:20s} {'-' * 12:12s}"

MENU = {1 : "Search for books",
        2 : "Borrow a book",
        3 : "Return a book", 
        0 : "Exit the system"   
        }

STAFF_MENU = {1 : "Search for books",
        2 : "Borrow a book",
        3 : "Return a book",
        4 : "Add a book",
        5 : "Remove a book",
        6 : "Print catalog",
        0 : "Exit the system"
        }

# LISTS
records = []

# FUNCTIONS
# Defining function load_books()
def load_books(book_list, file_path):
    # Opening the file
    file = open(file_path, 'r')
    # Defining variable num_books_loaded which counts the number of books loaded
    num_books_loaded = 0
    # Iterating over each line in the file and parsing attribute values into separate variables
    for line in file:
        components = line.strip().split(',')
        isbn, title, author, genre, available = components
        # Creating Book objects from each set of attributes
        new_book = book.Book(isbn, title, author, genre, available)
        # Adding Book objects into the list
        book_list.append(new_book)
        num_books_loaded += 1
    # Closing the file
    file.close()
    # Returning the number of books loaded
    return num_books_loaded


# Defining function print_menu()
def print_menu(heading, menu_options):
    # Displaying heading
    print(heading)

    # Displaying menu options passed in
    for i in menu_options:
        print(f"{i}. {menu_options[i]}")
    
    # Getting input from user until valid selection is entered
    user_input = input("Enter your selection: ")
    validation = True
    while validation:
        if user_input == "2130":
            output = "2130"
            validation = False
        elif user_input in str(list(menu_options.keys())):
            output = user_input
            validation = False
        else:
            print("Invalid option")
            user_input = input("Enter your selection: ")

    # Returning user's valid selection
    return int(output)



# Defining function search_books()
def search_books(book_list, search_string):
    # Creating a list of search result
    search_list = []
    search_string = search_string.lower()
    # Iterating over the book list
    for i in book_list:
        # Using IF statements to check the occurence of the search string in isbn, title, author, or genre. The book will be added into the search result list if any match is found
        if search_string in book.Book.get_isbn(i).lower():
            search_list.append(i)
        elif search_string in book.Book.get_title(i).lower(): 
            search_list.append(i)
        elif search_string in book.Book.get_author(i).lower():
            search_list.append(i)
        elif search_string in book.Book.get_genre_name(i).lower():
            search_list.append(i)

    # Returning None if there is no book found         
    if len(search_list) == 0:
        output = None
    # Returning search result list if there is any books found
    else:
        output = search_list
    return output
    

# Defining function borrow_book()
def borrow_book(book_list):
    # Printing out "Borrowing" message and getting ISBN input
    print("\n-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    # Calling find_book_by_isbn() function to get the index of a specific book from the book_list
    index_return = find_book_by_isbn(book_list, isbn)

    # Executing appropriate actions based on the returned index

    # Case 1: No book is found
    if index_return == -1:
        print("No book found with that ISBN.")
    else:
        # Case 2: A matching book is found and is available to borrow
        if book.Book.get_available(book_list[index_return]) == "Available":
            # Invoking borrow_it() method from book.py 
            book.Book.borrow_it(book_list[index_return]) 
            print(f"'{book.Book.get_title(book_list[index_return])}' with ISBN {book.Book.get_isbn(book_list[index_return])} successfully borrowed.")
        
        # Case 3: A matching book is found and is unavailable to borrow
        elif book.Book.get_available(book_list[index_return]) == "Borrowed":
            print(f"'{book.Book.get_title(book_list[index_return])}' with ISBN {book.Book.get_isbn(book_list[index_return])} is not currently available.")
            

# Defining function find_book_by_isbn()
def find_book_by_isbn(book_list, isbn):
    # Assigning a default value None to the return_data
    return_data = None
    for each_book in book_list:
        # Returning a new value for return_data when a specific ISBN is found in the book_list
        if isbn == book.Book.get_isbn(each_book):
            return_data = book_list.index(each_book)
    # Assigning -1 to the return_value if the return_data has not changed its default value 0, which means there is no book found
    if return_data == None:
        return_value = -1
    # Assigning the index of the matching book to the return_value
    else:
        return_value = return_data
    # Returning the appropriate value
    return return_value


# Defining function return_book()
def return_book(book_list):
    # Printing out "Returning" message and getting ISBN input
    print("\n-- Return a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    # Calling find_book_by_isbn() function to get the index of a specific book from the book_list
    index_return = find_book_by_isbn(book_list, isbn)

    # Executing appropriate actions based on the returned index

    # Case 1: No book is found
    if index_return == -1:
        print("No book found with that ISBN.")
    else:
        # Case 2: A matching book is found but is not currently borrowed 
        if book.Book.get_available(book_list[index_return]) == "Available":
            print(f"'{book.Book.get_title(book_list[index_return])}' with ISBN {book.Book.get_isbn(book_list[index_return])} is not currently borrowed.")
        
        # Case 3: A matching book is found and is currently borrowed
        elif book.Book.get_available(book_list[index_return]) == "Borrowed":
            # Invoking return_it() method from book.py 
            book.Book.return_it(book_list[index_return]) 
            print(f"'{book.Book.get_title(book_list[index_return])}' with ISBN {book.Book.get_isbn(book_list[index_return])} successfully returned.")
            

# Defining function add_book()
def add_book(book_list):
    print("\n-- Add a book --")
    # Getting input from the user for ISBN, title, author, and genre name
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    genre_name = input("Enter genre: ")

    # Validating if the genre name is in the list of genre names or not
    genre = None
    while genre == None:
        for i in book.Book.GENRE_NAMES:
        # Translating the genre name into its integer value
            if genre_name == book.Book.GENRE_NAMES[i]:
                genre = i
        # Printing error messages and asking the user until the valid input is entered
        if genre == None:            
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
            genre_name = input("Enter genre: ")
    
    # Creating a new Book instance
    new_book = book.Book(isbn, title, author, genre, available = True)

    # Appending the new Book instance into the book list
    book_list.append(new_book)
    
    print(f"'{title}' with ISBN {isbn} sucessfully added.")
    
    
# Defining function remove_book() 
def remove_book(book_list):
    # Getting input from the user for ISBN
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    # Calling find_book_by_isbn() function to get the index of a specific book from the book list
    book_index = find_book_by_isbn(book_list, isbn)
    
    # Removing a specific book if its index is returned
    if book_index != -1:
        book_to_remove = book_list[book_index]
        del book_list[book_index]
        print(f"'{book_to_remove.get_title()}' with ISBN {isbn} successfully removed.")       
    
    # Printing a message if there is no book found from the book list
    else:
        print("No book found with that ISBN")  
        
        
# Defining function print_books()        
def print_books(book_list):

    # Printing the book information heading
    print(CATALOG_HEADER)

    # Iterating over the book list and display each Book object on each single line
    for books in book_list:
        print (books)
        
        
# Defining function save_books()
def save_books(list, path):

    # Opening the file
    file = open(path,"w")

    # Iterating over the book list
    for i in list:
        if book.Book.get_available(i) == "Available":
            available = True
        elif book.Book.get_available(i) == "Borrowed":
            available = False
        # Formatting a comma separated string containing each book's attribute values
        x = [book.Book.get_isbn(i), book.Book.get_title(i), book.Book.get_author(i), book.Book.get_genre(i), available]
        
        str_value = ""
        
        # Writing each strings as a single line to the file
        for j in x:
            if str(j) == str(x[-1]):
                str_value += (str(j) + "\n")
            else:
                str_value += (str(j) + ",")
        file.write(str_value)

    # Closing the file
    file.close()
    return "Book catalog has been saved."



def main():
    # Printing the "Starting the system" message and asking for the pathname of the CSV data file from the user
    print("Starting the system ...")
    file_location = input("Enter book catalog filename: ")
    
    # Validating the pathname of the CSV data file and printing appropriate messages
    while not os.path.exists(file_location):
        file_location = input("File not found. Re-enter book catalog filename: ")
    # Populating the book list by calling load_books()
    load_books(records, file_location)
    print("Book catalog has been loaded.")
    
    # Presenting the menu
    selection = print_menu(HEADER_MENU, MENU)
    # Evaluating the user's selection
    # Appropriate actions when the user does not choose to quit the program
    while selection != 0:
        # Case 1: Options for the user menu    
        while selection != 2130:
            # Option 1: Searching for books
            if selection == 1:
                print("\n-- Search for books --")
                search_string = input("Enter search value: ")
                if search_books(records, search_string) == None:
                    print("No matching books found.")
                else:
                    print_books(search_books(records, search_string))
            # Option 2: Borrowing a book
            elif selection == 2:
                borrow_book(records)
            # Option 3: Returning a book
            elif selection == 3:
                return_book(records)
            elif selection == 0:
                break
            # Continuing printing the user menu
            selection = print_menu(HEADER_MENU, MENU)

        # Case 2: Options for the librarian menu    
        while selection == 2130:
            selection_staff = print_menu(HEADER_STAFF, STAFF_MENU)
            # Option 1: Searching for books
            if selection_staff == 1:
                print("\n-- Search for books --")
                search_string = input("Enter search value: ")
                if search_books(records, search_string) == None:
                    print("No matching books found.")
                else:
                    print_books(search_books(records, search_string))
            # Option 2: Borrowing a book
            elif selection_staff == 2:
                borrow_book(records)
            # Option 3: Returning a book
            elif selection_staff == 3:
                return_book(records)
            # Option 4: Adding a book
            elif selection_staff == 4:
                add_book(records)
            # Option 5: Removing a book
            elif selection_staff == 5:
                remove_book(records)
            # Option 6: Printing catalog
            elif selection_staff == 6:
                print("\n -- Print book catalog --")
                print_books(records)
            # Option 0: Exiting the system
            elif selection_staff == 0:
                selection = selection_staff
    # Printing the exit message when the user chooses to quit the program
    print("\n--Exit the system --",
          "\n"+save_books(records, file_location), # Calling save_books() to save list of Books to the file before ending the program
          "\nGood Bye!") 
    return

if __name__ == '__main__':
    main()
