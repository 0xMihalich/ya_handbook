text_in = input()
text_out = input()

result = []
with open(text_in, 'r', encoding="UTF-8") as f_in:
    for line in f_in.readlines():
        result.append(' '.join(line.split()))

with open(text_out, 'w', encoding="UTF-8") as f_out:
    for string in result:
        if string:
            f_out.write(string + '\n')
