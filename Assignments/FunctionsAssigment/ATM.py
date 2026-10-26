# 3. ATM Banking Simulator
# Beginner–Intermediate
# Concepts: Nested conditions, loops, functions
# Requirements
# •	Verify a PIN.
# •	Display balance, deposit, withdrawal, and exit options.
# •	Prevent withdrawals exceeding the available balance.
# •	Reject invalid amounts.
# •	Use separate functions for deposit, withdrawal, and balance enquiry.
# Bonus: Allow only three PIN attempts.
def data():
    d = {
    123:{"name":"kashish", "balance" :200000},
    134:{"name":"keshav","balance":300000},
    145:{"name":"kartavya","balance":400000}
    }
    return d
count=0
d = data()
def verify_pin(pin):
    global count
    if count<3:
        present_data = data()
    
        if pin in present_data:
            return True
        else:
            count+=1
            if count == 3:
                print("You have tried 3 times. Try again later.")
            return False
    

def balance(pin):
    return d[pin]["balance"]
        
def deposit(pin,bal):
    # d = data ()
    for i in d.keys():
        if pin in d:
            d[pin]["balance" ] +=bal
            return d[pin]["balance"]
def withdrawal(pin,bal):

    if bal <=0:
        return False
    if bal>d[pin]["balance"]:
        return False
    d[pin]["balance"]-=bal
    return d[pin]["balance"]
    
def exit():
    return False


while(count<3):
    pin = int(input("Enter the pin here : "))
    print()
    if verify_pin(pin):
        print(verify_pin(pin))

        break
    else:
        print("Incorrect password")


if verify_pin(pin):
    f =True
    while(f):
        print("\n1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        inputs = int(input("Enter you task here : "))
        if inputs == 1:
            print(f"The balance in your account is : {balance(pin)}")



        elif inputs == 2:
            bal = float(input("Enter the balance you want to deposit: "))
            print(f"Balance before withdrawal is :{balance(pin)}")
            print()

            print(f"Balance after deposite the money is : {deposit(pin,bal)}")


        elif inputs ==3 :
            bal = float(input("Enter the balance you want to withdrawal: "))
            print(f"Balance before withdrawal is :{balance(pin)}")
            result = withdrawal(pin,bal)
            if result:
                
                print(f"Balance after withdrawal money is : {result}")
                
            else:
                print("The balance is not enough")



        elif inputs == 4 :
            f =False
        else:
            print("Please enter the valid no. here !!!")