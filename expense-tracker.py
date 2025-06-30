from __future__ import annotations
import argparse
import datetime
import json
from tabulate import tabulate

class Expense():
    def __init__(self, expense_id: int, user: User, description: str, amount: float):
        self.expense_id = expense_id
        self.user = user
        self.description = description
        self.amount = amount

    def update(self, description: str, amount: float) -> None:
        self.description = description
        self.amount = amount
        print(f"Expense updated successfully (ID: {self.expense_id})")

    def __str__(self) -> None:
        return f"{self.expense_id}\t{self.description}\t\t{self.amount:.2f}$"

    def to_dic(self) -> dict:
        expense_dic = {
            'expense_id': self.expense_id,
            'date': datetime.datetime.now().strftime("%d-%m-%Y"),
            'description': self.description,
            'amount': self.amount
        }
        return expense_dic

class User():
    def __init__(self):
        self.expenses: list[dict] = self.load_expenses()

    def load_expenses(self):
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
        return expenses

    def create_expense(self, description: str, amount: float):
        if len(self.expenses) == 0:
            expense_id = 0
        else:
            expense_id = self.expenses[-1]['expense_id']+1
        expense = Expense(expense_id=expense_id, user=self, description=description, amount=amount)
        self.expenses.append(expense.to_dic())
        with open('expenses.json','w') as file:
            json.dump(self.expenses, file, indent=4)
        print(f"Expens eadded succesfully (ID: {expense_id})")

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
                with open('expenses.json','w') as file:
                    json.dump(self.expenses, file, indent=4)
                print(f"Expense updated succesfully (ID: {expense_id})")
                return
        print(f"ERROR: Couldn't find expense with id: ID{expense_id}")

    def delete_expense(self, expense_id: int) -> None:
        for expense in self.expenses:
            if expense['expense_id'] == expense_id:
                self.expenses.remove(expense)
                with open('expenses.json','w') as file:
                    json.dump(self.expenses, file, indent=4)
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

    #Create parser for add command
    parser_add = subparsers.add_parser('add', help="Add new expenses to your list")
    parser_add.add_argument('-d', '--description', required=True, type=str, help="Specify a description for your expense")
    parser_add.add_argument('-a', '--amount', required=True, type=float, help="Specify the amount of your expense")

    #Create parser for update command
    parser_update = subparsers.add_parser('update', help="Update/Change an already existing expense")
    parser_update.add_argument('-i', '--expense_id', required=True, type=int, help="Specify the expense id of the expense you want to update")
    parser_update.add_argument('-d', '--description', required=False, type=str, help="Specify a description for your expense")
    parser_update.add_argument('-a', '--amount', required=False, type=float, help="Specify the amount of your expense")

    #Create parser for delete command
    parser_delete = subparsers.add_parser('delete', help="Delete an already existing expense")
    parser_delete.add_argument('-i', '--expense_id', required=True, type=int, help="Specify the expense id of the expense you want to delete")

    #Create parser for list argument
    parser_list = subparsers.add_parser('list', help="List all existing expenses")

    #Create parser for summary argument
    parser_summary = subparsers.add_parser('summary', help="Prints the sum of all your expenses")
    parser_summary.add_argument('--month', required=False, help="Summarize all expenses for a specified month")

    args = parser.parse_args()

    user = User()
    
    match args.command:
        case 'add':
            user.create_expense(description=args.description, amount=args.amount)
        case 'update':
            user.update_expense(expense_id= args.expense_id,description=args.description, amount=args.amount)
        case 'delete':
            user.delete_expense(expense_id=args.expense_id)
        case 'list':
            user.list_all()
        case 'summary':
            user.summary()