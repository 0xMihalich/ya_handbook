files = []

for file in range(2):
    files.append(input())

result = input()
words = []

for file in files:
    with open(file, 'r', encoding="UTF-8") as f_in:
        file_words = []
        for line in f_in.readlines():
            file_words += line.split()
        words.append(set(file_words))

with open(result, 'w', encoding="UTF-8") as f_out:
    for word in sorted(list(words[0] ^ words[1])):
        f_out.write(word + '\n')
