def check_types(func):
    def wrapper(*args, **kwargs):
        arg_status = [isinstance(arg, int) for arg in args]
        args_status = all(arg_status)
        if args_status == True:
            func(*args, **kwargs)
            print(func(*args, **kwargs))
        else:
            print("TypeError: Arguments must be int not str")
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
add("1", "2")
