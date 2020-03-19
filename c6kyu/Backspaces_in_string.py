def clean_string(s):
    res = list()
    for i, symb in enumerate(s):
        if symb != '#':
            res.append(symb)
        else:
            if len(res) > 0:
                res.pop()
    return "".join(res)


clean_string('abc#d##c')
