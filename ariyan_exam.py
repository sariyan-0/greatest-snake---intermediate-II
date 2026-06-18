################################### EXAM ###################################

from functions.my_functions import *
# Q1
def check_password(password):

    SQ = False
    num = False
    length = False
    letters = False
    upper = False
    if len(password) >= 6:
        length = True

    for char in password:
        if char in "0123456789":
            num = True
        if char in "!@#$%^&*()?><,./":
            SQ = True
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = True
        if char in "abcdefghijklmnopqrstuvwxyz":
            letters = True

    if SQ and num and length and letters and upper == True:
        return True
    else:
        return False

# password = "Trump@123"
# if check_password(password): # Works when the statement is True in the return
#     print("Nice Password")
# else:
#     print("Bad Password")
#########################################################
# Q2: Write a function that findes the common vlaues between two lists and organizes them from the lowest to the highest
def common_organize (lst_x, lst_y):
    
    lst_common = []
    lst_answer = []
    for item in lst_x:
        if item in lst_y:
            lst_common.append(item)
    t = len(lst_common)
    for i in range (t):
        mini = lst_common[0]
        for item in lst_common:
            if item < mini:
                mini = item
        lst_answer.append (mini) # Adds mini to lst2
        lst_common.remove (mini) # Removes mini from lst

    return lst_answer


# lst_1 = [13, 18, 5, 90, 60, 0, 10, 30]
# lst_2 = [10, 40, 3, 80, 22, 5, 90, 60]

# answer = common_organize(lst_1, lst_2)
# print(answer)
#########################################################
# Q3: find the fibonacci numbers under 1000

def fibo (num_x):
    lst = [1, 1]
    x = 1
    y = 1
    for i in range(num_x):
        z = x + y
        if z < num_x:
            lst.append(z)
            x = y
            y = z
    return lst
# answer = average(fibo(1000))
# print(answer)
#########################################################
# Q4: Using while true, find the 10th natural number whos numerators sum to a prime number


# x = 1
# count = 0

# while True:
#    lst_d = divisor(x)
#    sum_d = sum_lst(lst_d)
#    if is_prime(sum_d) == True:
#        count += 1
#    if count == 10:
#        print(x)
#        break
#     x =+ 1

#########################################################
# Q5: Find which item has the least quantity


# f = open("kala.txt")

# min_quantity = None
# min_name = ""

# for i in range(10):
#     line = f.readline()
#     lst_s = splitting(line)
#     lst_s = corrected_words(lst_s)

#     if len(lst_s) > 1:
#         name = lst_s[0]            
#         quantity = int(lst_s[1])   

#         if min_quantity is None:
#             min_quantity = quantity
#             min_name = name
#         else:
#             if quantity < min_quantity:
#                 min_quantity = quantity
#                 min_name = name

# f.close()

# print(min_name, "with the quantity of", min_quantity, "has the lowest")
#########################################################
# Q6: Show the entire value of all the items in the storage
# f = open("kala.txt")
# total = 0
# for i in range(6):
#     line = f.readline()
#     lst_s = splitting(line, " ")
#     kala = lst_s[0]
#     count = lst_s[1]
#     price = lst_s [2]
#     total += (int(count)) * (int(price))

# f.close()
# print(total)
# print(kala)
##################################################################
# Q7: Find the 100th fibonacci number with while loop

lst = [1, 1]
x = 1
y = 1
i = 1
while i < 100:
        x, y = y, x + y
        i += 1
print(y)