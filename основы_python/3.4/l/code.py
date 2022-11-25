shopping = []
for i in range(int(input())):
    shopping += input().split(', ')
shopping = sorted(shopping)
nums = range(1, len(shopping) + 1)
for num, shop in zip(nums, shopping):
    print(f'{num}. {shop}')
