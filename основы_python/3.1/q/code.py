string = input().lower().replace(' ', '')
print('YES' if string == string[::-1] else 'NO')
