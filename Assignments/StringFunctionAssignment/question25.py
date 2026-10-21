# 25. Check whether a string contains only digits without using isdigit().
def only_digit(s):
    for i in s :
        if not i.isdigit():
            return False
    return True

s ="12331235"
if only_digit(s):
    print("yes")
else:
    print("No")