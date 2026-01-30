import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(self.abc)
        print(f"Before calling {func.__name__}")
        result = func(self, *args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

class MyClass:
    def __init__(self):
        self.abc = "5"
    def my_method(self, value):
        return f"Original method executed with {value}"

MyClass.my_method = my_decorator(MyClass.my_method)
obj = MyClass()
print(obj.my_method(10))