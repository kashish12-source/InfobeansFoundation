# 27) *	#	*	#	*	#	*	#	*	…….
n = int(input("enter a no. here : "))
i=0
while(n!=0):
    if(i%2==0):
        print("*",end=" ")
    else:
        print("#",end= " ")
    i+=1
    n-=1