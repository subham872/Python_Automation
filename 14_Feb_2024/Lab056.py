# *Agrs & **Kargs

#*args is basically passing any number of arguments

def my_arguments(*args):
    for i in args:
        print(i)

my_arguments(1)
my_arguments(1,2)
my_arguments(1,2,3,4,)
my_arguments(1,2,3,4,5,)

def make_pizza(*toppings):
    for topp in toppings:
        print(topp)

make_pizza("bread","bun","paneer","sauce")