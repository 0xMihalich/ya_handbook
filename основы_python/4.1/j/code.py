# Снова ошибка при выполнении функции, хотя функция работает. Так же задан вопрос поддержке
def merge(tuple_1, tuple_2):
    return tuple(sorted(list(set(tuple_1) | set(tuple_2))))

assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
