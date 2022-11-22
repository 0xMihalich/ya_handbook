friend_list = {}
while (strings := input()) != '':
    people_1, people_2 = strings.split()
    friends_1 = friend_list.get(people_1)
    if not friends_1:
        friends_1 = []
    friends_1.append(people_2)
    friends_2 = friend_list.get(people_2)
    if not friends_2:
        friends_2 = []
    friends_2.append(people_1)
    friend_list.update({people_1: friends_1, people_2: friends_2})
friend_list = dict(sorted(friend_list.items()))
for people, friends in friend_list.items():
    second_friends = set()
    for friend in friends:
        for second_friend in friend_list[friend]:
            if second_friend != people and second_friend not in friends:
                second_friends.add(second_friend)
    second_friends = list(second_friends)
    second_friends.sort()
    print(f"{people}: {', '.join(second_friends)}")
