"""### **ALGORITHMS CHALLENGE:** The Expense Tracker

Given a list of dictionaries representing specific product names, manufacturing costs, and selling prices, add new key-value pairs for each dictionary representing net expense as either profit (positive) or loss (negative).

If profit was earned, add key-value pairs where `net_positive = True` and `net_negative = False`.

If loss was incurred, add key-value pairs where `net_positive = False` and `net_negative = True`.

If breakeven occurred, add key-value pairs where `net_positive = False` and `net_negative = False`.

Finally, enable the function to accept a boolean keyword argument called `subset_expenses`. If `True`, instead of returning the entire dictionary, return two lists of the net positive and net negative expenses.
"""

# Example expense report data.
current_expense_report = [
    {"name": "headphones", "total_cost": 4500, "total_revenue": 9000},
    {"name": "smartwatches", "total_cost": 2000, "total_revenue": 3990},
    {"name": "laptops", "total_cost": 50000, "total_revenue": 47500},
    {"name": "desktops", "total_cost": 77000, "total_revenue": 101400}
]

"""#### **Pseudocode.**

```
function to track expenses (expense report, boolean to subset)
  look over all expenses
    calculate net gain or loss
    by default, assume neither gain nor loss
    if gain, set gained status to true
    if loss, set loss status to true
    add gain and loss statuses to each expense in report
  if boolean to subset is true...
    split expenses into profits and losses using tracked statuses and send out
  otherwise, send current data out
```

#### **Coding Implementation.**
"""

# Function to track expenses with report and boolean-to-subset.
def track_expenses(expenses, subset_expenses=False):
  # TODO: Implement your code here!
  return