# снова получаю ошибку при прохождении тестов, есть предположение на ошибку со стороны яндекс, отправлен запрос в ТП

# решение 1
with open('numbers.num', 'rb') as f:
    nums = f.read()
print(sum([int.from_bytes(nums[i: i + 2], 'big') for i in range(0, len(nums), 2)]))

# решение 2
from struct import unpack


with open('numbers.num', 'rb') as f:
    nums = f.read()
print(sum([unpack('>h', nums[i: i + 2])[0] for i in range(0, len(nums), 2)]))
