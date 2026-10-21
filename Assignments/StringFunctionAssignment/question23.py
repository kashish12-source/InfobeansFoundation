# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"

def reverse_order(s):
    
    l = s.split()
    res =""
    for i in range(len(l)-1,0,-1):
        res+=l[i]
        res+=" "
    res+=l[0]
    return res

s ="python is easy"
print(f"The reverse order for the string '{s}' is : {reverse_order(s)}")
