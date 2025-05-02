'''
CPRG 216C

Project: Classes - Group7 OOP-Masters!

Part 1 Program Introduction:
To fulfill the requirements for the Reader's Guild Library's inventory and borrowing system, we will start by
creating the Book class in a file named book.py.
This class will include getters and setters for the book's attributes, methods for borrowing and returning books,
as well as method to format the product information as a string.

Programmers:    Naz Zaamout
                Nguyen Phuong Uyen Tran
                Jasjot Singh
                Abrar Bala

Date: April 11, 2024
'''

# Create the Book class:
class Book:

    # Implement Genre table as a class constant
    # Dictionary maps genre IDs to Genre names
    GENRE_NAMES = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }

    
    # Constructor to initialize five HIDDEN product attributes
    # Hidden for internal use within the class
    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = available


    # Getters for the book's properties - 5 attributes
    # Allow value access to the value of the hidden attributes
    def get_isbn(self):
        return self.__isbn
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_available(self):
        return self.__available
    
    # Additional getter method that returns the name of the genre as a string from the class constant table
    # Method that uses the genre ID to look up the genre name in the GENRE_NAMES dictionary
    def get_genre_name(self):
        return Book.GENRE_NAMES[self.get_genre()]
    
    # Additional getter method to return a string based on the available attribute. 
    # Method to indicate whether the book is available or borrowed
    def get_available(self):
        if self.__available == True or self.__available =="True":
            msg = "Available"
        elif self.__available == False or self.__available == "False":
            msg = "Borrowed"
        return msg


    # Setters for the book's properties - 4 attributes
    # Allow value modifications of the hidden attributes
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre


    # Method for borrowing books - Sets the book's available attribute to False
    def borrow_it(self):                                
        self.__available = False 



    # Method for returning books - Sets the book's available attribute to True
    # This method is used to indicate that the book has been returned 
    def return_it(self):
        self.__available = True                         # Book is returned - it is available


    # Method to format the product information as a string
    def __str__(self):
        # isbn: 14 characters | Title: Give it 25 characters for now | Author: give it 25 characters for now | Genre: 18 char- give it 20 | Availability: :s
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.__isbn, self.__title, self.__author, self.get_genre_name(), self.get_available())

