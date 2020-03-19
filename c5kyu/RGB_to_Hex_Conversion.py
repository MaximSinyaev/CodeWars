HEX_BASE = '0123456789ABCDEF'


def rgb(r, g, b):
    result = ""
    for color in [r, g, b]:
        if color < 0:
            color = 0
        elif color > 255:
            color = 255
        # print(color)
        result += HEX_BASE[color // 16] + HEX_BASE[color % 16]
    return result


print(rgb(-20,275,125))