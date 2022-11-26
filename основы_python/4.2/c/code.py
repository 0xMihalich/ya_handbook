def gcd(*nods):
    a = nods[0]
    if len(nods) == 1:
        return a
    result = []
    for b in nods[1:]:
        a = nods[0]
        while a != 0 and b != 0:
            if a > b: 
                a = a - b
            else: 
                b = b - a 
        result.append(max(a, b))
    return min(result)
