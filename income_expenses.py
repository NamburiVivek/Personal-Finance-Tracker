import json
from datetime import datetime


def record_transaction(transactions, budgets):
    """Records a new income or expense transaction."""
    while True:
        date = input("Enter date (DD-MM-YYYY) or 'restart' to initialize: ")
        if date.lower() == 'restart':
            break

        try:
            # Check if the date is in correct format
            datetime.strptime(date, "%d-%m-%Y")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            type_ = input("Enter type (income/expense): ").lower()
            
            # Validate transaction type and amount
            if type_ not in ("income", "expense"):
                print("Invalid transaction type! Please enter 'income' or 'expense'.")
                continue

            if amount <= 0:
                print("Enter a valid Amount!")
                continue
            
            # Update budget for income transactions
            if type_ == "income" and category in budgets:
                budgets[category] += amount
                print(f"Added {amount} to {category} income.")
            else:
                #  To Add transaction to the list
                transactions.append({
                    "date": date,
                    "amount": amount,
                    "category": category,
                    "type": type_
                })
                
                # Initialize budget category for new expense categories
                if type_ == "expense" and category not in budgets:
                    budgets[category] = 0

                print("Transaction recorded successfully!")
        except ValueError:
            print("Invalid input! Please enter valid data.")


def categorize_transaction(transactions):
    """Categorizes existing transactions."""
    for transaction in transactions:
        if not transaction.get("category"):
            print(f"Transaction on {transaction['date']} is uncategorized.")
            new_category = input("Enter a category for this transaction: ")
            transaction["category"] = new_category
            print(f"Transaction categorized as {new_category}.")
        else:
            print(f"Transaction on {transaction['date']} is already categorized as {transaction['category']}.")
