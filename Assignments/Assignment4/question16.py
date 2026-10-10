# 16) …... -6	-3	0	3	6	9	……. n terms [where n is even]	
n= int (input("Enter a no. here : "))
if (n%3==0):
    for i in range(-n,n+1,3):
        print(i,end=" ")
else:
    print("please enter the digit which is multiple of 3")