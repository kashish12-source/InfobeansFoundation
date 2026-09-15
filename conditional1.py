# a= int (input(f"enter the 1st value "))
# b = int (input(f"enter the 2nd value "))

# print(f"first value is greater : {a}")if a>b else print(f"second value is greater : {b}")

'''
a = int (input(f"enter the 1st value "))
b = int (input(f"enter the 2nd value "))
c = int (input(f"enter the 3rd value "))

max = a if a>b else b
print ("third is greater ")if(max<c) else print("max is greater ")
'''

a = int (input(f"enter the 1st value "))
b = int (input(f"enter the 2nd value "))
c = int (input(f"enter the 3rd value "))

print(f"first value is greater {a}") if a>b and a>c else print(f"second value is greater {b}") if b>c else print(f"thrid vlaue is greater {c}")