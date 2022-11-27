def make_equation(*num):
    num = list(num)
    if len(num) == 1:
        return str(num[0])
    else:
        x = num.pop()
        return f'({make_equation(*num)}) * x + {x}'
