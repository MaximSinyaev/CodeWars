""""
Description:

In this Kata, you will create a function that converts a string with letters and
numbers to the inverse of that string (with regards to Alpha and Numeric
characters).

So, e.g. the letter a will become 1 and number 1 will become a; z will become 26
 and 26 will become z.
"""


def AlphaNum_NumAlpha(string):
    i = 0
    res = ""
    alpha_base_zero = ord('a') - 1
    while i < len(string):
        if string[i].isalpha():
            res += str(ord(string[i]) - alpha_base_zero)
        else:
            if i + 1 < len(string) and string[i: i + 2].isdigit() \
                    and int(string[i: i + 2]) <= 26:
                res += chr(int(string[i: i + 2]) + alpha_base_zero)
                i += 2
                continue
            else:
                res += chr(int(string[i]) + alpha_base_zero)
        i += 1
    return res


if __name__ == "__main__":
    print(AlphaNum_NumAlpha('e1h16q'))
