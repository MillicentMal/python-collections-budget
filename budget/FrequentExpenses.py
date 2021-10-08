from . import Expense
from . import data


expenses = Expense.Expenses()
expenses.read_expenses(data.spending_data.csv)

spending_categories = []

for expense in expenses.list:
    spending_categories = spending_categories.append(expense.category)

    