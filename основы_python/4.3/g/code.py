def same_type(foo):
    def foo_wrapper(*args):
        check = type(args[0])
        for arg in args:
            if not isinstance(arg, check):
                print('Обнаружены различные типы данных')
                return
        return foo(*args)
    return foo_wrapper
