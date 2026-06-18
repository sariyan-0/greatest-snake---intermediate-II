############################### Programming Paradigmes ###############################

# Proceduarl Programming

# Functional Programming:
#                       map/filter/reduce/zip/lambda/comprehenstions





# map

# Lambda expressions / Inline functions / Unknown functions
lambda t: (9/5) * t + 32


lst_t = [10, 25, 65, 100]
lst_f = list(map(lambda t: (9/5) * t + 32, lst_t))
# print(lst_f)


# -------------------------------
# lst_t = [10, 25, 65, 100]
# lst_f = []
# for item in lst_t:
#     a = transform(item)
#     lst_f.append(a)
# print(lst_f)
######################################################################
# filter
# lambda x: x % 2 == 0

# lst_n = [10, 15, 19, 25, 100]
# lst_e = list(filter(lambda x: x % 2 == 0, lst_n))
# print(lst_e)  # [10, 100]
######################################################################
# reduce
from functools import reduce

# lst = [10, 50, 20, 100, 10, 10]

# total = reduce(lambda a, b: a + b   ,   lst)
# print(total)

# def sum_num(x, y):
#     return x + y

# total = reduce(sum_num, lst)
# print(total)    

# total = 0
# for item in lst:
#     total += item
# print(total)
######################################################################
# zip
# try and find the best mark of evey student in every report card
#          s0  s1  s2  s3  s4  s5  s6
lst_mid = [18, 12, 20, 19, 13, 19, 16]
lst_fin = [12, 14, 18, 20, 18, 13, 10]

# output:
#         [18, 14, 20, 20, 18, 19, 16]

# st = list(map(max, zip(lst_mid, lst_fin)))
# print(lst)

# lst = []
# for item in zip(lst_mid, lst_fin):
#     m = max(item)
#     lst.append(m)
# print(lst)

# ---------------------------------
# a = list(zip(lst_mid, lst_fin))
# print(a)
# ---------------------------------

# lst = []
# for i in range(7):
#     if lst_mid[i] > lst_fin [i]:
#         lst.append(lst_mid[i])
#     else:
#         lst.append(lst_fin[i])
# print(lst)
######################################################################
#
# lst = [10, 25, 65, 100]
#
# lst_f = [(9/5) * t + 32 + 32 for t in lst_t]
# print(lst_f)
#
# lst_a = [x ** 2 for x in range(10)]
# print(lst_a)
#
# lst_b = [z + 1/z for z in range(1,5)]
# print(lst_b)
#
# --------------------------------------------------------------------
# Q: Find the average of the students till two decimal point and round them up
# lst_marks = [18.434555, 19.234324, 20, 14.34234, 16.98312]

# lst = [round(mark, 2) for mark in lst_marks]
# print(lst)
######################################################################
# Q1: Find the divisors
# x = 12          # 1, 2, 3, 4, 6, 12

# divisors = list(filter(lambda i: x % i == 0, range(1, x + 1)))
# print(divisors)
######################################################################
# Q2: Find prime numbers
# x = 101
# p = len(list(filter(lambda i: x % i == 0, range (1, x + 1)))) == 2
# print(p)
######################################################################
# Q3: Find all prime numbers under 1000
# p = list(filter(lambda x: len(list(filter(lambda i: x % i == 0, range(1, x + 1)))) == 2, range(2, 1000)))
# print(p)
######################################################################
# Q4: Find the factorials
# 5! = 5 x 4 x 3 x 2 x 1
# x = 5

# fact = reduce(lambda a, b: a * b, range(1, x + 1))
# print(fact)

# fact = 1
# for i in range(1, x + 1):
#     fact = fact * i
# print(fact)
######################################################################
# Q5: Find the smallest item in the list
# lst = [12, 50, 4, 16, 80, 2, 90, 45]
# smallest = reduce(lambda a, b: a if a < b else b, lst)
# print(smallest) # 2
######################################################################
# Q6 try and find the best mark of evey student in every report card
#          s0  s1  s2  s3  s4  s5  s6
lst_mid = [18, 12, 20, 19, 13, 19, 16]
lst_fin = [12, 14, 18, 20, 18, 13, 10]

# output:
#         [18, 14, 20, 20, 18, 19, 16]

# lst = [max(pair) for pair in zip(lst_mid, lst_fin)]
# print(lst)  # [18, 14, 20, 20, 18, 19, 16]
#
lst = [round((a + b)/2, 1) for a, b in zip(lst_mid, lst_fin)]
print(lst)
# ---------------------------------------------------------------------
# Dixtionary Comprehention
#   Key:  Value
d = {num: num +100 for num in range(10)}
print(d)
# ---------------------------------------------------------------------
lst_names = ["Joe", "Ali", "Bob", "Jake"]
lst_marks = [ 18,    17,    19,    14]
#
d = {k: v for k, v in zip (lst_names, lst_marks)}
print(d)
# ---------------------------------------------------------------------
lst_a = [x ** 2 for x in range(10) if x % 2 == 0]
print(lst_a)
# ---------------------------------------------------------------------
d = {k: v for k, v in zip(lst_names, lst_marks)if len(k) == 4}
print(d)