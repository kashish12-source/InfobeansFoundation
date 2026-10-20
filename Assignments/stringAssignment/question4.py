# Count uppercase letters, lowercase letters, digits, and special characters.
s = "AbcdEfg12r63!@$%"
lc=0
sc=0
uc=0
dc=0
for i in s:
    if ord(i) >=65 and ord(i)<=90:
        uc+=1
    elif ord(i)>=97 and ord(i)<=122:
        lc+=1
    elif i.isdigit():
        dc+=1
    else:
        sc+=1
print(f"The string you give is : {s}")
print(f"The no. of lowercase letters is : {lc}")
print(f"The no. of uppercase letters is : {uc}")
print(f"The no. of digits is : {dc}")
print(f"The no. of special charaters is : {sc}")

