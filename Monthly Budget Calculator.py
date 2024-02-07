#This Program calculates your monthly budget

#Create a function to calculate the monthly budgget
def calculate_monthly_budget(income, expenses):
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    budget = {
        "Income": income,
        "Total Expenses": total_expenses,
        "Savings": savings
    }
    
    return budget

print("Welcome to the monthly budget calculator")

income = float(input("Enter your monthly income (ZAR): "))
num_expenses = int(input("Enter the number of expenses categories: "))

expenses = []

for i in range(num_expenses):
    expense = float(input(f"Enter the amount for expenses #{i+1}: "))
    expenses.append(expense)

budget = calculate_monthly_budget(income, expenses)
print("\nMonthly Budget Breakdown: ")

for category, amount in budget.items():
    print(f"{category}: R{amount:.2f}")