def recursive_sum(*num):
    if len(num) == 1:
        return num[0]
    num = list(num)
    x = num.pop()
    num[-1] = num[-1] + x
    return recursive_sum(*num)
