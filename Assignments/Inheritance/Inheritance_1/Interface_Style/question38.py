# 38. File Compression Tool

# Methods:

# compress()

# Implement:

# ZIPCompression
# RARCompression

from abc import ABC, abstractmethod

data = {}

def add_to__collection(obj, id):
    data[id] = obj


class Compression(ABC):

    @abstractmethod
    def compress(self):
        pass


class ZipCompression(Compression):

    def __init__(self, id, content):
        self.__id = id
        self.__content = content

    def compress(self):
        print("The content is compressed using ZIP")

    def display(self):
        for key, val in data.items():
            if key == self.__id:
                print(val.__content)


class RARCompression(Compression):

    def __init__(self, id, content):
        self.__id = id
        self.__content = content

    def compress(self):
        print("The content is compressed using RAR")

    def display(self):
        for key, val in data.items():
            if key == self.__id:
                print(val._RARCompression__content)


obj1 = ZipCompression(1, "Hello Python")
obj2 = RARCompression(2, "Hello World")

add_to__collection(obj1, 1)
add_to__collection(obj2, 2)

obj1.compress()
obj2.compress()

obj1.display()
obj2.display()
