# 4. Restaurant Billing System
# Beginner–Intermediate
# Concepts: Loops, conditions, functions
# Requirements
# •	Display a menu with item prices.
# •	Let customers select items and quantities.
# •	Calculate the running bill.
# •	Apply discounts based on the bill amount.
# •	Calculate the final bill, including tax.
# Bonus: Add coupon codes and repeat-order functionality.


def menu():
    items = {
        "Main Course":{
            "panner":{
                "Matar Panner":230,
                "Paneer Lababdar":235,
                "Shahi Panner":300,
                "Kaju panner":460,
                "kadhai panner":239,
                "Paneer Kolhapuri":450
            },
            "Dal":{
                "Plain Dal":120,
                "Fried Dal":200,
                "Dal Makhni":300,
                "Moong Dal":200,
                "Masur Dal":300
            },
            "Rice":{
                "Jeera Rice":200,
                "Pulao":239,
                "Plain Rice":120,
                "Biriyani":340
            },
            "Bread":{
                "Plain Tawa Roti":12,
                "Butter Tawa Roti":16,
                "Plain Tandori Roti":15,
                "Butter Tandori Roti":20,
                "Missi Roti":30,
                "Plain Parathe":35,
                "Lacche Parathe":40

            },
            "Papad":{
                "Roasted Papad":10,
                "Fried Papad":15
            },
            "Raita":{
                "Boondi Raita":130,
                "Cucumber Raita":150,
                "Aloo Raita":130
            }
        },
        "Chinees":{
            "Noodles":300,
            "Manchurian":200,
            "Momos":200,
            "Chinees Bhel":300,
            "Spring Rolls":300
        },
        "Dessert":{
            "Rassgulla":150,
            "Cakes":230,
            "MoongDal Halwa":300,
            "Rass Malai":200,
            "Rabdi":240,
            "Jalebi":200
        },
        "Drinks":{
            "Soft Drinks":{
            "Coke":140,
            "Sprite":290,
            "Monster":130,
            "Fanta":140}
            ,
            "Coffee":{
            "Esspresso":300,
            "Cold Coffee":230,
            "Cold Coffee + Icecream":390,
            "Late":230
        }
        }
    }
    return items

# choices = []

item = menu()
    
def select_items():
    choices = []
    categories = {
        1: "Main Course",
        2: "Dessert",
        3: "Chinees",
        4: "Drinks"
    }
    print()
    while True:
        print("\n1. Main Course")
        print("2. Desserts")
        print("3. Chinese")
        print("4. Drinks")
        print("5. Exit")
        print()
        choose = int(input("Enter category number: "))
        print()
        if choose == 5:
            break

        if choose not in categories:
            print("Invalid category")
            continue

        category = categories[choose]
        available = item[category]

        # Display items
        items = {}

        for name, price in available.items():
            if isinstance(price, dict):
                items.update(price)
            else:
                items[name] = price

        item_list = list(items.items())

        for i, (name, price) in enumerate(item_list, 1):
            print(f"{i}. {name} : Rs. {price}")
        print()
        item_no = int(input("Choose item number: "))
        print()
        if item_no < 1 or item_no > len(item_list):
            print("Invalid item number")
            continue

        quantity = int(input("Enter quantity: "))

        name, price = item_list[item_no - 1]
        cost = price * quantity
        choices.append(cost)
        print()
        print(f"{name} x {quantity} = Rs. {cost}")

    return choices

    


    # f = True
    # while(f):
    #     print("Press 1 for MainCourse")
    #     print("Press 2 for Desserts")
    #     print("Press 3 for Chinees")
    #     print("Press 4 for Drinks")
    #     print('Press 5 for exit')
    #     chooice = int(input("Enter you choice here : "))
    #     if chooice == 1:
    #         j=1
    #         for i in item.keys():
    #             print(f"Press {j} for : {item[i]}")
    #             j+=1
    #         print("Press 'y' for choose items ")
    #         print("Press 'x' for exit()")
            
    #         g= True
    #         while(g):
                
    #             n = input("Enter your choice here : ")
    #             print("choose the main ")
    #             choices.append(item[n])
    #             print("Press 2 for ")
                


def calculate_bill(choices):

    sum =0
    for i in choices:
        sum+=i
    return sum

def apply_discount(sum):
    if sum >=5000:
        # give discount of the 10 %
        x = sum
        sum = sum - (sum/10)
        if x == 5000:
            print(f"Your total bill is of 5000 so we give discount of 10% ")
            print(f"\nSo the final bill is {sum}")
        elif x >5000:
            print(f"Your total bill is greater than 5000 so we give discount of 10% ")
            print(f"\nSo the final bill is {sum}")
        
        
    elif 3000<=sum <5000:
       x =sum
       sum =sum - (sum/20)
       print("Your total bill is greater than 3000 so you get 5% of discount ")
       print(f"\nSo your final bill is : {sum}")
    else:
        print("You are not elidible for the discount ")
        print(f"\nSo the total is  : {sum}")


print("_______________________________________________________________________________________________________")
print()

print(f"\t\t\t\t\tWelcome To Taj")
print()

print("_______________________________________________________________________________________________________")

print("\n   Main Course:")
print("\n\t   Paneer:")
print("\t\tMatar Paneer :230")
print("\t\tPaneer Lababdar :235")
print("\t\tShahi Paneer :300")
print("\t\tKaju Paneer :460")
print("\t\tKadhai Paneer :239")
print("\t\tPaneer Kolhapuri :450")

print("\t   Dal:")
print("\t\tPlain Dal :120")
print("\t\tFried Dal :200")
print("\t\tDal Makhni :300")
print("\t\tMoong Dal :200")
print("\t\tMasur Dal :300")

print("\t   Rice:")
print("\t\tJeera Rice :200")
print("\t\tPulao :239")
print("\t\tPlain Rice :120")
print("\t\tBiriyani :340")

print("\t   Bread:")
print("\t\tPlain Tawa Roti :12")
print("\t\tButter Tawa Roti :16")
print("\t\tPlain Tandori Roti :15")
print("\t\tButter Tandori Roti :20")
print("\t\tMissi Roti :30")
print("\t\tPlain Parathe :35")
print("\t\tLacche Parathe :40")

print("\t   Papad:")
print("\t\tRoasted Papad :10")
print("\t\tFried Papad :15")

print("\t   Raita:")
print("\t\tBoondi Raita :130")
print("\t\tCucumber Raita :150")
print("\t\tAloo Raita :130")


print("\n   Desserts:")
print("\t\tRassgulla :150")
print("\t\tCakes :230")
print("\t\tMoongdal Halwa :300")
print("\t\tRass Malai :240")
print("\t\tRabdi :240")
print("\t\tJalebi :200")

print("\n   Chinees:")

print("\t\tNoodles :300")
print("\t\tManchurian :200")
print("\t\tMomos :200")
print("\t\tChinees Bhel :300")
print("\t\tSpring Roll :300")



print("\n   Drinks:")
print("\t   Soft Drinks:")
print("\t\tCoke :140")
print("\t\tSprite :290")
print("\t\tMonster :130")
print("\t\tFanta :140")


print("\t   Coffee:")
print("\t\tEsspresso :300")
print("\t\tCold Coffee :230")
print("\t\tCold Coffee + Icecream :390")
print("\t\tLatte :230")

print("_______________________________________________________________________________________________________")

choices = select_items()
total = calculate_bill(choices)
print(f"Your total price is : {total}")

apply_discount(total)
