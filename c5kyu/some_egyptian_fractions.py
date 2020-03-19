def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return 1
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def decompose(n):
    decomposition = list()
    if '.' in n:
        a, b = n.split('.')
        denominator = 10 ** len(b)
        numerator = int(a) * denominator + int(b)
    elif '/' in n:
        a, b = n.split('/')
        numerator = int(a)
        denominator = int(b)
    else:
        numerator = int(n)
        denominator = 1

    if numerator >= denominator:
        decomposition.append(f"{numerator // denominator}")
        numerator -= (numerator // denominator) * denominator
    k = 2
    print(f"{numerator}/{denominator}")
    while numerator > 0:
        if numerator * k >= denominator:
            decomposition.append("1/" + str(k))
            numerator = numerator * k - denominator
            denominator *= k
            print(decomposition[-1])
            common_divisor = gcd(numerator, denominator)
            if common_divisor != 1:
                numerator //= common_divisor
                denominator //= common_divisor
            if numerator == 1:
                decomposition.append(f"{numerator}/{denominator}")
                return decomposition
            k = denominator // numerator if numerator != 0 else k + 1
        else:
            k += 1
    return decomposition


if __name__ == "__main__":
    print(decompose('20/23'))