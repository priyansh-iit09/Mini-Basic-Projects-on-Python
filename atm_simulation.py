
print("................ATM Simulation Program...................")

users={
    "9900": 6000,
    "4590": 4000,
    "9293": 7000,
    "1234": 500,
    "5678":8000
}

transaction_list=[]
pin=input("Enter your pin number: ")

if(pin in users):
    print("You entered correct pin number:",pin)
    while True:
        print("\nHere are your options:")
        print("1.Check balance")
        print("2.Deposit money")
        print("3.Withdraw money")
        print("4.View transaction history")
        print("5.Exit")
        choice=int(input("Enter your choice (1/2/3/4/5):"))
        if choice==1:
            print("Your current balance is:",users[pin])
        elif choice==2:
            money=int(input("Enter deposit amount:"))
            if money>=0:
                users[pin]+=money
                transaction_list.append(["deposit",money])
                print("Successfully deposited:",money)
                print("Updated balance:",users[pin])
            else:
                print("Invalid amount! Deposit must be greater than zero.")

        elif choice==3:
            money=int(input("Enter withdrawal amount:"))
            if(money>=0 and money<=users[pin]):
                users[pin]-=money
                transaction_list.append(["withdrawl",money])
                print("Successfully withdrew:",money)
                print("Updated balance:",users[pin])
            else:
                print("Invalid amount! Withdrawal must be greater than zero or higher than initial amount.")

        elif choice==4:
            if transaction_list:
              print("Transaction History:",transaction_list)
            else:
                print("No transactions made yet.")

        elif choice == 5:
            print("Thank you for using the ATM. bye!")
            break

            

        else:
            print("Wrong choice! Please select an option from 1 to 5.")
else:
    print("Incorrect PIN number. Access denied.")
