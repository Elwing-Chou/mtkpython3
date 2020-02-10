a = print
a("hello")

def test():
    return print
test()("hello")

# Decorator
def deco(func):
    def wrap():
        print(func.__name__)
        return func()
    return wrap

@deco
def test2():
    return 3

@deco
def test3():
    return 4

print(test2())
print(test3())