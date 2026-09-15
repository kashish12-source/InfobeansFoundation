name =input("Enter the name here :")
gender = input("Enter the gender here: ")

quant_1 = int(input("enter the quantity of item 1 here :"))

quant_2 = int(input("enter the quantity of item 2 here :"))

quant_3 = int(input("enter the quantity of item 3 here :"))

quant_4 = int(input("enter the quantity of item 4 here :"))

quant_5 = int(input("enter the quantity of item 5 here :"))

quant_6 = int(input("enter the quantity of item 6 here :"))

quant_7 = int(input("enter the quantity of item 7 here :"))

quant_8 = int(input("enter the quantity of item 8 here :"))

quant_9 = int(input("enter the quantity of item 9 here :"))

quant_10 = int(input("enter the quantity of item 10 here :"))

total_quant5 = (50*quant_5)*0.01

total_quant10 = (100*quant_10) *0.15
if quant_1>4:
    quant1_dis =(10*quant_1) * 0.05 
    
else:
    quant1_dis =(10*quant_1)
    
total =  quant1_dis * 0.05  + (20*quant_2) +(30*quant_3) + (40*quant_4) + total_quant5 +(60*quant_6) + (70*quant_7) +(80*quant_8) + (90*quant_9) + total_quant10
bill =total
if total >10000 :
    bill = total *0.15
elif total >5000 and total <=10000:
    bill = total *0.10

gst= bill*0.10
total_bill =  gst + bill

carrybag = input("Want carry bag or not")
if carrybag == "yes":
    x=10.00
    
    total_bill = total_bill + 10 
else:
    x=0.00

if gender == "female":
    Gift = "Cadbury"
elif gender == "male":
    Gift = "Ladger Wallet"
else :
    Gift = "No gift"
    
print(f"\t\t\t\t D-Mart")
print(f"Name : {name} \t\t\t\t\t\t     Date : 15/09/26")
print("----------------------------------------------------------------------------")
print(f"Item Name  \t Quantity  \t Price  \t Total  \t AfterDiscount")
print(f"  Item-1   \t    {quant_1}   \t   10   \t   {10*quant_1}  \t           {quant1_dis}")
print(f"  Item-2   \t    {quant_2}   \t   20   \t   {20*quant_2}  \t   {20*quant_2}")
print(f"  Item-3   \t    {quant_3}   \t   30   \t   {30*quant_3}  \t   {30*quant_3}")
print(f"  Item-4   \t    {quant_4}   \t   40   \t   {40*quant_4}  \t   {40*quant_4}")
print(f"  Item-5   \t    {quant_5}   \t   50   \t   {50*quant_5}  \t   {total_quant5}")
print(f"  Item-6   \t    {quant_6}   \t   60   \t   {60*quant_6}  \t   {60*quant_6}")
print(f"  Item-7   \t    {quant_7}   \t   70   \t   {70*quant_7}  \t   {70*quant_7}")
print(f"  Item-8   \t    {quant_8}   \t   80   \t   {80*quant_8}  \t   {80*quant_8}")
print(f"  Item-9   \t    {quant_9}   \t   90   \t   {90*quant_9}  \t   {90*quant_9}")
print(f"  Item-10   \t    {quant_10}  \t           100   \t   {100*quant_10}  \t   {total_quant10}")
print("----------------------------------------------------------------------------")
print(f"\t\t\t\t\t A.P\t\tD.P")
print(f"\t\t\t\t\t{total}\t\t{bill}")
print(f"Gift :- {Gift} \t\t\t 0.0\t\t0.0 \n")
print(f"Carry Bag : {carrybag}\t\t\t\t{x}\t\t{x}")
print(f"GST : 10% \t\t\t\t{total_bill}\t\t{total_bill}")
print("----------------------------------------------------------------------------")
print(f"\t\t\t\tThank You")
print(f"\t\t\t         To Vist")
print(f"\t\t\t          D-Mart")