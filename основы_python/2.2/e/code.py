N = int(input())
M = int(input())
petya = 7
vasya = 6
petya -= 3
vasya += 3
petya += 2
vasya += 5
vasya -= 2
petya += N
vasya += M
if petya > vasya:
    print('Петя')
elif petya < vasya:
    print('Вася')
else:
    print('Оба')
