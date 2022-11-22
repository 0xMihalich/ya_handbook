abc = [None, None, None]

abc[0] = int(input())
abc[1] = int(input())
abc[2] = int(input())

abc.sort()
a, b, c = abc

crc_1 = (a ** 2) + (b ** 2)
crc_2 = c ** 2

if crc_1 > crc_2:
    print('крайне мала')
elif crc_1 < crc_2:
    print('велика')
elif crc_1 == crc_2:
    print('100%')
