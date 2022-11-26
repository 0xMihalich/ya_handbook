result = []
with open("secret.txt", "r", encoding="UTF-8") as file_out:
    for strings in file_out.readlines():
        out = ''
        for i in strings.replace('\n', ''):
            if ord(i) < 128:
                out += i
                continue
            out += ord(i).to_bytes(2, byteorder='little')[:1].decode()
        result.append(out)
for out in result:
    print(out)
