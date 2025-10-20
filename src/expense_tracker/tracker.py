from tabulate import tabulate
from datetime import datetime

from .expense import Expense
from .utils import load_json, write_to_json

class Tracker():
    def __init__(self):
        self.expenses: list[dict] = load_json()

    def create_expense(self, category:str, description: str, amount: float):
        if len(self.expenses) == 0:
            expense_id = 0
        else:
            expense_id = self.expenses[-1]['expense_id']+1
        expense = Expense(expense_id=expense_id, user=self, category=category, description=description, amount=amount)
        self.expenses.append(expense.to_dic())
        write_to_json(self.expenses)
        print(f"Expense eadded succesfully (ID: {expense_id})")

    def update_expense(self, expense_id: int, category: str = None, description: str = None, amount: float = None):
        if description is None and amount is None and category is None:
            print("ERROR: Please change at least one of the following: CATEGORY, DESCRIPTION, AMOUNT")
            return
        for expense in self.expenses:
            if expense['expense_id'] == expense_id:
                if description is not None:
                    expense['description'] = description
                if amount is not None:
                    expense['amount'] = amount
                if category is not None:
                    expense['category'] = category
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

    def list_all(self, category: str = None) -> None:
        headers = ['ID', 'Date', 'Category', 'Description', 'Amount']
        if category is None:
            rows = [[expense['expense_id'], expense['date'], expense['category'], expense['description'], f"{expense['amount']:.2f}$"] for expense in self.expenses]
        else:
            rows = self.filter_category(category)
            print(f"Expenses filtered by category: {category}")
        print(tabulate(rows, headers))

    def filter_category(self, category: str) -> list[str]:
        rows = []
        for expense in self.expenses:
            if expense['category'] != category:
                continue
            rows.append([expense['expense_id'], expense['date'], expense['category'], expense['description'], f"{expense['amount']:.2f}$"])
        return rows

    def summary(self, month: str = None, year: int = None) -> None:
        if month is None:
            total_expenses = 0
            for expense in self.expenses:
                total_expenses += expense['amount']
            print(f"Total expenses: {total_expenses:.2f}$")
        else:
            if year is None:
                year = datetime.now().year
            month_expenses = self.summary_specific_month(month, year)
            month_string = self.convert_month(month=month, switch=True)
            print(f"Total expenses for month {month_string}: {month_expenses:.2f}$")

    def summary_specific_month(self, month: str, year: int) -> float:
        month = self.convert_month(month=month, switch=False)
        if month < 1 | month > 12:
            return
        month_str = str(month)
        if month < 10:
            month_str = "0" + month_str
        month_sum = 0

        for expense in self.expenses:
            if expense['date'][3:5] != month_str or expense['date'][6:10] != str(year):
                continue
            month_sum += expense['amount']
        
        return month_sum

    def convert_month(self, month: str, switch: bool):
        """Converts a month to an int if the switch is set to False. If it is set to True it will return
        the given month as a string that can later be used for print statements."""
        month = month.lower().strip()
        month_number = 0
        month_string = ""
        match month:
            case "january" | "1" | "01":
                month_number = 1
                month_string = "January"
            case "february" | "2" | "02":
                month_number = 2
                month_string = "February"
            case "march" | "3" | "03":
                month_number = 3
                month_string = "March"
            case "april" | "4" | "04":
                month_number = 4
                month_string = "April"
            case "may" | "5" | "05":
                month_number = 5
                month_string = "May"
            case "june" | "6" | "06":
                month_number = 6
                month_string = "June"
            case "july" | "7" | "07":
                month_number = 7
                month_string = "July"
            case "august" | "8" | "08":
                month_number = 8
                month_string = "August"
            case "september" | "9" | "09":
                month_number = 9
                month_string = "September"
            case "october" | "10":
                month_number = 10
                month_string = "October"
            case "november" | "11":
                month_number = 11
                month_string = "November"
            case "december" | "12":
                month_number = 12
                month_string = "December"
            case _:
                print("ERROR: Check again for spelling mistakes or if you typed a number check if it is between 1 and 12.")
        if switch:
            return month_string
        else:
            return month_number
    
    def filter_month(self, month:str, year:int) -> list[str]:
        rows = []
        for expense in self.expenses:
            if expense['date'][3:5] != month or expense['date'][6:10] != str(year):
                continue
            rows.append([expense['expense_id'], expense['date'], expense['category'], expense['description'], f"{expense['amount']:.2f}$"])
        return rows