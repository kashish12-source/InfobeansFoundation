# 2. Check whether a string is a palindrome.
def check_palindrome(s):
    s = s.lower()
    left =0
    right = len(s)-1
    while(left<right):
        if s[left] != s[right]:
            return False
        else:
            left +=1
            right -=1
    return True

s ="nitdfain"
if check_palindrome(s):
    print("Is palindrome")
else:
    print("Not palindrome")