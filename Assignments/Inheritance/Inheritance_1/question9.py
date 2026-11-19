'''
Library Managment 
 parent - Library item
 child - book, magazine, newspaper
 implement borrowing system
'''

from abc import ABC ,abstractmethod

class LibraryItems(ABC):
    @abstractmethod
    def display(self):
        pass 
    @abstractmethod
    def issue(self):

        pass 

    @abstractmethod
    def return_book(self):
        pass 


class Books(LibraryItems):
    __collection ={}
    def __init__(self, name , id, author,quantity ):
        self.__name= name 
        
        self.__author = author
        self.__quantity = quantity
        
        Books.__collection[self.__name]={ "author":self.__author,"quantity":self.__quantity}
    def display(self):
        for key , val in Books.__collection.items():
            print(f"{key}:{val}")

    def issue(self):
        name = input("Enter the name of the book you want to issuse here : ")
        if name in Books.__collection:
            quantity = int(input("Enter the no. of books you need : "))
            if quantity <Books.__collection[name]["quantity"]:
                print("book issued successfully")
                Books.__collection[name]["quantity"] -= quantity
            else:
                print("Quantity of the books are not enough to be issued ")
        else:
            print("Book not found ")

    def return_book(self):
        name = input("Enter the name of the book you want to return here : ")
        if name in Books.__collection:
            quantity = int(input("Enter the no. of books you want to return "))
            if quantity< ( Books.__collection[name]["quantity"]+quantity):
                Books.__collection[name]["quantity"]+=quantity
                print("Book is returned successfully")
            else:
                print("Their is no record that you have issued this book")

        else:
            print("book not found ")


class NewsPaper(LibraryItems):
    __collection ={}
    def __init__(self, name,quantity ):
        self.__name= name 
        self.__quantity = quantity
        NewsPaper.__collection[self.__name]={"quantity":self.__quantity}
    def display(self):
        for key , val in NewsPaper.__collection.items():

            print(f"{key}:{val}")

    def issue(self):
        name = input("Enter the name of the news paper here : ")
        name = name.strip()

        if name in NewsPaper.__collection:
            quantity = int(input("Enter the no. of newspaper you want to issue need : "))
            if quantity <NewsPaper.__collection[name]["quantity"]:
                print("newspaper issued successfully")
                NewsPaper.__collection[name]["quantity"] -= quantity
            else:
                print("Quantity of the newspaper are not enough to be issued ")
        else:
            print("Newspaper not found ")

    def return_book(self):
        name = input("Enter the name of the newspaper you want to return here : ")
        if name in NewsPaper.__collection:
            quantity = int(input("Enter the no. of newspaper you want to return "))
            if quantity < (NewsPaper.__collection[name]["quantity"]+quantity):
                NewsPaper.__collection[name]["quantity"]+=quantity
                print("newspaper is returned successfully")
            else:
                print("Their is no record of your's that you issued this newspaper")
        else:
            print("newspaper not found ")

class Magzine(LibraryItems):
    __collection ={}
    def __init__(self, name,quantity,writer ):
        self.__name= name 
        self.__writer=writer
        self.__quantity = quantity
        Magzine.__collection[self.__name]={ "writer":self.__writer,"quantity":self.__quantity}
    def display(self):
        for key , val in self.__collection.items():
            print(f"{key}:{val}")

    def issue(self):
        name = input("Enter the name of the magzine here : ")
        name = name.strip()

        if name in Magzine.__collection:
            quantity = int(input("Enter the no. of Magzine you need : "))
            if quantity <Magzine.__collection[name]["quantity"]:
                print("Magzine issued successfully")
                Magzine.__collection[name]["quantity"] -= quantity
            else:
                print("Quantity of the Magzine are not enough to be issued ")
        else:
            print("Magzine not found ")

    def return_book(self):
        name = input("Enter the name of the Magzine you want to returnhere : ")
        if name in Magzine.__collection:
            quantity = int(input("Enter the no. of Magzine you want to return "))
            if quantity < (Magzine.__collection[name]["quantity"]+quantity):
                Magzine.__collection[name]["quantity"]+=quantity
                print("Magzine is returned successfully")
            else:
                print('Their is no record shown that you have issued this magzine')
        else:
            print("Magzine not found ")
            


print("First we check the object of the Book class \n")

b1 = Books("champak",101,"ramcharan",123)
b2 =Books("chetak",102,"shivajniva",234)
b1.display()
b1.issue()
b1.return_book()
print("\nNow we check the object of the class Newspaper\n")
n1 = NewsPaper("dainikBhaskar",100)
n2 = NewsPaper("agnibaan",120)
n3 = NewsPaper("Timeofindia",390)
n1.display()
n1.issue()
n1.return_book()

print("\nNow we check the object of the class Magzine ")
m1 = Magzine("times", 23,"koshiki")
m1.display()
m1.issue()
m1.return_book()


