nums = (int(i) for i in input().split())
degree = int(input())
print(' '.join(str(num ** degree) for num in nums))
