side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

check_1 = (side_1, side_2 + side_3)
check_2 = (side_2, side_1 + side_3)
check_3 = (side_3, side_1 + side_2)

if all(check[0] < check[1] for check in (check_1, check_2, check_3)):
    print('YES')
else:
    print('NO')
