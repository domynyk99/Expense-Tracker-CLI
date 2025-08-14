import datetime

class Expense():
    def __init__(self, expense_id: int, category: str, description: str, amount: float, user):
        self.expense_id = expense_id
        self.user = user
        self.category = category
        self.description = description
        self.amount = amount

    def update(self, category: str, description: str, amount: float) -> None:
        self.category = category
        self.description = description
        self.amount = amount
        print(f"Expense updated successfully (ID: {self.expense_id})")

    def __str__(self) -> None:
        return f"{self.expense_id}\t{self.description}\t\t{self.amount:.2f}$"

    def to_dic(self) -> dict:
        expense_dic = {
            'expense_id': self.expense_id,
            'date': datetime.datetime.now().strftime("%d-%m-%Y"),
            'category': self.category,
            'description': self.description,
            'amount': self.amount
        }
        return expense_dic