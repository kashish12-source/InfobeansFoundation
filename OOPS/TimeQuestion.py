# we have the class time in which we have the properties like - hr , sec ,min 
# now we have to return the addition of the two time objects i.e - t1,t2

class Time:
    def __init__(self , hr ,min ,sec):
        self.__hr = hr
        self.__min = min
        self.__sec = sec 

    def add (self , t1,t2):
        temp = Time(0,0,0)
        


    def display(self):
        pass 

    def set_hr(self ,hr):
        self.__hr = hr 

    def set_min(self , min):
        self.__min = min

    def set_sec (self,sec):
        self.__sec = sec 

    def get_hr(self):
        return self.__hr

    def get_min(self):
        return self.__min

    def get_sec(self):
        return self.__sec


t1 = Time(2,23,30)
t2 = Time(3,40,54)
t3 = Time(4,23,60)
t4 = t3.add(t1,t2)
t4.display()
