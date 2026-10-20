# Count the number of vowels and consonants in a string.
s = "abcdefioujklmsno"
vowel = "aeiouAEIOU"
count = 0
for i in s:
    if i in vowel:
        count+= 1
print(f"The no. of vowels present in the string is : {count }")
