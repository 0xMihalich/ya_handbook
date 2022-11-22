name = input()
price = int(input())
wt = int(input())
total = wt * price
cash = int(input())
result = cash - total
print(f'''Чек
{name} - {wt}кг - {price}руб/кг
Итого: {total}руб
Внесено: {cash}руб
Сдача: {result}руб''')
