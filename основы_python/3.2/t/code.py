# решение проходит 19 тестов из 21, возможно, проблема со стороны яндекса
from math import gcd


nums = sorted(list(set(int(i) for i in input().split('; '))))
for a in nums:
    result = [str(b) for b in nums if gcd(a, b) == 1]
    if not result:
        continue
    print(f'{a} - {", ".join(result)}')
