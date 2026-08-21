"""
## **EXERCISE: Fizz(y) Buzz(y)**

**OBJECTIVE:** Given a positive number, print each integer up to that number substituting "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5, and "Fizz Buzz" for numbers divisible by both.

**INPUT:** `15`

**OUTPUT:**
  - `1`
  - `2`
  - `"Fizz"`
  - `4`
  - `"Buzz"`
  - `"Fizz"`
  - `7`
  - `8`
  - `"Fizz"`
  - `"Buzz"`
  - `11`
  - `"Fizz"`
  - `13`
  - `14`
  - `"Fizz Buzz"`

---
"""


def fizz_buzz(number):
  # go through all numbers up to and including target number
  for num in range(1, number + 1):
    # if divisible by both --> "Fizz Buzz"
    if (num % 3 == 0 and num % 5 == 0):
      print("Fizz Buzz")
    # if divisible by 3 --> "Fizz"
    elif (num % 3 == 0):
      print("Fizz")
    # if divisible by 5 --> "Buzz"
    elif (num % 5 == 0):
      print("Buzz")
    # otherwise print the original number
    else:
      print(num)