num = int(input())
result = {}
for i in range(2, 11):
    check = num
    i_result = 0
    while check > 0:
        i_result += check % i
        check //= i
    if i_result not in result:
        result.update({i_result: i})

print(result[max(result)])
