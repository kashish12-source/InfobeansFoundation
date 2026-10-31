#  Write a Java program to create class called "TrafficLight" with attributes for color and duration, and methods to change the color and check for red or green.
import time
class TrafficLight:
    def __init__(self,color):
        self.__color = color
        self.__duration = 5
        self.__colors = ["red","green","yellow"]
    
    def check_color(self):
        return self.__color
    
    def change_color(self):
        current_index = self.__colors.index(self.__color)

        next_index = (current_index+1)%len(self.__colors)

        self.__color = self.__colors[next_index]

    def run (self):
        count = 0 
        while(count<3):
            print("Traffic Light:" ,self.check_color())

            time.sleep(self.__duration)  #this will tell the python that you have to execute the code after the particular time 
            

            self.change_color()

            if self.__color =="red":
                count +=1
        print("Traffic light simmulation stopped ")

t1 = TrafficLight("yellow")
t1.run()



