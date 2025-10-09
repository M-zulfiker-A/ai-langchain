def logger(func):
    print(func.__name__)
    return func

@logger
def add(x, y):
    return x + y

print(add(2, 3))