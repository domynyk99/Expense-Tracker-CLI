from tabulate import tabulate
from expense import Expense
from utils import load_json, write_to_json

class CommandLoader():
    def __init__(self):
        self.expenses: list[dict] = load_json()

    def create_expense(self, description: str, amount: float):
        if len(self.expenses) == 0:
            expense_id = 0
        else:
            expense_id = self.expenses[-1]['expense_id']+1
        expense = Expense(expense_id=expense_id, user=self, description=description, amount=amount)
        self.expenses.append(expense.to_dic())
        write_to_json(self.expenses)
        print(f"Expense eadded succesfully (ID: {expense_id})")

    def update_expense(self, expense_id: int, description: str = None, amount: float = None):
        if description is None and amount is None:
            print("ERROR: Please change at least the description or the amount of the expense.")
            return
        for expense in self.expenses:
            if expense['expense_id'] == expense_id:
                if description is not None:
                    expense['description'] = description
                if amount is not None:
                    expense['amount'] = amount
                write_to_json(self.expenses)
                print(f"Expense updated succesfully (ID: {expense_id})")
                return
        print(f"ERROR: Couldn't find expense with id: ID{expense_id}")

    def delete_expense(self, expense_id: int) -> None:
        for expense in self.expenses:
            if expense['expense_id'] == expense_id:
                self.expenses.remove(expense)
                write_to_json(self.expenses)
                print(f"Expense deleted succesfully (ID: {expense_id})")
                return
        print(f"ERROR: Couldn't find expense with id: ID{expense_id}")

    def list_all(self) -> None:
        headers = ['ID', 'Date', 'Description', 'Amount']
        rows = [[expense['expense_id'], expense['date'], expense['description'], f"{expense['amount']:.2f}$"] for expense in self.expenses]
        print(tabulate(rows, headers))

    def summary(self) -> None:
        total_expenses = 0
        for expense in self.expenses:
            total_expenses += expense['amount']
        print(f"Total expenses: {total_expenses:.2f}$")