# 21. Find the most frequent character in a string.
def most_frequent(s):
    d={}
    for i in s :
        if  i in d:
            d[i]+=1
        else:
            d[i]=1
    max = 0
    res = ""
    for i in d.keys():
        if d[i]>max:
            max = d[i]
            res = i
    return max , res


s = "kashishhhh"
max,res = most_frequent(s)
print(f"The character with  max freq is : {res} repetated {max} times")