"""
## **EXERCISE: Bill Calculator**

**PROBLEM STATEMENT:**

Let's imagine we're going out to eat at a restaurant; we just had a good meal and we want to calculate the bill. In essence, let's conceptualize and create a custom bill calculator in Python.

**OBJECTIVE:** Given a starting meal price (as a `float`) and a tip quantity (as an `int`) as well as a constant tax rate (as a `float`), calculate the total bill on purchased food.

**INPUT:** `calculate_bill(price_of_food=20.99, amount_tipped=5)`

**OUTPUT:** `27.826625`

---
"""

def calculate_bill(price_of_food:float, amount_tipped:int):
    tax_rate = 0.0875
    taxes = price_of_food * tax_rate
    return price_of_food + taxes + amount_tipped