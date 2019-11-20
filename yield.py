def calc(x,y):    #function generator
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    yield add
    yield sub
    yield mul
    yield div

# result = calc(10,20)
# print(result)
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())

for result in calc(10,20):
    print(result)