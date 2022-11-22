elf = input()
gnome = input()
human = input()

if all(elf[0] in num for num in (elf, gnome, human)):
    print(elf[0])
elif all(elf[1] in num for num in (elf, gnome, human)):
    print(elf[1])
else:
    print('NO')
