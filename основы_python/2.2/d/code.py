petya = int(input())
vasya = int(input())
tolya = int(input())
userdict = {petya: 'Петя', vasya: 'Вася', tolya: 'Толя'}
userlist = [petya, vasya, tolya]
userlist.sort(reverse=True)
for num, user in enumerate(userlist):
    print(f'{num + 1}. {userdict[user]}')
