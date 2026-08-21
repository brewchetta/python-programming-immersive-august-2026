"""
## **EXERCISE: The ROT-13 Algorithm**

**OBJECTIVE:** Given some message (string) to encode, we want to design a function that changes every letter in the string to the letter that is `13` positions forward in the English alphabet.

**INPUT:** `"hello there"`

**OUTPUT:** `"uryyb gurer"`

a - 97 + 13
z - 122 + 13


---
"""

def rot_13(string:str):
    result = ""
    for character in string.lower():
        character_code = ord(character)
        if (character_code > 123 or character_code < 97):
            result += character
        elif (character_code >= 110):
            new_char_code = character_code - 13
            result += chr(new_char_code)
        else:
            new_char_code = character_code + 13
            result += chr(new_char_code)
    return result


"""
## **BONUS: The ROT-N Algorithm**

**OBJECTIVE:** Given some message (a string) to encode, construct a class with the ability to apply a ROT substitution transformation to encrypt (or decrypt) the message with degree `N`.

**INPUT:** `"hello there"`, `13`

**OUTPUT:** `"uryyb gurer"`

---
"""

def rot_n():
    pass