# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
def count_freq(s):
    d ={}
    for i in s :
        if i in d:
        
            d[i]+=1
        else:
            d[i]=1
    return d
s ="kashish"
res = count_freq(s)
for i in res.keys():
    print(f"The charcter is : {i} , and it's frequency is : {res[i]}")
    
