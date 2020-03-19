def countBits(n):
    pow = 0
    base = 2
    res = 0
    while base ** pow < n:
        pow += 1
    while n:
        greatest_divisor = base ** pow
        if greatest_divisor <= n:
            n -= greatest_divisor
            res += 1
        pow -= 1
    return res