# 5. Write a Java program to create a class called "Book" with attributes for title, author, and ISBN, and methods to add and remove books from a collection.

class Book :
    def __init__(self , title, author , ISBN):
        self.__title = title 
        self.__author = author 
        self.__ISBN = ISBN

    def display (self):
        print(f"Title : {self.__title}\nAuthor : {self.__author}\nISBN : {self.__ISBN}")
    
    collections= []
    
    def add_book (self):
        
        Book.collections.append(self.__ISBN)
        print(f"{self.__title} is added")


    def set_title(self,title):
        self.__title = title

    def set_author(self,author):
        self.__author = author 

    def get_title(self):
        print(self.__title)
    
    def get_author (self):
        print(self.__author)


    def remove_book(self):
        if self.__ISBN in Book.collections:
            Book.collections.remove(self.__ISBN)
            print(f"{self.__title} is removed from the collection")

        else:
            print(f"{self.__title} is not present in the collection")


book1 = Book("champak","Ram",123)
book2=Book("chatur","rajesh", 124)
book3 = Book("Twisted Love " , "Anna",125)
book1.add_book()
book2.add_book()
book3.add_book()


book2.remove_book()
