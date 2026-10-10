# 18) 1	2	2	4	8	32	…… n terms

n = int(input("Enter a no. here : "))

a = 1
b = 2 
n-=2
print( a , end= " ")
print( b , end = " ")
while(n!=0):
    k=a*b
    print(k,end=" ")
    a=b
    b=k
    n-=1