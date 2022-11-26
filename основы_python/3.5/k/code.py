import json


file_in = input()
file_out = input()

with open(file_in, 'r', encoding="UTF-8") as file:
    nums = []
    for line in file.readlines():
        nums += [int(num) for num in line.split()]

count = len(nums)
positive_count = len([num for num in nums if num > 0])
min_ = min(nums)
max_ = max(nums)
sum_ = sum(nums)
average = round(sum_ / count, 2)

records = {"count": count, "positive_count": positive_count, "min": min_,
           "max": max_, "sum": sum_, "average": average}

with open(file_out, "w", encoding="UTF-8") as json_out:
    json.dump(records, json_out, ensure_ascii=False, indent=4)
