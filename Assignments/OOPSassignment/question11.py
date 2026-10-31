# 11. Write a Java program to create a class called "Library" with a collection of books and methods to add and remove books.

class Library:

    def __init__(self):
        self.collection_of_books =[]
    
    def add_books(self,name):
        self.collection_of_books.append(name)
        print("Book added successfully")
    
    def remove_books(self,name):
        if name in self.collection_of_books:
            self.collection_of_books.remove(name)
            print("Book removed successfully")
        else:
            print("Book not found ")
        
    def display_collection(self):
        k = 1
        for i in range(len(self.collection_of_books)):
            print(f"{k}.{self.collection_of_books[i]}")
            k+=1
    
b1 = Library()
b1.add_books("champak")
b1.add_books("twisted love")
b1.add_books("rom com")
b1.add_books("it ends with us")
b1.add_books("twisted games ")
b1.display_collection()

b1.remove_books("champak")
b1.display_collection()