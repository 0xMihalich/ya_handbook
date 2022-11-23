from itertools import islice


kasha_list = []
for i in range(int(input())):
    kasha_list.append(input())

kasha_days = int(input())
kasha_list = kasha_list * kasha_days

for i in islice(kasha_list, 0, kasha_days):
    print(i)
