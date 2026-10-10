# 19) 1	+	1/2	+	1/3	+	1/4	+	1/5	….. n terms(find out sum)
n=int(input("Enter a no. here : "))
i=1
sum=0
while(n!=0):
    sum+=(1/i)
    i+=1
    n-=1
print(f"sum of the series is : {sum:.2f}")