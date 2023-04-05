# functions

# allow you to follow DRY

# DONT REPEAT YOURSELF
# def print_something():
#     print("something")
#
# print_something()
# print_something()
# print_something()

def print_something(print_string):
    print(print_string)

print_something("something 1")
print_something("something 2")

def greeting(name):
    print("hello, my name is " + name)

greeting("Phil")


# return statement

def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))

# default arguments

def addition(int1=2, int2=2):
    return int1 + int2

print(addition(10, 2))

# multiple arguments

def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5)

# type hints

# def greeting(name: str):
#     print("hello, my name is " + name)
#
# greeting(4545)

def division(denum: int, num: int) -> float:
    return denum / num

print(division(12, 5))


def subtraction(int1: int = 5, int2: int = 2) -> int:
    return int1 - int2

print(type(subtraction))

# functions best practices

# 1. name your methods using lowercase and underscores
# 2. all arguments should be clkear in their need and where possible their expected type
# 3. rememnber the return statement or your function will return none in most cases
# 4. keep your functions as small as possible, and keep them readable
# 5. use comments within your methods to help with instructions on how to use them
# 6 consider using type hints to avoid  errors 