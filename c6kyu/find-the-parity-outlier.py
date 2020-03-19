def find_outlier(integers):
    even_flag = 0 #  flag > 0 if even and flag < 0 if odd
    for i in range(3):
        if integers[i] % 2 == 0:
            even_flag += 1
        else:
            even_flag -= 1
    if even_flag > 0:
        searching_remainder = 1
    else:
        searching_remainder = 0
    for i in integers:
        if i % 2 == searching_remainder:
            return i
    return None
