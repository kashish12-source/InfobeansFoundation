# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

def remove_duplicate(s):
    d ={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    res ="".join(d.keys())
    return  res

    
s ="programming"
print(remove_duplicate(s))

