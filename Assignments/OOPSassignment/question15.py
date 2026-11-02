# 15. Write a Java program to create a class called "MusicLibrary" with a collection of songs and methods to add and remove songs, and to play a random song.
import random

from datetime import datetime
class MusicLibrary:
    def __init__(self):
        self.__collections =[]
        self.__duration = 3

    def add_songs(self,song):
        self.__collections.append(song)
        print(f"Song: '{song}' added successfully")


    def remove_songs(self,song):
        if song in self.__collections:
            self.__collections.remove(song)
            print("song has been removed successfully")


        else:
            print("song not found")

    def paly_songs(self):
        time = 20
        if not self.__collections:
            print("No songs available in the library")
            return

        print("Press 1 to play a random song")
        print("Press 2 to stop playing")

        while True:
            n = int(input("Enter your choice: "))

            if n==1:
                song = random.choice(self.__collections)
                print("Now playing:", song)


            elif n == 2:
                print("Music stopped")
                break

            else:
                print("Invalid choice")

s1 = MusicLibrary()
s1.add_songs("fitoor")
s1.add_songs("aap ki kashish")
s1.add_songs("nazzam")
s1.add_songs("alfaaz")
s1.remove_songs("nazzam")
s1.paly_songs()
