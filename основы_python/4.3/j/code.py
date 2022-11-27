def make_linear(lst):
    result = []
    for el in lst:
        if isinstance(el, list):
            result += make_linear(el)
        else:
            result.append(el)
    return result
