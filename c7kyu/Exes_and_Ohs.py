def xo(s):
    amount = {'x': 0, 'o': 0}
    for i in s:
        if i.lower() == 'x':
            amount['x'] += 1
        elif i.lower() == 'o':
            amount['o'] += 1

    return amount['x'] == amount['o']