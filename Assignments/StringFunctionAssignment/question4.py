# 4. Count uppercase letters, lowercase letters, digits, and special characters.
def count(s):
    sc=lc=uc=dc=0
    for i in s:
        if 65 <= ord(i) <= 90:
            uc+=1
        elif 97 <= ord(i) <=122:
            lc+=1
        elif 48<= ord(i)<=57:
            dc+=1
        else:
            sc+=1
    return sc , lc ,uc , dc

s ="adifAao22512m3#"
sc,lc,uc,dc = count(s)
print(f"Special count is : {sc}")
print(f"Lower count is : {lc}")
print(f"Upper count is : {uc}")
print(f"Digit count is : {dc}")


