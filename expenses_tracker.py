import os, json
from utils import validate_amount, validate_user_input

def main():

    expenses = load_expenses()

    while True:

        print("=====EXPENSES TRACKER======\n")
        print("1. add expenses\n2. View expenses\n3. delete expenses\n4. Check Total Expenses\n5. View By Category\n6. Exit\n")

        user_input = validate_user_input("Choose a number from the listed options: ", ["1", "2", "3", "4", "5", "6"])
        print()
            

        match user_input:

            case "1":
                print(add_expenses(expenses) + "\n")

            case "2":
                view_expenses(expenses)

            case "3":
                print(delete_expenses(expenses) + "\n")
            
            case "4":
                total = total_spending(expenses)
                print(f"Current Total Expenses: ₦ {total:,.2f}")
                print()

            case "5":
                total_spending_by_category(expenses)

            case "6":
                print("Exiting...")
                break

        save_expenses(expenses)
        
        try_again = validate_user_input("will you like to perform another transaction? [y/n]: ", ["y", "n"]).lower()
        if try_again == "n":
            break

    print("Remeber to spend wisely!\nSee You Again!!!")


def load_expenses():

    try:
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                expenses = json.load(file)

        else :
            expenses = []

    except json.JSONDecodeError:
        print("WARNING! WARNING!! WARNING!!!")
        print("The file expenses.json exist but needed attention first\n")
        expenses = "Empty/Corrupted File"

    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def add_expenses(expenses):
    print("Give a brief description of proposed expenses\n")

    category = validate_user_input("Enter ategory: ").title()
    print()
    description = validate_user_input("Enter Description: ")
    print()
    amount = validate_amount("Enter Amount: ")
    print()

    expenses.append({
        "category": category,
        "description": description,
        "amount": amount
    })
    return "Action successful"


def view_expenses(expenses):

    if not expenses:
        print("The list is currently EMPTY!!!")
    
    else:
        number = 1

        for expense in expenses:
            print(f"---- ref number [{number}] ----")

            for key, value in expense.items():

                if key == "amount":
                    print(f"{key:<20}: {value:,.2f}")
                
                else:
                    print(f"{key:<20}: {value}")
                
            number += 1
            print()



def delete_expenses(expenses):

    if not expenses:
        return "Action Blocked: The list is currently empty"

    view_expenses(expenses)

    while True:
        delete_ind = int(validate_amount("Write the [ref number] of the deleting expenses: "))
        print()

        if delete_ind < 1 or delete_ind > len(expenses):
            print("slecetion out of range: choose again\n")
            continue
        else:
            break
    
    expenses.pop(delete_ind - 1)
    return f"Expenses {delete_ind} successfully deleted"



def total_spending(expenses):

    if not expenses:
        return 0

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total



def total_spending_by_category(expenses):

    if not expenses:
        print("The List is currently empty")

    else:

        total = total_spending(expenses)
        seen = {}

        for expense in expenses:
            category = expense["category"]

            if category in seen:
                seen[category] += expense["amount"]

            else:
                seen[category] = expense["amount"]
    
        for key, value in seen.items():
            percentage = (value * 100) / total
            print(f"{key:<20}: {value:,.2f}     {percentage:.2f}%")

    print()



if __name__ == "__main__":
    main()