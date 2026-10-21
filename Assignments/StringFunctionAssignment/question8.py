# 8. Remove all spaces from a string.
def remove_space(s):
    l = s.split()
    res = "".join(l)
    return res
s ="hello how are you "
print(remove_space(s))