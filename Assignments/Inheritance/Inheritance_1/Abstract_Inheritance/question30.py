# 30. Restaurant Management

# Abstract:

# Restaurant

# Derived:

# PizzaRestaurant
# BurgerRestaurant

# Prepare food differently.


from abc import ABC ,abstractmethod

collection = []
def add_to_collection(obj):
    collection.append(obj)

class Restaurant(ABC):

    @abstractmethod
    def validate_dish(self):
        pass 

    @abstractmethod
    def display_dish_details(self):
        pass 

    @abstractmethod
    def dish_recepie(self):
        pass 


class RegisterDish:
    def __init__(self,id ,type,name,origin_country,recepie):
        self.__id = id 
        self.__type = type 
        self.__name = name 
        self.__origin_country = origin_country
        self.__recepie = recepie

    def get_id(self):
        return self.__id 

    def get_details(self):
        return self.__type,self.__name,self.__origin_country

    def get_recepie(self):
        self.__recepie


class PizzaRestuarant(Restaurant):

    def __init__(self,id):
        self.__id =id 
        self.__validate_food = False 
        self.__obj = None 

    def validate_dish(self):
        for obj in collection:
            if obj.get_id() == self.__id :
                self.__validate_food =True
                self.__obj = obj 
                print("This dish is registered in the restaurant")
                return True
        print("The dish is not registered in the restaurant")
        return False

    def display_dish_details(self):
        if self.__validate_food:
            d_type,name,origin_country = self.__obj.get_details()
            print("\n=============================Pizza Details===============================\n")
            print(f"Name of the dish : {name }")
            print(f"Type of the dish : {d_type}")
            print(F"Origin country of the dish is : {origin_country}")
           
    

    def dish_recepie(self):
        if self.__validate_food:
            print("=============================Pizza Recepie===================================")
            recepie = self.__obj.get_recepie()
            print(recepie)
    


class BurgerRestuarant(Restaurant):

    def __init__(self,id):
        self.__id =id 
        self.__validate_food = False 
        self.__obj = None 

    def validate_dish(self):
        for obj in collection:
            if obj.get_id() == self.__id :
                self.__validate_food =True
                self.__obj = obj 
                print("This dish is registered in the restaurant")
                return True
        print("The dish is not registered in the restaurant")
        return False

    def display_dish_details(self):
        if self.__validate_food:
            d_type,name,origin_country = self.__obj.get_details()
            print("\n=============================Burger Details===============================\n")
            print(f"Name of the dish : {name }")
            print(f"Type of the dish : {d_type}")
            print(F"Origin country of the dish is : {origin_country}")
           
    

    def dish_recepie(self):
        if self.__validate_food:
            print("===============================Burger Recepie================================")
            recepie = self.__obj.get_recepie()
            print(recepie)



p1 = RegisterDish(101,"italian", "capsicum pizza", "italy","1. Take a pizza base.\n2. Spread pizza sauce evenly over the base.\n3. Chop capsicum, onion, and tomatoes into small pieces.\n4. Spread grated mozzarella cheese over the pizza base.\n5. Add chopped capsicum, onion, and tomatoes.\n6. Sprinkle oregano, chilli flakes, and black pepper.\n7. Add another layer of grated cheese.\n8. Preheat the oven to 180°C.\n9. Bake the pizza for 10-15 minutes until the cheese melts and the base becomes crispy.\n10. Remove the pizza from the oven and cut it into slices.\n11. Serve hot and enjoy your delicious capsicum pizza!")
    
p2 =RegisterDish(102,"italian","cheese corn", "italy","1. Take a pizza base.\n2. Spread pizza sauce evenly over the base.\n3. Boil sweet corn for 3-4 minutes and drain the water.\n4. Spread grated mozzarella cheese over the pizza base.\n5. Add boiled sweet corn evenly over the cheese.\n6. Add chopped capsicum and onion if desired.\n7. Sprinkle oregano, chilli flakes, and black pepper.\n8. Add another layer of grated cheese.\n9. Preheat the oven to 180°C.\n10. Bake the pizza for 10-15 minutes until the cheese melts and the base becomes crispy.\n11. Remove the pizza from the oven and cut it into slices.\n12. Serve hot and enjoy your delicious cheese corn pizza!"
)

b1 = RegisterDish(201,"german","aloo tikki burger ","germany","1. Boil 3-4 potatoes, peel them, and mash them in a bowl.\n2. Add salt, red chilli powder, garam masala, coriander powder, and chopped coriander leaves.\n3. Mix everything properly and shape the mixture into round patties.\n4. Coat the patties with breadcrumbs or cornflour.\n5. Heat oil in a pan and shallow fry the patties until golden brown and crispy on both sides.\n6. Take burger buns and cut them into two halves.\n7. Apply butter to both halves and toast them lightly on a pan.\n8. Spread mayonnaise, tomato ketchup, and green chutney on the inner sides of the buns.\n9. Place a lettuce leaf on the bottom half of the bun.\n10. Add a few onion rings and tomato slices.\n11. Place the crispy aloo tikki over the vegetables.\n12. Add a cheese slice and sprinkle some chaat masala.\n13. Cover it with the top half of the burger bun.\n14. Serve hot with French fries and enjoy your delicious homemade aloo tikki burger!")

b2 = RegisterDish(202,"german","cheese burger","germany", "1. Take a burger bun and cut it into two halves.\n2. Apply butter to both halves of the bun.\n3. Heat a pan and lightly toast the burger buns until golden brown.\n4. Take a veg or chicken patty and shallow fry it until crispy and golden brown.\n5. Spread mayonnaise and tomato ketchup on the inner sides of the burger buns.\n6. Place a lettuce leaf on the bottom half of the bun.\n7. Add sliced tomatoes and onion rings.\n8. Place the crispy patty over the vegetables.\n9. Add one or two cheese slices over the hot patty and allow them to melt slightly.\n10. Sprinkle some black pepper and oregano for extra flavour.\n11. Add another layer of mayonnaise if desired.\n12. Cover it with the top half of the burger bun.\n13. Serve hot with French fries and enjoy your delicious homemade cheese burger!")

add_to_collection(p1)
add_to_collection(p2)
add_to_collection(b1)
add_to_collection(b2)


pizza1 = PizzaRestuarant(101)
pizza2 = PizzaRestuarant(102)

burger1 = BurgerRestuarant(201)
burger2 = BurgerRestuarant(202)


print("\n====================== TEST PIZZA RESTAURANT ======================\n")

pizza1.validate_dish()
pizza1.display_dish_details()
pizza1.dish_recepie()

pizza2.validate_dish()
pizza2.display_dish_details()
pizza2.dish_recepie()


print("\n====================== TEST BURGER RESTAURANT ======================\n")

burger1.validate_dish()
burger1.display_dish_details()
burger1.dish_recepie()

burger2.validate_dish()
burger2.display_dish_details()
burger2.dish_recepie()