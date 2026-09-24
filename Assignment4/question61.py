# 61) WAP to find out all the leap years between two entered years
year_1 = 2000
year_2 = 2020

for i in range(year_1 , year_2+1):
    if((i%400 ==0 ) or (i%4 == 0  and i%100!=0)):
        print(f"{i} is a leap year")