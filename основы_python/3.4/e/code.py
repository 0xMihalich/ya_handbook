shopping = sorted(list(set(input().split(', ') + input().split(', ') + input().split(', '))))
nums = range(1, len(shopping) + 1)
for num, item in zip(nums, shopping):
    print(f'{num}. {item}')
