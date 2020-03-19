def move_zeros(array):
    res = []
    length = len(array)
    for i, el in enumerate(array[::-1]):
        # print(isinstance(el, bool), isinstance(el, int))
        if el == 0 and not isinstance(el, bool):
            res.append(0)
            array.pop(length - i - 1)
    return array + res

if __name__ == "__main__":
    print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
    print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
    print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
