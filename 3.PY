# Case Study 3: ATM Transaction Sequence Simulation

balance = float(input("Enter opening balance: "))

transactions = []

while True:
    print("\n--- ATM MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            transactions.append(("Deposit", amount))
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance = balance - amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful.")

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")

print("\nFinal balance:", balance)
print("Transaction History:")

for transaction in transactions:
    print(transaction[0], "- Rs.", transaction[1])