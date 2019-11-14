import random

def decorator_wrapper(fn):
    def decorator_modifying_fn(*args,**kwargs):
        print("Before calling " + fn.__name__)
        print(fn(*args,**kwargs))
        print("After calling " + fn.__name__)
        print()
        return None
    return decorator_modifying_fn

@decorator_wrapper
def test():
    print("Hello everyone")

@decorator_wrapper
def test2():
    print("Hello again")

test2()

# print(random.random())
my_random_fn = decorator_wrapper(random.random)
my_random_fn()

my_randint_fn = decorator_wrapper(random.randint)
my_randint_fn(a=10,b=100)