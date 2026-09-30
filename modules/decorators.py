################################## Decorators ##################################
import random
import time
import os
import math
# ------------------------------------------------------------------------------
# 1: Function accepts a function as an argument and returns a function as a result
def same(x):
    return x

def power(x):
    return x ** 2

def inverse(x):
    return 1 / x

def sum_num(function):
    total = 0
    for item in range(1, 1001):
        total += function(item)
    return total

# a = sum_num(same)                   # 1 + 2 + 3 + 4 + ... + 1000
# print(a)
# #
# a = sum_num(power)                   # 1 + 4 + 9 + 16 ... + 1000000
# print(a)
# #
# a = sum_num(inverse)                   # 1 + 1/2 + 1/3 + 1/4 ... + 1/1000
# print(a)
# #
# a = sum_num(math.sin)                # sin(1) + sin(2) + sin(3) + sin(4) ... + sin(1000)
# print(a)
#################################################################################
# 2: Function inside another function
#
def helo():
    def select():
        lst_h = ["Hello\n", "hi\n", "Good morning\n"]
        h = random.choice(lst_h)
        return h

    result = select() + "My name is Ari."
    return result

# a = helo()
# print(a)
#################################################################################
# 3:
#
def helo():
    def select():
        lst_h = ["Hello\n", "hi\n", "Good morning\n"]
        h = random.choice(lst_h)
        result = h + f"My name is Ari."
        return result

    return select
        

# a = helo()              # a ~ select
# b = a()
# print(a)
#################################################################################
# 4: Inner function can access the outer function's variables
#
def helo(name_x):
    def select():
        lst_h = ["Hello\n", "hi\n", "Good morning\n"]
        h = random.choice(lst_h)
        result = h + "My name is " + name_x + "."
        return result

    return select
        

# a = helo("Ari")              # a ~ select
# b = a()
# print(a)
################################## Decorators ##################################
import random


def hello_decorator(function):

    def wrapper(*args, **kwargs):
        lst_h = ["Hello\n", "Hi\n", "Good morning\n"]
        h = random.choice(lst_h)

        original = function(*args, **kwargs)

        lst_b = ["\nBye.", "\nGoodbye.", "\nSee you soon."]
        b = random.choice(lst_b)

        improved_result = h + str(original) + b
        return improved_result

    return wrapper


# @ hello_decorator                   # sum_num = hello_decorator(sum_num)
# def sum_num():
#     total = 0
#     for item in range(1, 1001):
#         total += item
#     return total

# a = sum_num()       # sum_num ~ wrapper
# print(a)
#################################################################################
# Q1: Run time decorator

def runtime_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        original = function(*args, **kwargs)  
        #          Tuble unpacking,     Dict unpacking
        end = time.time()
        duration = round(end - start, 2)
        improved = f"The result is: {original}\nTakes: {duration} seconds."
        return improved
    return wrapper


@runtime_decorator
def sum_num(x, y):
    total = 0
    for item in range(x, y +1):
        total += item
    return total

    
@runtime_decorator
def is_prime(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

# a = sum_num(y=5000, x=100)
# print(a)
#################################################################################
# Q2: Loop / Repeat decorator

def loop_decorator(function):
    def wrapper():
        lst = []
        for i in range(10):
            original = function()
            lst.append(original)
        return lst
    return wrapper


# @loop_decorator
# def sum_num():
#     total = 0
#     for item in range(1, 1001):
#         total += item
#     return total



# a = sum_num()
# print(a)
#################################################################################
# Q3:

# @loop_decorator
# @runtime_decorator
# def sum_num():
#     total = 0
#     for item in range(1, 1001):
#         total += item
#     return total

# a = sum_num()
# print(a)
#################################################################################
# Q4: Storage decorator
#
# Save the results so that the next we can use the results without running the function again.  

d = {}  # or      txt       sql     excel


# def sum_num():
#     total = 0
#     for item in range(1, 1001):
#         total += item
#     return total
#################################################################################
#
# Functions with unknown number of arguments
#
def sum_numbers(*args):             # <args> is a tuple
    result = 0
    for item in args:
        result += item
    return result

# s = sum_numbers(10, 50)
# print(s)
#################################################################################
#
# Functions with unknown keyboard arguments
#
def find_top(**kwargs):            # <kwargs> is a dictionary
    maxi = -1
    for k, v in kwargs.items():
        if v > maxi:
            maxi = v
            top = k
    return top

# a = find_top(printer = 1400, monitor = 1200, mouse = 100, keyboard = 200)
# print(a)

#################################################################################
# Default prameters
def azimi(x, y=1):      # Default follow non-default
    z = x / y
    return z

# a = azimi(5)
# print(a)
# b = azimi(5, 2) 
# print(b)
# ----------------------
def azimi(x, y):
    z = x / y
    return z


# a = azimi(x=2, y=5)     # Keyword arguments
# print(a)
# b = azimi(5, x=2)       # Error: Multiple value for X
# print(b)
# c = azimi(5, y=2)       # OK
# print(c)
# d = azimi(x=5, 2)       # Error: Keywords must follow positions
# print(d)