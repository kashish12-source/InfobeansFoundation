# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False

def balanced_para(s):
    l =[]
    for i in range(len(s)):
        if s[i] == "{" or s[i] =="[" or s[i]=="(":
            l.append(s[i])
        elif s[i] == "}" and l[-1] == "{":
            l.pop()
        elif s[i] == "]" and l[-1] == "[":
            l.pop()
        elif s[i] == ")" and l[-1] == "(":
            l.pop()
        else:
            return False
    return True

s ="{[]()]}"
if balanced_para(s):
    print("Balanced")
else:
    print("Not balanced")

    
