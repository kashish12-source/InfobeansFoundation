# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4


# n =int(input("Enter a no. here : "))
n=9
max_value = (n//2)+1

for i in range(n):
    for j in range(n):

        dis_row = i
        dis_col = j 
        dis_bottom = n-1-i
        dis_top = n-1-j
        
        min_dis = min(dis_row,dis_col,dis_bottom,dis_top)

        value= max_value-min_dis

        print(value,end=" ")
    print()