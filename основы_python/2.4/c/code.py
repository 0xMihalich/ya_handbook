range_start = 1
num_list = [str(i + 1) for i in range(int(input()))]
while True:
    if not num_list:
        break
    print(' '.join(num_list[:range_start]))
    num_list = num_list[range_start:]
    range_start += 1
