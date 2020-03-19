def zero(*args): return 0 if not args else args[0](0)
def one(*args): return 1 if not args else args[0](1)
def two(*args): return 2 if not args else args[0](2)
def three(*args): return 3 if not args else args[0](3)
def four(*args): return 4 if not args else args[0](4)
def five(*args): return 5 if not args else args[0](5)
def six(*args): return 6 if not args else args[0](6)
def seven(*args): return 7 if not args else args[0](7)
def eight(*args): return 8 if not args else args[0](8)
def nine(*args): return 9 if not args else args[0](9)


def plus(arg): return lambda x: x + arg
def minus(arg): return lambda x: x - arg
def times(arg): return lambda x: x * arg
def divided_by(arg): return lambda x: x // arg


if __name__ == "__main__":
    print(five(times(five())))
