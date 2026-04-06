import json

print("💰 Expense Tracker")

# load data
try:
    with open("expenses.json", "r") as file:
        data = json.load(file)
except:
    data = []

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    # ADD INCOME
    if choice == "1":
        amount = float(input("Enter income amount: "))
        data.append({"type": "income", "amount": amount})

        with open("expenses.json", "w") as file:
            json.dump(data, file)

        print("✅ Income added")

    # ADD EXPENSE
    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        data.append({"type": "expense", "amount": amount})

        with open("expenses.json", "w") as file:
            json.dump(data, file)

        print("✅ Expense added")

    # VIEW BALANCE
    elif choice == "3":
        balance = 0

        for item in data:
            if item["type"] == "income":
                balance += item["amount"]
            else:
                balance -= item["amount"]

        print("💰 Current Balance:", balance)

    # EXIT
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice ❌")