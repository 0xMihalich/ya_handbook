def roots(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 'Infinite solutions'
    elif a == 0 and b == 0:
        return 'No solution'
    elif a == 0:
        x = -c / b
        return f'{x:.2f}'
    d = b ** 2 - 4 * a * c
    if d > 0:
        x = [None, None]
        x[0] = (-b + d ** 0.5) / (2 * a)
        x[1] = (-b - d ** 0.5) / (2 * a)
        x.sort()
        return f'{x[0]:.2f} {x[1]:.2f}'
    elif d == 0:
        x = -b / (2 * a)
        return f'{x:.2f}'
    return 'No solution'


a = float(input())
b = float(input())
c = float(input())
print(roots(a, b, c))
