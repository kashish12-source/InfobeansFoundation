# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

def reverse_word(s):
    l = s.split()
    res =""
    for i in l:
        word = list(i)
        start =0
        end = len(word)-1
        while(start<end):
            word[start],word[end] = word[end],word[start]
            start+=1
            end-=1
        res += "".join(word)
        res += " "
    return res

s ="python is easy"
print(f"The reverse_word of the give string '{s}' is : {reverse_word(s)} ")
