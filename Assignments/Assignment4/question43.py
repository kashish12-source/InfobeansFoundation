# 43) WAP to convert binary number into decimal number
n = int(input("Enter binary number: "))

result = 0
power = 0

while n > 0:
    digit = n % 10
    decimal = result + digit * (2 ** power)
    power += 1
    n = n // 10

print(result)