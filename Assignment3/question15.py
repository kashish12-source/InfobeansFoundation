price = int (input("enter the price of the bike here : "))

if price > 100000:
    print(f"the road tax of the bike is : {price*0.15}")

elif price > 50000 and price <= 100000:
    print(f"the road tax of the bike is : {price*0.10}")
elif price <= 50000:
    print(f"the road tax of the bike is : {price*0.05}")
else:
    print("invalid input")