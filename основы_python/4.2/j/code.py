from itertools import cycle


def secret_replace(text, **kwargs):
    text = list(text)
    for args in kwargs:
        rep = cycle(kwargs[args])
        for num, letter in enumerate(text):
            if letter == args:
                text[num] = next(rep)
    return ''.join(text)
