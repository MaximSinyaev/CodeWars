def valid_parentheses(string):
    stack = list()
    for symb in string:
        if symb == '(':
            stack.append('(')
        elif symb == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True if not stack else False


if __name__ == "__main__":
    print(valid_parentheses("  ("))
    assert valid_parentheses("  (") is False
    assert valid_parentheses(")test") is False
    assert valid_parentheses("") is True
    assert valid_parentheses("hi())(") is False
    assert valid_parentheses("hi(hi)()") is True