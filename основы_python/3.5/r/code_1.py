from os.path import getsize
from math import ceil


def filesize(size, value=0):
    sizes = {0: 'Б', 1: 'КБ', 2: 'МБ', 3: 'ГБ', 4: 'ТБ'}
    if size > 1024:
        value += 1
        return filesize(size / 1024, value)
    return f'{ceil(size)}{sizes[value]}'


print(filesize(getsize(input())))
