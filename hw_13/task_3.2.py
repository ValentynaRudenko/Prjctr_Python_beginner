def check_types(func):
    def wrapper(*args, **kwargs):
        errors_count = 0
        for arg in args:
            if type(arg) != int:
                print(f"TypeError: Argument {arg} must be int not {type(arg).__name__}")
                errors_count += 1   
        if errors_count == 0:
            func(*args, **kwargs)
            print(func(*args, **kwargs))
    return wrapper



@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
add("1", "2")
