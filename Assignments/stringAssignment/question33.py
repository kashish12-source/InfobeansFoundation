# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False
s = "{[()]]}"
l = []

for i in s:
    if i == "{" or i == "[" or i == "(":
        l.append(i)

    elif i == "}":
        if len(l) > 0 and l[-1] == "{":
            l.pop()
        else:
            l.append(i)

    elif i == "]":
        if len(l) > 0 and l[-1] == "[":
            l.pop()
        else:
            l.append(i)

    elif i == ")":
        if len(l) > 0 and l[-1] == "(":
            l.pop()
        else:
            l.append(i)

print(len(l) == 0)