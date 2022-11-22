while (string := input()) != '':
    comm = string.find('#')
    if comm == 0:
        continue
    elif comm != -1:
        string = string[:comm]
    print(string)
