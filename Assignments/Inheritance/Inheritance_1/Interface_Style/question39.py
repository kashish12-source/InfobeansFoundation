# 39. Navigation System

# Methods:

# navigate()

# Implement:

# GoogleMaps
# AppleMaps



from abc import ABC,abstractmethod
class Navigation(ABC):
    @abstractmethod
    def navigate(self):
        pass 

class GoogleMap(Navigation):
    def __init__(self,from_place, destination):
        self.__from_place =from_place
        self.__destination =destination
    
    def navigate(self):
        print(f"you are traveling from {self.__from_place} to {self.__destination} ")

class AppleMap(Navigation):

        def __init__(self,from_place, destination):
            self.__from_place =from_place
            self.__destination =destination
    
        def navigate(self):
            print(f"you are traveling from {self.__from_place} to {self.__destination} ")
obj1 = GoogleMap("Indore", "Bhopal")

obj2 = AppleMap("Delhi", "Mumbai")

obj1.navigate()
obj2.navigate()