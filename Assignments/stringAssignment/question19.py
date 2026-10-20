# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
s =" Hello  "
d = {}
for i in s :
    if i!=" ":
        if i in d :
            d[i]+=1
        else:
            d[i]=1
print(d)
