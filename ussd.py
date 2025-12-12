# balance += amount → adds to balance when depositing.
# balance -= amount → subtracts from balance when withdrawing

print("Welcome to ABDUL-RAFEEQ banking system😇🤝!")
print("---------------------------------------")

balance = 0  # starting balance
savings = 0  # savings account

while True:
    print("\nMenu: Press 1 for Deposit  2 for Withdraw  3 for Check Balance  4 for Save  5 to Exit")
    choice = input("Please enter your choice (1-5): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("❌ Invalid amount! Please enter a positive number.")
        else:
            balance += amount
            print(f"✅ You have deposited {amount}. New balance: {balance}")

    elif choice == "2":
        amount = float(input("Kindly enter the amount to withdraw: "))
        if amount > balance:
            print("❌ Insufficient funds!")
        else:
            balance -= amount
            print(f"✅ You have withdrawn {amount}. Remaining balance: {balance}")

    elif choice == "3":
        print(f"💰 Your current balance is: {balance}")

    elif choice == "4":
        amount = float(input("Enter amount to save: "))
        if amount <= 0:
            print("❌ Invalid amount! Please enter a positive number.")
        elif amount > balance:
            print("❌ Insufficient funds to save!")
        else:
            balance -= amount
            savings += amount
            print(f"✅ You saved {amount}. Savings: {savings}, Remaining balance: {balance}")

    elif choice == "5":
        print("👋🏽 Thank you for using ABDUL-RAFEEQ banking system!")
        break

    else:
        print("Invalid choice, please try again.")