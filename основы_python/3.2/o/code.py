result = []
for num in input().split():
    binary = list(bin(int(num))[2:])
    result.append({'digits': len(binary), 'units': binary.count('1'), 'zeros': binary.count('0')})
print(result)
