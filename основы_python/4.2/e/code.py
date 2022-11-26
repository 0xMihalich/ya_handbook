def to_string(*data, sep=' ', end='\n'):
    return sep.join([f'{d}' for d in data]) + end
