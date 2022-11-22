N = int(input())
M = int(input())
T = int(input())
min_sum = M + T
hour = (N + (min_sum // 60)) % 24
minute = min_sum % 60
print(f'{hour:02d}:{minute:02d}')
