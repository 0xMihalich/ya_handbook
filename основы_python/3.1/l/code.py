kasha = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
days = int(input())
kasha = kasha * (days // len(kasha) + 1)
for i in range(days):
    print(kasha[i])
