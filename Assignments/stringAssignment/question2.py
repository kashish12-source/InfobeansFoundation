# 2. Check whether a string is a palindrome.
s = "A1@b#c2c#b@A"
start = 0
end = len(s)-1
f = True
while(start<end):
    while not s[start].isalpha() and start<end:
        start+=1
    while not s[end].isalpha() and start<end:
        end-=1
    if s[start].lower() == s[end].lower():
        start+=1
        end-=1
    else:
        f = False
        break
        
if f:
    print("Is palindrome")
else:
    print("Not palindrome")
