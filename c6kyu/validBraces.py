"""
Description:
Write a function that takes a string of braces, and determines if the order of
the braces is valid. It should return true if the string is valid, and false if
it's invalid.

url: https://www.codewars.com/kata/5277c8a221e209d3f6000b56
"""

brackets = {
    "(": ")",
    "[": "]",
    "{": "}"
}

def validBraces(string):
    stack = list()
    for symb in string:
        if symb in brackets:
            stack.append(symb)
        elif symb in brackets.values():
            if stack and brackets[stack[-1]] == symb:
                stack.pop()
            else:
                return False
    return True if not stack else False
