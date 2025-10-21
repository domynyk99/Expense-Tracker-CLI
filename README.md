# Expense Tracker CLI Application

## Overview
A simple command-line application to track your personal expenses directly from the terminal.
Built with Python and `argparse`, this CLI tool lets you easily add, update, delete, and view expenses stored locally in a simple JSON file.

## Features

- **Add** an expense with description, category, and amount  
- **Update** or **delete** existing expenses  
- **View** all recorded expenses in a formatted table  
- **Summarize** expenses by month  
- **Filter** expenses by category

## Installation

#### Prerequisites
- Python 3.10 or higher
- [tabulate](https://pypi.org/project/tabulate/) (installed automatically when using `pip install .`)

1. Clone the repository:
    
    ```bash
    git clone https://github.com/domynyk99/Expense-Tracker-CLI.git
    cd Expense-Tracker-CLI
    ```

2. Install the package:

    ```bash
    pip install .
    ```

3. Run the CLI:
    ```bash
    expense-tracker <command> [arguments]
    ```

## How to use

```bash
expense-tracker add --description "Dinner" --amount 28.74
# Expense added succesfully (ID: 0)

expense-tracker add --description "Gym Membership" --category Sports  --amount 14.99
# Expense added succesfully (ID: 1)

expense-tracker list
#   ID  Date        Category    Description     Amount
# ----  ----------  ----------  --------------  --------
#    0  21-10-2025              Dinner          28.74$
#    1  21-10-2025  Sports      Gym Membership  14.99$

expense-tracker summary
# Total expenses: 43.73$

expense-tracker list --category Sports
# Expenses filtered by category: Sports
#   ID  Date        Category    Description     Amount
# ----  ----------  ----------  --------------  --------
#    1  21-10-2025  Sports      Gym Membership  14.99$

expense-tracker delete --id 0
# Expense deleted succesfully (ID: 0)

expense-tracker summary
# Total expenses: 14.99$

expense-tracker summary --month october
# Total expenses for month October: 14.99$

expense-tracker summary --month 10
# Total expenses for month October: 14.99$
```

## Why I built this

I built this project to learn more about command-line interfaces using Python's `argparse` module. I also wanted to explore how to save and structure data effectively in a JSON format, and to practice object-oriented design in a small, practical project.

## Future Improvements
- Allow users to set a monthly budget and show warnings when approaching or exceeding it  
- Export expenses to a CSV file
