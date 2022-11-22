num_1 = input()
num_2 = input()
nums = [int(n) for n in list(num_1 + num_2)]
nums.sort()
result = int(f'{nums[-1]}{(nums[1] + nums[2]) % 10}{nums[0]}')
print(result)
