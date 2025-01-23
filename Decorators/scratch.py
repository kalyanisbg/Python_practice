
def fn_call_announcement(function):
    def wrapper(*args, **kwargs):
        print(f"{function}() has been called")
        function(*args, **kwargs)
        print(f"end of {function}()")
    return wrapper

@fn_call_announcement
def add_and_subtract(a: float, b:float) -> float:
    return a+b, abs(a-b)


add_and_subtract(4, 5)