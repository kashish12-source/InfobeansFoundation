for i  in range(5,0,-1):
    k=65 
    for j in range(0,i):
        print(" ",end="")
    for j in range(1,6):
        if j<=5 and j>=i:
            print(chr(k),end="") 
            k+=1
    print()


#      A
#     AB
#    ABC
#   ABCD
#  ABCDE