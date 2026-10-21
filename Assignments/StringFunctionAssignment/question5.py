# 5. Count the number of words in a sentence.

def count_words(s):
    count = 0
    if s and s[0]!=" ":
        count = 1

    for i in range(len(s)-1):
        if s[i]==" " and s[i+1] != " ":
            count +=1
    return count 




s = "   hello how are    you hope you are doing well    "
res= count_words(s)
print(res)