from ctypes import c_ushort


with open('numbers.num', 'rb') as f:
    nums = f.read()

result = c_ushort()

for i in range(0, len(nums), 2):
    result.value += c_ushort(int.from_bytes(nums[i: i + 2], 'big')).value

print(result.value)
