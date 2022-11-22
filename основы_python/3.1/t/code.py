# при проверке яндексом не проходит 9 тест, задан вопрос поддержке, поскольку считаю данное решение верным
from math import factorial


polsk_calc = []
s = input().split()
for x in s:
    if x == '+':
        g = polsk_calc.pop()
        z = polsk_calc.pop()
        polsk_calc.append(z + g)
    elif x == '-':
        g = polsk_calc.pop()
        z = polsk_calc.pop()
        polsk_calc.append(z - g)
    elif x == '*':
        g = polsk_calc.pop()
        z = polsk_calc.pop()
        polsk_calc.append(z * g)
    elif x == '/':
        g = polsk_calc.pop()
        z = polsk_calc.pop()
        polsk_calc.append(z // g)
    elif x == '~':
        g = polsk_calc.pop()
        polsk_calc.append(g * -1)
    elif x == '!':
        g = polsk_calc.pop()
        polsk_calc.append(factorial(g))
    elif x == '#':
        polsk_calc.append(polsk_calc[-1])
    elif x == '@':
        g = polsk_calc.pop(-3)
        polsk_calc.append(g)
    else:
        polsk_calc.append(int(x))
print(polsk_calc[0])
