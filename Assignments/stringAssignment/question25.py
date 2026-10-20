# 25. Check whether a string contains only digits without using isdigit().
s ="213214234a614"
f =False
for i in s :
    if ord(i)>=48 and ord(i)<=57:
        f = True
    else:
        f=False
        break
if f:
    print("contain only digits")
else:
    print("does not have only digits ")
