class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        sum_expenses = 0
        expenses = list()
        self.sum_overages = 0
        self.overages = list()

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
