def set_budget(budgets):
    """Sets or updates the budget for a category."""
    try:
        category = input("Enter category: ")
        amount = float(input("Enter budget amount: "))
        
        if amount <= 0:
            print("Budget amount must be greater than zero.")
            return

        budgets[category] = amount
        print(f"Budget for {category} set to {amount}")

    except ValueError:
        print("Invalid budget amount! Please enter a valid number.")


def track_budget(transactions, budgets):
    """Tracks spending against the set budget."""

    # Initialize a dictionary to track spending for each category
    spending = {category: 0 for category in budgets}

    # Iterate through transactions and accumulate spending for each category
    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]
        if category in budgets and transaction["type"] == "expense":
            spending[category] += amount
    
    # Print a summary of the budget, actual spending, and remaining budget for each category
    for category, budget in budgets.items():
        actual_spending = spending.get(category, 0)
        remaining_budget = budget - actual_spending
        print(f"Budget for {category}: {budget}")
        print(f"Actual Spending on {category}: {actual_spending}")
        print(f"Remaining Budget for {category}: {remaining_budget}\n")
