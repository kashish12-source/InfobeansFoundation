# 5. Count the number of words in a sentence.
s = "    Hello dear     I am kashish how  are you     "
count = 0

if s and s[0] != " ":
    count = 1

for i in range(len(s) - 1):
    if s[i] == " " and s[i+1] != " ":
        count += 1

print(count)
    