filename = input()
with open(filename, 'r', encoding="UTF-8") as file:
    nums = []
    for line in file.readlines():
        nums += [int(num) for num in line.split()]
print(len(nums))
print(len([num for num in nums if num > 0]))
print(min(nums))
print(max(nums))
print(sum(nums))
print(f'{sum(nums) / len(nums):.2f}')
