import random

""""
def lottery():
    #returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    #returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
    print("And the next number is... %d!" % (random_number))
"""

def fib():
    a, b = 1, 1
    while 1: 
        yield a
        a, b = b, a+b

import types
if type(fib()) == types.GeneratorType:
    print("Good, The Fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

# yield is like a return statement, except its an iteratble object so it can output multiple things sorta