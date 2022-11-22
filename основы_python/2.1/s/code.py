name = input()
price = int(input())
wt = int(input())
cash = int(input())
total = wt * price
result = cash - total
cost = f'{wt}кг * {price}руб/кг'
print(f'{"Чек":=^35}')
print(f'Товар:{name:>29}')
print(f'Цена:{cost:>30}')
print(f'Итого:{total:>26}руб')
print(f'Внесено:{cash:>24}руб')
print(f'Сдача:{result:>26}руб')
print(f'{"":=^35}')
