# 19. Mobile Phone Hierarchy
# Phone
# Smartphone
# AndroidPhone

# Add Android features.

class Phone:
    __collection = {}

    def __init__(self, c_name, min_range, max_range):
        self.__c_name = c_name
        self.__min_range = min_range
        self.__max_range = max_range

        Phone.__collection[self.__c_name] = {
            "min range": self.__min_range,
            "max range": self.__max_range
        }

    def get_c_name(self):
        return self.__c_name

    def check_company(self, name):
        return name in Phone.__collection

    def check_range(self, price, name):
        if name in Phone.__collection:
            if (price >= Phone.__collection[name]["min range"]
                    and price <= Phone.__collection[name]["max range"]):
                return True
        return False


class SmartPhone(Phone):

    def __init__(self, c_name, price, storage):
        self.__c_name = c_name
        self.__price = price
        self.__storage = storage

    def get_c_name(self):
        return self.__c_name

    def check_phone(self):
        if self.check_company(self.__c_name):
            if self.check_range(self.__price, self.__c_name):
                print(f"This smartphone is in your budget range and has {self.__storage} storage")
                return True
            else:
                print("The phone is not available in the given budget range")
                return False
        else:
            print("We don't have mobile phones of this company")
            return False


class AndroidPhone(SmartPhone):

    def __init__(self, c_name, price, storage, model):
        super().__init__(c_name, price, storage)
        self.__model = model

    def billing(self):
        if self.check_phone():
            print("\n__________ BILLING DETAILS __________")
            print(f"Company: {self.get_c_name()}")
            print(f"Model: {self.__model}")
            print("Payment successful!")
            print("Thank you for shopping!")


p1 = Phone("Samsung", 10000, 80000)
p2 = Phone("Apple", 50000, 150000)

a1 = AndroidPhone("Samsung", 45000, "256 GB", "S24")

a1.billing()
