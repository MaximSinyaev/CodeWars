"""
Description:

For this task you are required to take a continuous string that can consist of
any combination of words or characters and then convert the words that make up
this string into hexadecimal values that could then be read as colour values.

Each word will represent a hexadecimal value by taking the first three letters
of each word and find the ASCII character code for each character. This will
then give you one hexadecimal value that represents the colours red, green or
blue. You will then combine these values into one readable RGB hexadecimal
value, ie, #ffffff.
"""


def words_to_hex(words):
    words = words.split()
    first_char = "#"
    res = list()
    for word in words:
        word_hex = first_char
        if len(word) < 3:
            for i in range(len(word)):
                word_hex += f"{ord(word[i]):x}"
            for _ in range(3 - len(word)):
                word_hex += "00"
        else:
            for i in range(3):
                word_hex += f"{ord(word[i]):x}"
        res.append(word_hex)
    return res


if __name__ == "__main__":
    print(words_to_hex("Hello, my name is Gary and I like cheese."))
