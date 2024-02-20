# No return type with Arguments
# multiple arguments

def say_hello(name, age):
    print("Hey my name is", name, "and my age is", age)


say_hello(name="Subham", age=29)


def say_hello_args(name, age):
    print("hello", name, age)


say_hello_args("Subham", 30)


def f1(a, b, c):
    return a + b + c


r = f1(1, 2, 3)

print(r)
