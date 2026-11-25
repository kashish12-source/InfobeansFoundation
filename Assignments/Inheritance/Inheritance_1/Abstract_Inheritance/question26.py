# 26. Media Player

# Abstract:

# MediaPlayer

# Derived:

# AudioPlayer
# VideoPlayer

# Implement play functionality.

from abc import ABC ,abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def quality(self):
        pass 

    @abstractmethod
    def speed(self):
        pass 

    @abstractmethod
    def validate_media(self):
        pass 

collection =[]
def add_to_collection (obj):
    collection.append(obj)
    print("Media added successfully")

class Media:
    def __init__(self,id, quality ,speed):
        self.__id = id 
        self.__quality = quality
        self.__speed = speed
        
    
    def get_id(self):
        return self.__id

    def get_quality (self):
        return self.__quality
    
    def get_speed(self):
        return self.__speed

class AudioPlayer(MediaPlayer):
    def __init__(self,id):
        self.__validate_id =False
        self.__id = id 
        self.__obj = None

    def validate_media(self):
        for obj in collection :
            if obj.get_id() == self.__id:
                self.__validate_id = True
                print("media validation is successfull")
                self.__obj = obj
                return True
        print("Media is not validated")
        return False

    def quality(self):
        if self.__validate_id:
            print(f" The quality of the media is : {self.__obj.get_quality()}")

    def speed(self):
        if self.__validate_id:
            print(f" The speed of the media is : {self.__obj.get_speed()}")



class VideoPlayer(MediaPlayer):
    def __init__(self,id):
        self.__validate_id =False
        self.__id = id 
        self.__obj = None

    def validate_media(self):
        for obj in collection :
            if obj.get_id() == self.__id:
                self.__validate_id = True
                print("media validation is successfull")
                self.__obj = obj
                return True
        print("Media is not validated")
        return False

    def quality(self):
        if self.__validate_id:
            print(f" The quality of the media is : {self.__obj.get_quality()}")

    def speed(self):
        if self.__validate_id:
            print(f" The speed of the media is : {self.__obj.get_speed()}")
            

m1 = Media(101, "HD", "1.5x")
m2 = Media(102, "4K", "2x")

add_to_collection(m1)
add_to_collection(m2)

a = AudioPlayer(101)

a.validate_media()
a.quality()
a.speed()









