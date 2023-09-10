import time


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(func(*args, **kwargs))
        print(f"Execution time: {execution_time} seconds")
    return wrapper


@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
