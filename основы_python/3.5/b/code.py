from sys import stdin


result = []
for line in stdin:
    nums = line.split()
    result.append(int(nums[2]) - int(nums[1]))
mid = 0
for middle in result:
    mid += middle
print(round(mid / len(result)))
