from string import digits

incrementing_order_digits = digits[1:] + '0'
decrementing_order_digits = digits[-1:0:-1] + '0'


def check_awesome(n):
    n_str = str(n)
    if len(n_str) < 3:
        return 0
    # Number with all zeros beside first digit
    if n_str[1:] == '0' * (len(n_str) - 1):
        return 1
    # Number with all the same digits
    if n_str == n_str[0] * len(n_str):
        return 1
    # Number has incrementing order of digits
    if n_str in incrementing_order_digits:
        return 1
    # Number has decrementing order of digits
    if n_str in decrementing_order_digits:
        return 1
    # Number is palindrome
    if n_str[:len(n_str) // 2] == n_str[-1:len(n_str) // 2: -1]:
        return 1
    return 0


def is_interesting(number, awesome_phrases):
    if check_awesome(number) or number in awesome_phrases:
        return 2
    for i in range(number + 1, number + 3):
        if check_awesome(i) or i in awesome_phrases:
            return 1
    return 0


if __name__ == "__main__":
    tests = [
        {'n': 3, 'interesting': [1337, 256], 'expected': 0},
        {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
        {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
        {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
        {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
        {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
    ]
    for t in tests:
        print(is_interesting(t['n'], t['interesting']))
        assert is_interesting(t['n'], t['interesting']) == t['expected']
