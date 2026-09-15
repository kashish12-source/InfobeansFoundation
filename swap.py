a = int ( input ( "enter the first number : "))
b = int ( input ("enter the second number : "))

print(f"Before swap a is : {a} and b is : {b}")

a = a^b
b = a^b
c = a^b

print(f"After swap a is : {a} and b is : {b}")
