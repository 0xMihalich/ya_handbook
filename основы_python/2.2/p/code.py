petya = int(input())
vasya = int(input())
tolya = int(input())
finishlist = [petya, vasya, tolya]
finishlist.sort(reverse=True)
finish = {petya: 'Петя', vasya: 'Вася', tolya: 'Толя'}
print(f'''{"":^8}{finish[finishlist[0]]:^8}{"":^8}
{finish[finishlist[1]]:^8}{"":^8}{"":^8}
{"":^8}{"":^8}{finish[finishlist[2]]:^8}
{"II":^8}{"I":^8}{"III":^8}''')
