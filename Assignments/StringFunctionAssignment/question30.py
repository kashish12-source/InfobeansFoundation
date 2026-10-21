# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"

def longest_common_prefix(l):
    l.sort()
    first = l[0]
    last = l[-1]
    res=""
    for i in range(min(len(first),len(last))):
        if first[i] == last[i]:
            res+=first[i]
        else:
            break
    return res

l =  ["flower", "flow", "floight"]
print(f"The longest common prefix from the given list of the words is : {longest_common_prefix(l)}")
