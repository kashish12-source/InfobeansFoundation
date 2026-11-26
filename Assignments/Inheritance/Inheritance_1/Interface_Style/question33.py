# 33. Smart Home Devices

# Methods:

# turn_on()
# turn_off()

# Implement:

# SmartFan
# SmartLight
# SmartAC

from abc import ABC,abstractmethod
class Devices(ABC):
    @abstractmethod
    def turn_on():
        pass 

    @abstractmethod
    def turn_off():
        pass 

class SmartFan(Devices):
    def __init__(self,name ):
        self.__name = name
    
    def turn_on(self):
        print(f"The device {self.__name} is on")
    
    def turn_off(self):
        print(f"The device {self.__name} is off")


class SmartLight(Devices):
    def __init__(self,name ):
        self.__name = name
    
    def turn_on(self):
        print(f"The device {self.__name} is on")
    
    def turn_off(self):
        print(f"The device {self.__name} is off")
        

class SmartAC(Devices):
    def __init__(self,name ):
        self.__name = name
    
    def turn_on(self):
        print(f"The device {self.__name} is on")
    
    def turn_off(self):
        print(f"The device {self.__name} is off")
    
    

fan = SmartFan("Ceiling Fan")
light = SmartLight("LED Light")
ac = SmartAC("Air Conditioner")


print("--- Smart Fan ---")
fan.turn_on()
fan.turn_off()




print("\n--- Smart Light ---")
light.turn_on()
light.turn_off()

print("\n--- Smart AC ---")
ac.turn_on()
ac.turn_off()