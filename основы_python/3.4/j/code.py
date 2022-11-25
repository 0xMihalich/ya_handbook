from itertools import product


juice = int(input())
nums = range(1, juice)

print('А Б В')
for a, b, c in product(nums, nums, nums):
    if a + b + c == juice:
        print(a, b, c)
