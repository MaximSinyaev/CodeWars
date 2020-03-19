from math import log

def zeros(n):
    if n <= 0:
        return 0
    sum = 0
    k_max = int(log(n, 5))
    for i in range(1, k_max + 1):
        sum += int(n / 5 ** i)
    return int(sum)


if __name__ == "__main__":
    for i in range(105):
        print(i, zeros(i))
