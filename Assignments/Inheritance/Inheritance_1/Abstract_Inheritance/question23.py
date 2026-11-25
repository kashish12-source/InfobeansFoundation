# 23. Notification System

# Abstract:

# Notification

# Derived:

# EmailNotification
# SMSNotification
# PushNotification

from abc import ABC ,abstractmethod

class Notification(ABC):

    @abstractmethod
    def notification_sent(self):
        pass 

    @abstractmethod
    def validate_reciver(self):
        pass 

    @abstractmethod
    def validate_user(self):
        pass 


email_collection = []
def add_to_collection(obj):
    email_collection.append(obj)
    print("Email added successfully")


sms_collection = []

def add_to_sms_collection(obj):
    sms_collection.append(obj)


class CreateUser:
    def __init__(self,reciver,email,contact):
        self.__reciver = reciver 
        self.__email =email
        self.__contact = contact

    def get_email (self):
        return self.__email
    
    def get_reciver(self):
        return self.__reciver

    def get_contact(self):
        return self.__contact


class EmailNotification(Notification):

    def __init__(self, email, reciver, message):
        self.__email = email
        self.__reciver = reciver
        self.__message = message
        self.__valid_reciver = False
        self.__valid_user = False

    def validate_user(self):
        for obj in email_collection:
            if obj.get_email() == self.__email:
                print("Your credentials are valid")
                self.__valid_user = True
                return True

        self.__valid_user = False
        print("Your credentials are not valid")
        return False

    def validate_reciver(self):
        for obj in email_collection:
            if obj.get_email() == self.__reciver:
                print("Your receiver id is valid")
                self.__valid_reciver = True
                return True

        self.__valid_reciver = False
        print("Your receiver id is not valid")
        return False

    def notification_sent(self):
        if self.__valid_reciver and self.__valid_user:
            print(f"Notification sent successfully to {self.__reciver}")
            print(f"Message: {self.__message}")
        else:
            print("Notification is not sent")


class SMS(Notification):
    def __init__(self,contact,r_contact,message):
        self.__contact = contact
        self.__r_contact =r_contact
        self.__message = message
        self.__valid_sender = False
        self.__valid_reciver = False

    def validate_reciver(self):
        for obj in sms_collection:
            if obj.get_contact() == self.__r_contact:
                print("Reciver is valid ")
                self.__valid_reciver = True
                return True
        
        print("Reciver is not valid")
        return False
    
    def validate_user(self):
        for obj in sms_collection:
            if obj.get_contact() == self.__contact:
                print("Sender is valid")
                self.__valid_sender = True
                return True

        print("Sender is not valid ")
        return False
    
    def notification_sent(self):
        if self.__valid_sender and self.__valid_reciver:
            print("Message sent successfully")
            print({self.__message})
        else:
            print("Notification has not been sent")

class PushNotification(Notification):
    def __init__(self, sender, receiver, msg_type):
        self.__sender = sender
        self.__receiver = receiver
        self.__msg_type = msg_type

        self.__valid_sender = False
        self.__valid_receiver = False

    def validate_reciver(self):
        self.__valid_receiver = False

        if self.__msg_type == "sms":
            for obj in sms_collection:
                if obj.get_contact() == self.__receiver:
                    print("Valid receiver")
                    self.__valid_receiver = True
                    return True

        elif self.__msg_type == "email":
            for obj in email_collection:
                if obj.get_email() == self.__receiver:
                    print("Valid receiver")
                    self.__valid_receiver = True
                    return True

        else:
            print("Invalid notification type")
            return False

        print("Invalid receiver")
        return False

    def validate_user(self):
        self.__valid_sender = False

        if self.__msg_type == "sms":
            for obj in sms_collection:
                if obj.get_contact() == self.__sender:
                    print("Valid sender")
                    self.__valid_sender = True
                    return True

        elif self.__msg_type == "email":
            for obj in email_collection:
                if obj.get_email() == self.__sender:
                    print("Valid sender")
                    self.__valid_sender = True
                    return True

        else:
            print("Invalid notification type")
            return False

        print("Invalid sender")
        return False

    def notification_sent(self):
        if self.__valid_sender and self.__valid_receiver:
            print("Notification sent successfully")
        else:
            print("Notification is not sent")


c =CreateUser("kashish","kashishvishnoi2006@gmail.com", 7489619180)
c1 = CreateUser("koshiski", "koshiki@gmail.com",7898894532)
add_to_collection(c1)
add_to_sms_collection(c1)
add_to_sms_collection(c)
add_to_collection(c)
e = EmailNotification("kashishvishnoi2006@gmail.com","koshiki@gmail.com","hello koshiki")
e.validate_user()
e.validate_reciver()
e.notification_sent()
print()

print("=============================check SMS notification================================\n")

s = SMS(7489619180,7898894532,"sms")
s.validate_user()
s.validate_reciver()
s.notification_sent()


print()

print("=============================check PUSH notification================================\n")

p= PushNotification(7489619180,7898894532,"sms")
p.validate_user()
p.validate_reciver()
p.notification_sent()




