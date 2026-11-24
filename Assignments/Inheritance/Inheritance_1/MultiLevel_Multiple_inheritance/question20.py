# 20. Gaming Characters
# Character
# Warrior
# SuperWarrior

# Add special powers.

collection = []

class Character:

    def __init__(self, c_id, c_name, c_features=None):
        self.__c_name = c_name
        self.__c_features = c_features if c_features is not None else []
        self.__c_id = c_id

    @property
    def get_c_features(self):
        return self.__c_features

    @property
    def get_c_name(self):
        return self.__c_name

    @property
    def get_c_id(self):
        return self.__c_id

    @classmethod
    def add_to_collection(cls, obj):
        collection.append(obj)


class Warrior(Character):

    warrior_collection = []

    def __init__(self, obj):
        super().__init__(
            obj.get_c_id,
            obj.get_c_name,
            obj.get_c_features
        )

    @classmethod
    def find_warriors(cls):
        cls.warrior_collection.clear()

        for obj in collection:
            if "warrior" in obj.get_c_features:
                cls.warrior_collection.append(cls(obj))

    @classmethod
    def display_warriors(cls):
        if cls.warrior_collection:
            for obj in cls.warrior_collection:
                print(obj.get_c_id, obj.get_c_name)
        else:
            print("No warrior available")


class SuperWarrior(Warrior):

    super_warrior_collection = []

    @classmethod
    def check_superwarrior(cls):
        cls.super_warrior_collection.clear()

        s_features = ['cute', 'kind', 'powerful']

        for obj in cls.warrior_collection:
            if all(feature in obj.get_c_features for feature in s_features):
                cls.super_warrior_collection.append(cls(obj))

    @classmethod
    def display_super_warrior(cls):
        if cls.super_warrior_collection:
            for obj in cls.super_warrior_collection:
                print(obj.get_c_name, obj.get_c_id)
        else:
            print("No SuperWarrior available")


# Creating characters

c = Character(101, "nazuko",
              ["beautiful", "cute", "small", "demon"])

c1 = Character(102, "naruto",
               ["powerful", "cute", "kind", "big", "ninja", "warrior"])

c2 = Character(103, "akaza",
               ["mysterious", "cute", "dangerous", "small", "demon"])

c3 = Character(104, "inouske",
               ["powerful", "cute", "kind", "big", "ninja", "warrior"])


# Adding characters to collection

Character.add_to_collection(c)
Character.add_to_collection(c1)
Character.add_to_collection(c2)
Character.add_to_collection(c3)


# Finding warriors

Warrior.find_warriors()
Warrior.display_warriors()


# Finding super warriors

SuperWarrior.check_superwarrior()
SuperWarrior.display_super_warrior()
