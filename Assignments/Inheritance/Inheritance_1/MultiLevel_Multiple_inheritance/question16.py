# 16. E-commerce User Roles
# User
# Seller(User)
# PremiumSeller(Seller)

# Add premium benefits.

class User : 
    def __init__(self,name,age,identity ,gender ):
        self.__name = name 
        self.__age = age 
        self.__identity = identity
        self.__gender = gender 

    def get_user_details(self):
        return self.__name,self.__age,self.__identity,self.__gender 
    

class Seller(User):
    def __init__(self,name ,age,identity ,gender ,gst_no,account_no):
        super().__init__(name,age,identity,gender)
        self.__gst_no = gst_no
        self.__account_no = account_no
    
    def get_seller_details(self):
        return self.__gst_no,self.__account_no

    

class PremiumSeller(Seller):
    def __init__(self, name ,age ,identity,gender ,gst_no,account_no, vip_id):
        super().__init__(name,age,identity,gender,gst_no,account_no)
        self.__vip_id = vip_id

    def details(self):
        name ,age,identity,gender = self.get_user_details()
        gst_no,account_no = self.get_seller_details()

        print(f"Name : {name}")
        print(f"Age : {age}")
        print(f"Indentity : {identity}")
        print(f"Gender : { gender}")
        print(f"GST Number : {gst_no}")
        print(f"Accoun Number : {account_no}")
        print(f"VIP Id : {self.__vip_id}")

p = PremiumSeller("Kashish" ,20,"Adhar" ,"Female",10232032,4560003234,1002)
p.details()
