# 5. Library Management System
# Problem

# Design a library system.

# Requirements

# Each book should contain:

# book id
# title
# author
# availability status
# Functionalities
# Issue book
# Return book
# Display availability
# Count total books using class variable
# Additional Challenge

# Prevent issuing already issued books.

# Concepts Practiced
# object state changes
# boolean flags
# class variables


class LibraryManagement:
    books_counter = 0
    def __init__(self,book_id,title,author,quantity):
        self.__id = book_id 
        self.__title = title
        self.__author = author 
        
        self.__quantity = quantity
        self.__collection = {}
        if self.__quantity>0:
            self.__status=True
        else:
            self.__status = False
        self.__collection[self.__title] = self.__quantity
        LibraryManagement.books_counter+=1
    
    def display_available_books(self):
        print("name\tquantity")
        if len( self.__collection)>0:
            for key, values in self.__collection.items():
                if values>0:
                    print(f"{key}      {values}")
                

        else:
            print("No books are available")

    def issue_books(self):
        self.display_available_books()
        print(f"\n")
        book_name = input("Enter the name of the book here : ")
        if book_name in self.__collection:

            if self.__collection[book_name] > 0:

                self.__collection[book_name] -= 1
                print("Your book has been issued successfully")

            else:
                print("Book is not available")
        else:
            print("Book is not available")

    
    def return_books(self):
        book_name = input("Enter a name of the book here : ")
        if book_name in self.__collection:

            self.__collection[book_name] += 1
            print("Your book has been returned successfully")

        else:
            print("Book not found in library")


    def total_books_in_library(self):
        print(f"Total books available in library is : {LibraryManagement.books_counter}")
    
    
l1 = LibraryManagement(1,"chammpak","ramkishan",10)
l1.display_available_books()

l1.issue_books()
l1.return_books()
l1.total_books_in_library()


