from sys import stdin


palindroms = set()
for line in stdin:
    for word in line.split():
        if word.lower() == word.lower()[::-1]:
            palindroms.add(word)
for word in sorted(list(palindroms)):
    print(word)
