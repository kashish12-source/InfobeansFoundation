l=[2,3,5,7,8]
even=0
odd =0
for i in l:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"even sum is : {even}")
print(f"odd sum is : {odd}")