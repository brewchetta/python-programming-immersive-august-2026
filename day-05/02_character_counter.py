"""
## **EXERCISE: Character Counter**

**OBJECTIVE:** Given a string (e.g. `"hello world"`), we want to design a function/script that can count the frequency of unique characters in that string.

**INPUT:** `"data"`, `"DATA"`, `"Data"`

**OUTPUT:**
  - `"d": 1`
  - `"a": 2`
  - `"t": 1`
---
"""

def character_counter(string:str):
    # empty dictionary - filled with letter / number pairs
    frequencies = {}
    # lower case the string so we don't count upper and lower letters differently
    lower_case_string = string.lower()

    # go through each character in the string
    for char in lower_case_string:
      # if it exists += 1
      if ( frequencies.get(char) ):
        frequencies[char] += 1
      # if not exists, add to dict
      else:
        frequencies[char] = 1

    # return frequencies as the final result
    return frequencies