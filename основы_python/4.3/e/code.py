def result_accumulator(foo):
    def foo_wrapper(*args, method="accumulate"):
        global accumulator
        result = accumulator.get(foo.__name__)
        if not result:
            result = []
        result.append(foo(*args))
        if method == "drop":
            accumulator.update({foo.__name__: []})
            return result
        accumulator.update({foo.__name__: result})
    return foo_wrapper


accumulator = {}
