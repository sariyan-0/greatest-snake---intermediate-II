
# def is_even(x):
#     if x % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#####################################################################   
# for item in range (1, 11):
#     if is_even(item) == "Even":
#         print(item, "is even")
#####################################################################
# def square(x):
#     return x * x

# lst = [2, 4, 6]

# for item in lst:
#     print(square(item))
#####################################################################
def maximum(lst_x):
    maxi = lst_x[0]
    for item in lst_x:
        if item > maxi:
            maxi = item
    return maxi

# lst = [12, 45, 7, 30, 99, 18]
# for item in lst:
#     x = (maximum(lst))
# print(x)
#####################################################################
def is_positive(x):
    if x > 0:
        return True
    else:
        return False

# lst = [-3, 5, 0, 12, -1, 8]

# for item in lst:
#     if is_positive(item) == True:
#         print(item)
#####################################################################
def is_prime(x):
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False
    
# lst = [4, 7, 12, 17, 9, 23, 10]


# maxprime = None
# for item in lst:
#     if is_prime(item) == True:
#         if maxprime == None or item > maxprime:
#             maxprime = item
# print (maxprime)
#####################################################################

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
# lst = [5, 12, 7, 20, 9, 4, 15, 8, 21]

# maxi = None
# for item in lst:
#     if is_even(item) == True:
#         if maxi is None or item > maxi:
#             maxi = item
# print(maxi)
#####################################################################

def is_positive(x):
    if x > 0:
        return True
    else:
        return False

# item = 0
# total = 0
# count = 0
# lst = [-5, 10, -3, 7, 0, 20, -1, 8]

# while item < len(lst):
#     if is_positive(lst[item]):
#         total += lst[item]
#         count += 1
#     item += 1   # only once

# average = total / count
# print(average)
#####################################################################


def is_odd(x):
    return x % 2 == 1
# lst = [3, 10, 7, 4, 9, 12, 5]
# lst_2 = []
# total = 0
# for item in lst:
#     if is_odd(item):
#         lst_2.append(item)
# print(sum(lst_2))
#####################################################################
def is_prime(x):
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

# lst1 = [4, 7, 12, 17, 9, 23, 10]
# lst2 = [2, 7, 11, 17, 23, 30]
# lst_common = []
# lst_prime = []
# for item in lst1:
#     if item in lst2:
#         lst_common.append(item)
# print (lst_common)

# for prime in lst_common:
#     if is_prime(prime):
#         lst_prime.append(prime)
#####################################################################
def average(lst_x):
    t = len (lst_x)
    total = 0
    for item in lst_x:
        total = total + item

    avg = total / t
    return avg



# f = open("data_1.txt", "r")

# total = 0
# count = 0

# for line in f:
#     num = int(line)
#     total += num
#     count += 1

# f.close()

# average = total / count
# print(average)
#####################################################################
# lst = [10, 20, 30, 40, 50]
# for item in lst:
#     print(item)
#####################################################################
# x = "EXAM"
# for item in x:
#     print(item)
#####################################################################
# lst = [4, 7, 12, 17, 9, 23, 10]
# lst_p = []
# for item in lst:
#     if is_prime(item) == True:
#         lst_p.append(item)
# print(maximum(lst_p))
#####################################################################
# total = 0
# for item in range(1, 50):
#     if is_prime(item) == True:
#         total += item
# print(total)
#####################################################################
# lst_12 = []
# lst_18 = []
# lst_common = []
# for item in range (1, 13):
#     if 12 % item == 0:
#         lst_12.append(item)

# for item in range(1, 19):
#     if 18 % item == 0:
#         lst_18.append(item)

# for answer in lst_12:
#     if answer in lst_18:
#         lst_common.append(answer)

# GCD = maximum(lst_common)
# print(GCD)

#####################################################################
lst_1 = [4, 7, 12, 17, 9, 23, 10]
lst_2 = [2, 7, 11, 17, 23, 30]
lst_3 = []
lst_prime = []
for item in lst_1:
    if item in lst_2:
        lst_3.append(item)
print(lst_3)

for prime in lst_3:
    if is_prime(prime) == True:
        lst_prime.append(prime)
print(lst_prime)