from inspect import signature


def check_types(func):
    def wrapper(*args, **kwargs):
        argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
        for i, arg in enumerate(args):
            arg_name = argnames[i]
            s = signature(func)
            expected_type = s.parameters[arg_name].annotation
            actual_type = type(arg)

            if isinstance(arg, expected_type):
                result = func(*args, **kwargs)
                print(result)
                return result
            else:
                print(f"TypeError: Argument {arg} must be "
                      f"{expected_type.__name__} not {actual_type.__name__}")

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
add("1", "2")
