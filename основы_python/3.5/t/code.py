from ctypes import c_ushort


with open('numbers.num', 'rb') as f:
    nums = f.read()
result = sum([int.from_bytes(nums[i: i + 2], 'big') for i in range(0, len(nums), 2)])
print(c_ushort(result).value)
