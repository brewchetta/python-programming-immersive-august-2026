# Day Five - Algorithmic Problem Solving

## Topics

- Psuedo-coding as an approach
- Algorithmic problem solving

## **EXERCISE 01: Bill Calculator**

**PROBLEM STATEMENT:**

Let's imagine we're going out to eat at a restaurant; we just had a good meal and we want to calculate the bill. In essence, let's conceptualize and create a custom bill calculator in Python.

**OBJECTIVE:** Given a starting meal price (as a `float`) and a tip quantity (as an `int`) as well as a constant tax rate (as a `float`), calculate the total bill on purchased food.

**INPUT:** `calculate_bill(price_of_food=20.99, amount_tipped=5)`

**OUTPUT:** `27.826625`

---

## **EXERCISE 02: Character Counter**

**OBJECTIVE:** Given a string (e.g. `"hello world"`), we want to design a function/script that can count the frequency of unique characters in that string.

**INPUT:** `"data"`, `"DATA"`, `"Data"`

**OUTPUT:**
  - `"d": 1`
  - `"a": 2`
  - `"t": 1`
---

## **EXERCISE 03: Fizz(y) Buzz(y)**

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

## **EXERCISE 04: The ROT-13 Algorithm**

**OBJECTIVE:** Given some message (string) to encode, we want to design a function that changes every letter in the string to the letter that is `13` positions forward in the English alphabet.

**INPUT:** `"hello there"`

**OUTPUT:** `"uryyb gurer"`

---

## **BONUS 04: The ROT-N Algorithm**

**OBJECTIVE:** Given some message (a string) to encode, construct a class with the ability to apply a ROT substitution transformation to encrypt (or decrypt) the message with degree `N`.

**INPUT:** `"hello there"`, `13`

**OUTPUT:** `"uryyb gurer"`

---

## **EXERCISE 05: The Fibonacci Algorithm**

**OBJECTIVE:** Given an integer `N` representing the length of the sequence that we want to generate, output the value from the Fibonacci sequence at the corresponding position of `N`.

For more information on the Fibonacci sequence see this article: https://en.wikipedia.org/wiki/Fibonacci_sequence

**FIBONACCI SEQUENCE**:

- `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...`

**INPUT**: `fibonacci_of(N=10)`

**OUTPUT:** `55`

---