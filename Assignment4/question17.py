# 17) 1 	2	 4	 7	 11	 16 	…… n terms

n= int(input("enter a no. here : "))

i= 0
k=1
while(n!=0):
    k+=i
    print(k,end=" ")
    i+=1
    n-=1