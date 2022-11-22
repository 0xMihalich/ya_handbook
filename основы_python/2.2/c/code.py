petya = int(input())
vasya = int(input())
tolya = int(input())
maxuser = max(petya, vasya, tolya)
if maxuser == petya:
    print('Петя')
elif maxuser == vasya:
    print('Вася')
elif maxuser == tolya:
    print('Толя')
