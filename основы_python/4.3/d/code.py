def answer(foo):
    def foo_wrapper(*args, **kwargs):
        return f"Результат функции: {foo(*args, **kwargs)}"
    return foo_wrapper
