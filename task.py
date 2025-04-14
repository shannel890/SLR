nums = [1,2,3,4,5,6,7,8,9,10,11]

nums = [x ** 2 for x in nums] 
print(nums)

def func(x=[]):

    x.append(1)
    return x
print(func())
print(func())

def fibonacci(n):
    a,b =0,1
    result = []
    for i in range(n):
        result.append(a)
        a,b = b,a+b
    return result
print(fibonacci(10))

nums = lambda x,y:max(x,y)
print(nums(4,5))

print(2 ** 3)
def gen():
    yield 1
    yield 2
g = gen()
print(next(g))
print(next(g))

nums = [x for x in range(5) if x % 2 == 0]
print(nums)
a = 5
print(type(a))  # <class 'int'>

a = 'five'
print(type(a))  # <class 'str'>
a = 5.0

def func(a,L=[]):
    L.append(a)
    return L
print(func(1))
print(func(2))
print(func(3))

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hello():
    print("Hello!")

say_hello()
print({True: 'yes', 1: 'no', 1.0: 'maybe'})

bool([]) is False

a = [1, 2, 3]
b = a
a += [4, 5]
print(b)

