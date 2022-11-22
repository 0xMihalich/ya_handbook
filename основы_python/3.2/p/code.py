places = set()
while (strings := input()) != '':
    place = strings.split()
    stop = len(place) - 1
    for num, word in enumerate(place):
        if word == 'зайка':
            if num == 0:
                places.add(place[1])
            elif num == stop:
                places.add(place[-2])
            else:
                places.add(place[num + 1])
                places.add(place[num - 1])
for word in places:
    print(word)
