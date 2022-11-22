place = []
while (string := input()) != '':
    place += string.split()
for i in set(place):
    print(i, place.count(i))
