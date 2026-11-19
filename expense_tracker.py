#PROJECT :- PERSONAL EXPENSE TRACKER
#CREATED BY:- RITESH AGRAHARI
#COURSE :- BCA

names = []
amounts = []
budget = 0

print("====================================")
print("     PERSONAL EXPENSE TRACKER")
print("     Created by: Ritesh Agrahari")
print("====================================")

name = input("\nPlease enter your name: ")
print("HELLO!", name.upper(), "WELCOME TO YOUR EXPENSE TRACKER")

while True:
    print("\n---------------- MENU ----------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spent")
    print("5. Set Budget")
    print("6. Check Budget")
    print("7. Highest Expense")
    print("8. Exit")
    print("--------------------------------------")

    choice = input("Enter your choice (1-8): ")

    # Add Expense
    if choice == "1":
        item = input("What did you spend on? ")
        amount = input("Enter amount: Rs. ")

        if amount.isdigit() and int(amount) > 0:
            names.append(item)
            amounts.append(int(amount))
            print("Expense added successfully!")
        else:
            print("Invalid amount! Please enter a number.")

    # View Expenses
    elif choice == "2":
        if len(names) == 0:
            print("No expenses yet.")
        else:
            print("\nNo.   Item              Amount")
            print("--------------------------------")
            for i in range(len(names)):
                print(i + 1, "   ", names[i], "         Rs.", amounts[i])

    # Delete Expense
    elif choice == "3":
        if len(names) == 0:
            print("No expenses to delete.")
        else:
            num = input("Enter expense number to delete: ")
            if num.isdigit() and 1 <= int(num) <= len(names):
                names.pop(int(num) - 1)
                amounts.pop(int(num) - 1)
                print("Expense deleted!")
            else:
                print("Invalid number!")

    # Total Spent
    elif choice == "4":
        print("Total spent: Rs.", sum(amounts))

    # Set Budget
    elif choice == "5":
        b = input("Enter your budget: Rs. ")
        if b.isdigit() and int(b) > 0:
            budget = int(b)
            print("Budget set to Rs.", budget)
        else:
            print("Invalid budget!")

    # Check Budget
    elif choice == "6":
        if budget == 0:
            print("Please set your budget first (option 5).")
        else:
            spent = sum(amounts)
            print("Budget    : Rs.", budget)
            print("Spent     : Rs.", spent)
            if spent <= budget:
                print("Remaining : Rs.", budget - spent)
                print("You are within your budget. Good job!")
            else:
                print("You crossed your budget by Rs.", spent - budget)

    # Highest Expense
    elif choice == "7":
        if len(amounts) == 0:
            print("No expenses yet.")
        else:
            highest = max(amounts)
            index = amounts.index(highest)
            print("Highest expense:", names[index], "- Rs.", highest)

    # Exit
    elif choice == "8":
        print("\nThank you for using Expense Tracker,", name, "!")
        print("Spend wisely!")
        break

    else:
        print("Invalid choice! Please select 1 to 8.")
