a = int(input())
b = int(input())
result = 0
for i in (1, 10, 100):
    out_a = a // i % 10
    out_b = b // i % 10
    sum_ab = (out_a + out_b) % 10 * i
    result += sum_ab
print(result)
