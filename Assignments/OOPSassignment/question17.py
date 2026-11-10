# 17. Write a Java program to create a class called "Movie" with attributes for title, director, actors, and reviews, and methods for adding and retrieving reviews.
class Movie:
    def __init__(self,title,director,actors,reviews):
        self.__title= title
        self.__director = director
        self.__actors=actors
        self.__collection={}
        self.__reviews=[reviews]
    
    def add_movie(self):
        self.__collection[self.__title] = self.__reviews
        print("Movie added successfully")

    def delete_movie(self):
        if self.__title in self.__collection:
            del self.__collection[self.__title]
            print("Movie deleted successfully")
        else:
            print("Movie not found")
                    

    def adding_reviews(self):
        print("Press 1 for excillent\nPress 2 for Very Good\nPress 3 for Good\nPress 4 for Normal\nPress 5 for Bad\n")

        choice = int(input("Enter your choice here : "))

        
        match choice:
                case 1:
                    self.__reviews.append("Excillent")
                    print("Review has been added ")
                    

                case 2:
                    self.__reviews.append("Very Good")
                    print("Review has been added ")
                case 3:
                    self.__reviews.append("Good")
                    print("Review has been added ")
                case 4 :
                    self.__reviews.append("Normal")
                    print("Review has been added ")
                case 5:
                    self.__reviews.append("Bad")
                    print("Review has been added ")
                case _:
                    print("Enter the valid choice ")
                    return
        self.__collection[self.__title] = self.__reviews
        print("Review has been added successfully")

            
    
    def retrieving_reviews(self):
        movie = input("Enter a movie here: ")

        if movie in self.__collection:
            for review in self.__collection[movie]:
                print(review)
        else:
            print("Movie not found")
        
m1 = Movie("dhurandar","Sanjay leela bhansali","Deepika","Good")
m1.add_movie()
m1.adding_reviews()
m1.adding_reviews()
m1.adding_reviews()
m1.retrieving_reviews()