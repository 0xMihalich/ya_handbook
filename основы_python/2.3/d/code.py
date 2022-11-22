num_1 = int(input())
num_2 = int(input())
reverse = False
if num_2 < num_1:
    num_1, num_2 = num_2, num_1
    reverse = True

result = [*range(num_1, num_2)] + [num_2]
result.sort(reverse=reverse)
print(" ".join(str(i) for i in result))
