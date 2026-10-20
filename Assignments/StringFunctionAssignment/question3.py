# 3. Count the number of vowels and consonants in a string.
def check_vowel_consonants(s):
    s=s.lower()
    vc=0
    cc=0
    vowel = "aeiou"
    for i in s:
        if i.isalpha():
            if i in vowel:
                vc+=1
            else:
                cc+=1
    return (vc, cc)
s = "abdafbbbbccdeio"
print(check_vowel_consonants(s))
