# 9. Find the first and last character of a string.
def Fist_last_char(s):
    start =0
    end = len(s)-1
    while(s[start]==" "):
        start +=1 
    while(s[end] == " "):
        end -=1
    return s[start],s[end]

s ="   adfakjdhoa   adfadf "
a,b = Fist_last_char(s)
print(f"The first and the last char is : {a} and {b}")
