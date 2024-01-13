"""
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
"""

# Closures - Technique by which the data is attached to some code even after end of those other original functions
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 
"""
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
"""


import logging

from cirq import Y
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))

        print(func(*args))

        #Necessary for closure to work (No paranthesis)
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y 

add_logger = logger(add)
add_logger(3, 3)
add_logger(4, 4)

sub_logger = logger(sub)
sub_logger(20, 10)
sub_logger(10, 5)