def merge(tuple_1, tuple_2):
    result = list(tuple_1) + list(tuple_2)
    n = 1
    while n < len(result):
        for i in range(len(result) - n):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
        n += 1
    return tuple(result)
