# 32) A	b	C	d	E	f	G	h	…… n terms 
n =int(input("Enter a no. here : "))
k = 65
i=0
if(n==26):
    while(n!=0):
        if(i%2==0):
            print(chr(k),end="  ")
        else:
            print(chr(k+32),end=" ")
        k+=1
        i+=1
        n-=1
else:
    print("please enter the no. less than and equal to the 26")