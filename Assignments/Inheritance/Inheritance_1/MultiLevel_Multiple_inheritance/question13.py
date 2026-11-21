
# 13. Smart Device System
# Device
# SmartDevice(Device)
# SmartTV(SmartDevice)


class Device :
    
    def __init__(self,brand_name,experience):
        self.__brand_name = brand_name
        self.__experience = experience

    def get_device_details(self):
        return self.__brand_name,self.__experience

class SmartDevice(Device):

    def __init__(self,brand_name , experience , management ,size  ):
        super().__init__(brand_name,experience)

        self.__management = management
        self.__size = size 

    
    def get_smart_device_details(self):
        return self.__management,self.__size 

    
class SmartTV(SmartDevice):

    def __init__ (self, brand_name ,experience, management,size,automation):
        super().__init__(brand_name , experience,management,size)

        self.__automation =automation

    def display(self):
        brand_name,experience = self.get_device_details()
        management,size = self.get_smart_device_details()
        print("___________Details___________")
        print(f"NAME :{brand_name}\nExperience : {experience} years \nMANAGEMENT : {management}\nSIZE :{size} inches \nAUTOMATION : {self.__automation}")

        print("____________________________")
        
s = SmartTV("Samasung",24,"manual and automation both","56","yes")
s.display()
