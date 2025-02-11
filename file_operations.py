import json

def save_data(transactions, budgets, transactions_file="transactions.json", budgets_file="budgets.json"):
    """Saves transactions and budgets to JSON files."""
    try:
        with open(transactions_file, "w") as f:
            json.dump(transactions, f)
        with open(budgets_file, "w") as f:
            json.dump(budgets, f)
        print("Data saved successfully.")
    except IOError:
        print("Error saving data to files.")


def load_data(transactions_file="transactions.json", budgets_file="budgets.json"):
    """Loads transactions and budgets from JSON files."""
    try:
        # Opening the transaction file in read mode and loading the transaction data
        with open(transactions_file, "r") as f:
            transactions = json.load(f)

        # Opening the budget file in read mode and loading the budget data
        with open(budgets_file, "r") as f:
            budgets = json.load(f)

        print("Data loaded successfully.")
        return transactions, budgets
    
    except (IOError):
        print("Error loading data from files. Starting with empty data.")
        return [], {}
