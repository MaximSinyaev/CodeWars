""""
Description:
A rectangle with sides equal to even integers a and b is drawn on the Cartesian
plane. Its center (the intersection point of its diagonals) coincides with the
point (0, 0), but the sides of the rectangle are not parallel to the axes;
instead, they are forming 45 degree angles with the axes.

url: https://www.codewars.com/kata/5886e082a836a691340000c3/train/python
"""

square_diagonal = 2 ** 0.5


def rectangle_rotation(a, b):
    a //= 2
    b //= 2
    # Main diagonal
    d1 = (1 + a // square_diagonal * 2) * (1 + b // square_diagonal * 2)
    # Additional diag
    d2 = (1 + (a - 0.7) // square_diagonal) * 2 * \
         (1 + (b - 0.7) // square_diagonal) * 2
    return int(d1 + d2)


if __name__ == "__main__":
    print(rectangle_rotation(6, 4), 23)
    print(rectangle_rotation(30, 2), 65)
    print(rectangle_rotation(8, 6), 49)
    print(rectangle_rotation(16, 20), 333)
