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
    {"name": "desktops", "total_cost": 77000, "total_revenue": 101400},
    {"name": "robot dog", "total_cost": 10000, "total_revenue": 10000},
]



# Function to track expenses with report and boolean-to-subset.
def track_expenses(expenses, subset_expenses=False):
  subset_items = {
    "net_positives": [],
    "net_negatives": []
  }

  # begin for loop
  for item in expenses:
    item_revenue = item["total_revenue"]
    item_cost = item["total_cost"]

    if (item_revenue - item_cost > 0):
      item["net_positive"] = True
    else:
      item["net_positive"] = False

    if (item_revenue - item_cost < 0):
      item["net_negative"] = True
    else:
      item["net_negative"] = False

    if (item_revenue - item_cost > 0 and subset_expenses):
      subset_items["net_positives"].append( item )
    elif (item_revenue - item_cost < 0 and subset_expenses):
      subset_items["net_negatives"].append( item )
  # end for loop

  if (subset_expenses):
    return subset_items
  else:
    return expenses