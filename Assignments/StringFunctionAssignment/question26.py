# 26. Find the longest word in a sentence.
def longest_word(s):
    d ={}
    s =s.strip()
    l = s.split()
    for i in l :
        d[i]=len(i)
    max =0
    res=""
    for i in d.keys():
        if d[i]>max:
            max = d[i]
            res =i
    return max ,res


s ="Hello everyone how are you all "
max , res = longest_word(s)
print(f"The longest word in the string '{s}' is : '{res}' with length {max}")
