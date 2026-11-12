# 9. ATM Machine Simulation
# Problem

# Design ATM software.

# Requirements

# Each account should have:

# account number
# PIN
# balance
# Functionalities
# Login verification
# Withdraw
# Deposit
# Change PIN
# Mini statement
# Additional Challenge

# Lock account after 3 wrong PIN attempts.

# Concepts Practiced
# encapsulation mindset
# validations
# object state

class ATM:
    __collection = {}

    def __init__(self, acc_no, pin, balance):
        self.__acc_no = acc_no
        self.__pin = pin
        self.__balance = balance

        ATM.__collection[self.__acc_no] = {
            "pin": self.__pin,
            "balance": self.__balance
        }

    def withdraw(self):
        account = int(input("Enter account number: "))

        if account in ATM.__collection:
            n = 3

            while n != 0:
                pin = int(input("Enter your PIN: "))

                if pin == ATM.__collection[account]["pin"]:
                    amount = float(input("Enter amount: "))

                    if amount > 0 and amount <= ATM.__collection[account]["balance"]:
                        ATM.__collection[account]["balance"] -= amount

                        print(f"Balance left: {ATM.__collection[account]['balance']}")
                    else:
                        print("Invalid amount or insufficient balance")

                    break

                else:
                    print("Enter valid PIN")
                    n -= 1

            if n == 0:
                print("Your account is locked due to 3 incorrect attempts")

        else:
            print("Account not found")

    def login_verification(self):
        account = int(input("Enter account number: "))

        if account in ATM.__collection:
            n = 3

            while n != 0:
                pin = int(input("Enter your PIN: "))

                if pin == ATM.__collection[account]["pin"]:
                    print("Login successful")
                    break

                else:
                    print("Enter valid PIN")
                    n -= 1

            if n == 0:
                print("3 incorrect attempts")

        else:
            print("Account not found")

    def deposit(self):
        account = int(input("Enter account number: "))

        if account in ATM.__collection:
            n = 3

            while n != 0:
                pin = int(input("Enter your PIN: "))

                if pin == ATM.__collection[account]["pin"]:
                    amount = float(input("Enter amount: "))

                    if amount > 0:
                        ATM.__collection[account]["balance"] += amount

                        print(f"Now the balance is: {ATM.__collection[account]['balance']}")
                    else:
                        print("Enter a valid amount")

                    break

                else:
                    print("Enter valid PIN")
                    n -= 1

            if n == 0:
                print("3 incorrect attempts")

        else:
            print("Account not found")

    def change_pin(self):
        account = int(input("Enter account number: "))

        if account in ATM.__collection:
            old_pin = int(input("Enter old PIN: "))

            if old_pin == ATM.__collection[account]["pin"]:
                new_pin = int(input("Enter new PIN: "))

                ATM.__collection[account]["pin"] = new_pin

                print("PIN changed successfully")

            else:
                print("Incorrect old PIN")

        else:
            print("Account not found")


# Creating objects

a1 = ATM(1, 123, 3536)
a2 = ATM(2, 124, 20000)
a3 = ATM(3, 125, 300000)


print("Withdraw from a1")
a1.withdraw()

print("\nDeposit to a2")
a2.deposit()

print("\nChange PIN of a3")
a3.change_pin()
