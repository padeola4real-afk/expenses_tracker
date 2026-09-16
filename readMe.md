# Expense Tracker

A terminal-based personal expense tracker built in Python. Add, view, delete, and analyze your expenses — with data automatically saved to disk between sessions.

## Features


- **Add expenses** — record an amount, category, and description for each transaction
- **View expenses** — see a numbered, formatted list of every recorded expense
- **Delete expenses** — remove a specific expense by its reference number
- **Total spending** — calculate the sum of all recorded expenses
- **Spending by category** — see totals *and* percentage breakdown per category
- **Persistent storage** — expenses are saved to `expenses.json` and automatically reloaded the next time the program runs
- **Input validation** — all menu choices and numeric input are validated, with clear prompts to retry on invalid entries
- **Graceful file handling** — the app starts cleanly even if no data file exists yet, and warns (without crashing) if the data file is corrupted


## Getting Started

### Requirements

- Python 3.10 or later (uses the `match`/`case` statement)

### Running the app

```
python3 expense_tracker.py
```

The file `expenses.json` is created automatically the first time you save data, and read automatically on every startup. If the file is ever missing, the app starts with an empty list. If the file exists but is corrupted or unreadable, the app warns you and falls back to an empty list rather than crashing.
## Usage

When you run the program, you'll see a menu:

```
=====EXPENSES TRACKER======

1. add expenses
2. View expenses
3. delete expenses
4. Check Total Expenses
5. View By Category
```

Choose an option by entering its number. After each action, you'll be asked whether you'd like to perform another transaction (`y`/`n`). Your data is saved automatically after every action, so nothing is lost if the program is closed unexpectedly.


## Data Storage

Expenses are stored in `expenses.json`, in the project directory, as a list of objects:

```json
[
    {
        "amount": 5000,
        "category": "Food",
        "description": "Lunch"
    }
]
```


## Design Notes

- Expenses are stored in memory as a **list of dictionaries** — chosen because most operations (viewing, totaling, grouping) need to process every expense anyway, so a simple list is sufficient without the overhead of managing unique IDs.
- No artificial ID field is used for each expense. Instead, an expense's **position in the list** doubles as its reference number, shown to the user as a 1-based index.
- Data is loaded once at startup and saved after every transaction, minimizing the risk of data loss if the program exits unexpectedly.

## Possible Improvements

- Handle non-integer input for the delete reference number more strictly (currently accepts a float and truncates it)
- Prevent duplicate/inconsistent category names (e.g. typos creating separate categories)
- Allow editing an existing expense instead of only add/delete
- Preserve a backup of a corrupted data file instead of discarding it