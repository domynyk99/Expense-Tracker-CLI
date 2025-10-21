import argparse

from .tracker import Tracker

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

    #Create parser for add command
    parser_add = subparsers.add_parser('add', help="Add new expenses to your list")
    parser_add.add_argument('-c', '--category', required=False, type=str, help="Specify the category of your expense (optional)")
    parser_add.add_argument('-d', '--description', required=True, type=str, help="Specify a description for your expense")
    parser_add.add_argument('-a', '--amount', required=True, type=float, help="Specify the amount of your expense")

    #Create parser for update command
    parser_update = subparsers.add_parser('update', help="Update/Change an already existing expense")
    parser_update.add_argument('-i', '--expense_id', required=True, type=int, help="Specify the expense id of the expense you want to update")
    parser_update.add_argument('-c', '--category', required=False, type=str, help="Specify the category of your expense")
    parser_update.add_argument('-d', '--description', required=False, type=str, help="Specify a description for your expense")
    parser_update.add_argument('-a', '--amount', required=False, type=float, help="Specify the amount of your expense")

    #Create parser for delete command
    parser_delete = subparsers.add_parser('delete', help="Delete an already existing expense")
    parser_delete.add_argument('-i', '--expense_id', required=True, type=int, help="Specify the expense id of the expense you want to delete")

    #Create parser for list argument
    parser_list = subparsers.add_parser('list', help="List all existing expenses")
    parser_list.add_argument('-c', '--category', type=str, required=False, help="List all expenses filtered by a specified category")

    #Create parser for summary argument
    parser_summary = subparsers.add_parser('summary', help="Prints the sum of all your expenses")
    parser_summary.add_argument('-m', '--month', required=False, help="Summarize all expenses for a specified month")
    parser_summary.add_argument('-y', '--year', type=int, help="Specify a year. If you don't specify a year the current year is set as default value.")

    args = parser.parse_args()

    c_loader = Tracker()
    
    match args.command:
        case 'add':
            c_loader.create_expense(category=args.category, description=args.description, amount=args.amount)
        case 'update':
            c_loader.update_expense(expense_id=args.expense_id, category=args.category, description=args.description, amount=args.amount)
        case 'delete':
            c_loader.delete_expense(expense_id=args.expense_id)
        case 'list':
            c_loader.list_all(category=args.category)
        case 'summary':
            c_loader.summary(month=args.month, year=args.year)