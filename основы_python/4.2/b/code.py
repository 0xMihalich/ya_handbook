def make_matrix(size, value=0):
    if isinstance(size, int):
        size = (size, size)
    return [[value for j in range(size[0])] for i in range(size[1])]
