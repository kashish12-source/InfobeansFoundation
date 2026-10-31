# we have the class time in which we have the properties like - hr , sec ,min 
# now we have to return the addition of the two time objects i.e - t1,t2

class Time:
    def __init__(self , hr ,min ,sec):
        self.__hr = hr
        self.__min = min
        self.__sec = sec 

    def add (self , t1,t2):
        temp = Time(0,0,0)
        temp.__hr = self.__hr + t1.__hr +t2.__hr
        temp.__min = self.__min + t1.__min + t2.__min
        temp.__sec = self.__sec +t1.__sec + t2.__sec

        if temp.__sec >=60:
            x = temp.__sec 
            
            temp.__min+=temp.__sec //60
            temp.__sec = x%60
        if temp.__min >=60:
            x = temp.__min

            temp.__hr += temp.__min//60
            temp.__min = x%60

        return temp






    def display(self):
        print(f"{self.__hr} : {self.__min} : {self.__sec}")

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
t3 = Time(0,0,0)
t4 = t3.add(t1,t2)
t4.display()
