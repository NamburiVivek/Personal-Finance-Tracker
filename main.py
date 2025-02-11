from income_expenses import record_transaction, categorize_transaction
from budgeting import set_budget, track_budget
from reporting_visualization import generate_income_vs_expense_report, generate_spending_by_category_report
from file_operations import save_data, load_data

def main():
    # Load existing transactions and budgets from a file
    transactions, budgets = load_data()

    while True:
        # Display menu options
        print("\n1. Record Transaction")
        print("2. Categorize Transactions")
        print("3. Set Budget")
        print("4. Track Budget")
        print("5. Generate Income vs Expense Report")
        print("6. Generate Spending by Category Report")
        print("7. Save Data")
        print("8. Restart")

        # Get user's choice
        choice = input("Choose an option (1-8): ")

        # Process user's choice
        if choice == "1":
            # To Record a new transaction
            record_transaction(transactions, budgets)
        elif choice == "2":
            #  To Categorize existing transactions
            categorize_transaction(transactions)
        elif choice == "3":
            #  To Set or modify budget categories
            set_budget(budgets)
        elif choice == "4":
            #  To Track current spending against budget
            track_budget(transactions, budgets)
        elif choice == "5":
            # To Generate a report comparing income and expenses
            generate_income_vs_expense_report(transactions)
        elif choice == "6":
            # To Generate a report showing spending by category
            generate_spending_by_category_report(transactions)
        elif choice == "7":
            # To Save current transactions and budgets to a file
            save_data(transactions, budgets)
        elif choice == "8":
            #  To Restart the program
            print("Exiting program.")
            break
        else:
            #  To Handle invalid input
            print("Invalid choice. Please choose a valid option (1-8).")

if __name__ == "__main__":
    # For Starting the main program
    main()