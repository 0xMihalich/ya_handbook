def cesar(string, step):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''
    for i in string:
        letter = i
        if i.lower() in alphabet:
            letter = alphabet[(alphabet.index(i.lower()) + step) % 26]
            if i.isupper():
                letter = letter.upper()
        result += letter
    return result


step = int(input())

with open("public.txt", "r", encoding="UTF-8") as file_in:
    with open("private.txt", "w", encoding="UTF-8") as file_out:
        file_out.write(cesar(file_in.read(), step))
