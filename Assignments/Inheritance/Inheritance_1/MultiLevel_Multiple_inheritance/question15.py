
class Player:
    def __init__(self, name, country):
        self.__name = name
        self.__country = country

    def get_name(self):
        return self.__name

    def get_country(self):
        return self.__country


class CricketPlayer(Player):

    def __init__(self, name, country, age, innings):
        super().__init__(name, country)
        self.__age = age
        self.__innings = innings

    def get_age(self):
        return self.__age

    def get_innings(self):
        return self.__innings

    def cricketer_details(self):
        print("ALL ABOUT THE CRICKETER")
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.__age}")
        print(f"Country: {self.get_country()}")
        print(f"Innings: {self.__innings}")


class Captain(CricketPlayer):

    def __init__(self, name, country, age, innings, price, toss):
        super().__init__(name, country, age, innings)
        self.__price = price
        self.__toss = toss

    def details(self):
        print("ALL ABOUT THE CAPTAIN")
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Country: {self.get_country()}")
        print(f"Innings: {self.get_innings()}")
        print(f"Price: {self.__price}")
        print(f"Tosses Won: {self.__toss}")


# CricketPlayer object
p = CricketPlayer("Virat", "INDIA", 35, 200)
p.cricketer_details()

print()

# Captain object
c = Captain("Rohit", "INDIA", 38, 250, 15, 10)
c.details()
