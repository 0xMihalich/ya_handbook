def modern_print(string):
    global string_list
    if string not in string_list:
        print(string)
        string_list.append(string)


string_list = []
