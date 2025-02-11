import matplotlib.pyplot as plt


def generate_income_vs_expense_report(transactions):
    """Generates a report of income vs. expenses and plots it."""
    total_income = sum(
        transaction["amount"] for transaction in transactions
        if transaction["type"] == "income"
    )
    total_expenses = sum(
        transaction["amount"] for transaction in transactions
        if transaction["type"] == "expense"
    )

    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")

    # Plot
    labels = ['Income', 'Expenses']
    values = [total_income, total_expenses]
    plt.bar(labels, values, color=['green', 'red'])
    plt.title('Income vs Expenses')
    plt.show()


def generate_spending_by_category_report(transactions):
    """Generates a report of spending by category and plots it."""
    spending = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            spending[category] = spending.get(category, 0) + transaction["amount"]

    for category, amount in spending.items():
        print(f"Spending in {category}: {amount}")

    # Plot
    plt.bar(spending.keys(), spending.values(), color='blue')
    plt.title('Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.show()
