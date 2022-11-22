while (string := input()) != '':
    if string[:2] == '##':
        string = string[2:]
    if string[-3:] == '@@@':
        continue
    print(string)
