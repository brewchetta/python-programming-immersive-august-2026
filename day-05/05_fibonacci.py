"""## **EXERCISE: The Fibonacci Algorithm**

**OBJECTIVE:** Given an integer `N` representing the length of the sequence that we want to generate, output the value from the Fibonacci sequence at the corresponding position of `N`.

**FIBONACCI SEQUENCE**:

- `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...`
   0  1  2  3  4  5  6  7   8   9   10  11  12   13   14

**INPUT**: `fibonacci_of(N=10)`

**OUTPUT:** `55`

---
"""

# recursion is HARD

def fibonacci_of(n:int):
    if (n == 0):
        print("n:", n, " | result:", 0)
        return 0
    elif (n == 1):
        print("n:", n, " | result:", 1)
        return 1
    else:
        result = fibonacci_of(n - 1) + fibonacci_of(n - 2)
        print("n:", n, " | result:", result)
        return result