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

    def wrapper():
        lst_h = ["Hello\n", "Hi\n", "Good morning\n"]
        h = random.choice(lst_h)

        original = function()

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
    
    def wrapper():
        start = time.time()
        original = function()
        end = time.time()
        duration = round(end - start, 2)
        improved = f"the result is: {original}\nThe function took {duration} seconds to run."
        return improved
    return wrapper


# @runtime_decorator
# def sum_num():
#     total = 0
#     for item in range(1, 100000001):
#         total += item
#     return total

# a = sum_num()
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


def sum_num():
    total = 0
    for item in range(1, 1001):
        total += item
    return total