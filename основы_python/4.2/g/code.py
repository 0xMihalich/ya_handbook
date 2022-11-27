def enter_results(*result):
    global result_1, result_2
    for num in result[0::2]:
        result_1.append(num)
    for num in result[1::2]:
        result_2.append(num)


def get_sum():
    global result_1, result_2
    if not result_1 and not result_2:
        return ()
    return round(sum(result_1), 2), round(sum(result_2), 2)


def get_average():
    global result_1, result_2
    if not result_1 and not result_2:
        return ()
    return round(sum(result_1) / len(result_1), 2), round(sum(result_2) / len(result_2), 2)


result_1, result_2 = [], []
