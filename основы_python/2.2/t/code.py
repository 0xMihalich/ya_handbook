strings = (input(), input(), input())
matched = [string for string in strings if 'зайка' in string]
result = min(matched)
print(result, len(result))
