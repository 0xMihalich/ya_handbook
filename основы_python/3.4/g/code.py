from itertools import combinations


gamers = []

for i in range(int(input())):
    gamers.append(input())

for gamer_1, gamer_2 in combinations(gamers, 2):
    print(gamer_1, '-', gamer_2)
