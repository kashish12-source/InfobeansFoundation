# 12. Write a Java program to create a class called "Airplane" with a flight number, destination, and departure time attributes, and methods to check flight status and delay.

from datetime import datetime
class Airplane:
    def __init__(self , flight_num , destination, dep_time):
        self.__flight_num = flight_num
        self.__destination = destination
        self.__dep_time = datetime.strptime(
            dep_time, "%Y-%m-%d %H:%M"
        )
    def check_status(self):
        current_time = datetime.now()
        if current_time == self.__dep_time:
            print("Flight reached the Airport")
        elif current_time >  self.__dep_time:
            print("Flight is a bit late")
        else :
            print("Flight reached airport before time ")

    def check_delay(self):
        current_time = datetime.now()
        if current_time > self.__dep_time:
            print(f"Flight is delayed by : {current_time - self.__dep_time}")
        elif current_time == self.__dep_time:
            print(f"Flight is on time ")
        else:
            print("Flight is before time ")

f1 = Airplane(101, "Bhopal", "2026-10-31 00:30")

f1.check_status()
f1.check_delay()