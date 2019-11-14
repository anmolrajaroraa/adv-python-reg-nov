def outer():
    x = 10
    def inner():
        print(x)

    # inner()
    return inner


inner = outer()
inner()
# print(x)