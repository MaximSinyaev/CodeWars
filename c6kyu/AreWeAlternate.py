"""
Description:
Create a function isAlt() that accepts a string as an argument and
validates whether the vowels (a, e, i, o, u) and consonants are in alternate
order.
"""

from string import ascii_lowercase
vowels = 'aeiou'

def is_alt(s):
    s = s.lower()
    sign = None
    vowel_flag = 0
    not_vowel_flag = 0
    for letter in s:
        if letter in vowels:
            if vowel_flag:
                return False
            vowel_flag = 1
            not_vowel_flag = 0
        else:
            if not_vowel_flag:
                return False
            not_vowel_flag = 1
            vowel_flag = 0
    return True

if __name__ == "__main__":
    print(is_alt("orange"))
    print(is_alt("apple"))
    print(is_alt("banana"))
