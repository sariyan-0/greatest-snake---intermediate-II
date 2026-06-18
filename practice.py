############################# PRACTICE #############################
# Q1: perimeter of rectangle
# a = 10
# b = 20
# #
# c = a + b
# d = c * 2
# print (d)
# --------------------------------
# Q2: perimeter of circle
# r = 5
# PI = 3.14
# #
# f = 2 * PI * r
# print(f)
# --------------------------------
# Q3: More geometry (Done)
# Square
# a = 5
# p = a * 4
# print (p)
#-----------------
# Triangle
# b = 2
# h = 5

# a = 0.5 * 2 * 5
# print (a) 
# b = 2
# h = 5

# a = 0.5 * 2 * 5
#-----------------
# Sphere Surface Area
# PI = 3.14
# r = 5

# a = 4 * PI * r**2
# print (a)
#-----------------
# Speed
# d = 10
# t = 2

# s = d / t
# print ("Speed:", s ,"M/S") # We use commas to seperate different values in a print statement
# --------------------------------
# Q4: Add limits (Done)
# a = -1
# if a > 100:
#     print("Invalid Score, the mark is more than 100%!")

# elif a > 80:
#     print("HELLL YAHHH")    # Indentation
#     print("Good Job")
#     print("You are amazing!")
# elif a > 70:
#     print("Woow")

# elif a > 50:
#     print("Try harder next time")

# elif a > -1:
#       print("You have to study all summer")
# elif a > 100:
#     print("Invalid Score, the mark is more than")
# else:
#   print("Invalid Score, you entered a negative mark!")
# --------------------------------
# Q5: Detect odd or even numbers (Done)

# Rule:
# If dividing a number by 2 and multiplying back by 2 gives
# the same number -> it is Even
# Otherwise -> it is Odd
# -------------------------------------------------------
# a = 67
# if (a // 2) * 2 == a:   # This is gonna remove the decimal number so that the answer is accurate. Thats why we use "//"  instead of "/" 
#     print(a, "is even")
# else:
#     print(a, "is odd")
#
# ----- OR -----
# x = 67
# if x % 2 == 0:
#     print("Even Number")

# else:
#     print("Odd Number")
# -------------------------------------------------------
# Q6: Which one is bigger?
# a = 50
# b = 50
# c = 50
# if a > b and a > c:
#     print(a, "is bigger")

# elif b > a and b > c:
#     print(b,"is bigger")

# elif c > a and c > b:
#     print(c,"is bigger")
    
# else:
#     print("they are all the same:", a)
# -------------------------------------------------------
# Q7: apply a 20% discount to the prices
# price = [20, 40, 30, 100]
# for discount in price:
#     final_price = discount - (discount * 0.2) # Applies the discount
#     print(final_price)
# -------------------------------------------------------
# Q8: Find the odd numbers in the list
# list = [13, 12, 5, 1]
# for odd in list:
#     if ( odd // 2) * 2 == odd:   # This is gonna remove the decimal number so that the answer is accurate. Thats why we use "//"  instead of "/" 
#         print(odd, "even")
#     else:
#         print(odd,"odd")
# Q9: Find the odd numbers in the list
# -------------------------------------------------------
# Q10: Find the divisors of the number 12 (Not Done)
# x = 12
# if x % 1 == 0:
#     print(1)

# if x % 2 == 0:
#     print(2)

# if x % 3 == 0:
#     print(3)

# if x % 4 == 0:
#     print(4)

# if x % 5 == 0:
#     print(5)

# if x % 6 == 0:
#     print(6)

# if x % 7 == 0:
#     print(7)

# if x % 8 == 0:
#     print(8)

# if x % 9 == 0:
#     print(9)

# if x % 10 == 0:
#     print(10)

# if x % 11 == 0:
#     print(11)

# if x % 12 == 0:
#     print(12)
# --------------------------- Same thing, but with loop
# x = 12
# for item in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
#     if x % item == 0:
#         print(item)
# -------------------------------------------------------
# Q11: Find the smallest number in the list
# lst = [12, 18, 3, 65, 25, 7, 15, 90]
# smallest = lst[0]
# for item in lst: # Tries each number in the list
    
#     # If the current number is smaller than the current smallest
#     if item < smallest:  # Update 'smallest' to this new minimum value
#         smallest = item  # Print the new smallest value found
# print(smallest)

# print(smallest)
# -------------------------------------------------------
# Q12: add a 20% discount for the prices above 10000 tomans
# lst = [10000, 50000, 8000, 90000, 2000, 65000, 40000]

# for price in lst:
#     if price > 10000:
#         final_price = price - (price * 0.2)  # Applies 20% discount if above 10000 toman
#         print(final_price)
#     else:
#         print(price, "(not discounted!)")  # No discount applied
# -------------------------------------------------------
# Q13: Using Range
# x = 1200
# for item in range(1,x+1): # By using +1 you also include the number itself
#     if x % item == 0:
#         print(item)
# -------------------------------------------------------
# Q14: Find the two digit divisors of x
# x = 1200
# for item in range(1,x+1): # By using +1 you also include the number itself
#     if x % item == 0:
#         if 9 < item <100: # Limits to only two digit numbers
#             print(item)
#
# We can also put the limit on range
# x = 1200
# for item in range(10, 100): # Limits to only two digit numbers
#     if x % item == 0:
#         print(item)
# -------------------------------------------------------
# Q15: Print the maximum in the list
# lst = [12, 18, 3, 65, 25, 7, 15, 90]
# largest = lst[0]
# for item in lst:
#     if item > largest: 
#         largest = item # Moves to the next number to compare with
# print(largest)  # Prints 90
# -------------------------------------------------------
# Q16: print the biggest odd number in the list
# lst = [12, 18, 3, 65, 25, 7, 15, 90]
# largest = lst[0]
# for item in lst:
#     if item > largest and item % 2 == 1:
#         largest = item # Moves to the next number to compare with
# print(largest)  # Prints the biggest odd
# -------------------------------------------------------
# Q17: Find the average of the smallest and and biggest numbers in the list
# lst = [12, 18, 7, 65, 35, 3, 15, 90]
# largest = lst[0]
# for item in lst:
#     if item > largest:
#         largest = item
# smallest = lst[0]
# for item2 in lst:
#     if item2 < smallest:
#         smallest = item2

# average = (largest + smallest)/2
# print (average)

# -------------------------------------------------------
# Q17: Find the sum of all the items in the list
# lst = [12, 18, 7, 65, 35, 3, 15, 90]
# g = 0
# for item in lst:
#     g = g + item
# print (g)
# OR
# a = sum(lst)
# print (a)
# -------------------------------------------------------
# Q18: Find the average of all the numbers in the list
# lst = [12, 18, 7, 65, 35, 3, 15, 90]
# g = 0
# for item in lst:
#     g = g + item

# n = len(lst)
# average = g / n
# print(average)

# -------------------------------------------------------
# Q19: Find the divisors of x
# x = 6
# c = 0
# for item in range (1, x+1):
#     if x % item == 0:
#         c = c + 1
# if c == 2:
#     print("This is a prime number")
# else:
#     print("This is not a prime number")
# -------------------------------------------------------
# Q20: Find out if x is a perfect number
#  x = 6
# total = 0
# for item in range (1, x):
#     if x % item == 0:
#         total = total + item
# if total == x:
#     print("This is a perfect number")
# else:
#     print("This is not a perfect number")
# -------------------------------------------------------
# Q21: Organize the following list
# lst = [12, 18, 7, 65, 35, 3, 15, 90]
# lst2 = []
# t = len(lst)

# for i in range (t):
#     mini = lst[0]
#     for item in lst:
#         if item < mini:
#             mini = item
#     lst2.append (mini) # Adds mini to lst2
#     lst.remove (mini) # Removes mini from lst

# print (lst2)
# -------------------------------------------------------
# Q22: Find all the prime numbers under 1000
# Ex: 2, 3, 5, 7, 11, 13, ...., 997
# prime_lst = []
# for x in range(1, 1000):
#     c = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             c = c + 1
#     if c == 2:
#         prime_lst.append(x)
# print(prime_lst)
# -------------------------------------------------------
# Q23: Sort the list from largest to smallest
# lst = [12, 18, 7, 65, 35, 3, 15, 90]
# lst2 = []
# t = len(lst)

# for i in range(t):
#     maxi = lst[0]
#     for item in lst:
#         if item < maxi:
#             maxi = item
#     lst2.append(maxi)   # Adds the largest value
#     lst.remove(maxi)    # Removes it from the original list

# print(lst2)
# -------------------------------------------------------
# Q24: Find the common numbers in both lists
# lst_1 = [12, 18, 7, 65, 35, 3, 15, 90]
# lst_2 = [90, 13, 12, 15, 16, 8, 2, 11]
# # Ex: 12, 15, 90

# common = []
# for item in lst_1:
#     if item in lst_2:
#         common.append(item)
# print(common)
# -------------------------------------------------------
# Q25: Find the smallest number in the first half from the list
# lst = [12, 18, 7, 65, 35, 3, 15, 90]

# half = len(lst) // 2
# lst_1 = []

# for i in range(half):
#     num = lst[i]
#     lst_1.append(num)

# mini = lst_1[0]
# for item in lst_1:
#     if item < mini:
#         mini = item

# print(mini)
# -------------------------------------------------------
# Q26: Find the average in the second half from the lst
# lst = [12, 18, 7, 65, 35, 5, 15, 90]

# lst_2 = []
# t = len(lst)
# half = len(lst) // 2
# for i in range(half, t):
#     num = lst[i]
#     lst_2.append(num)

# t_2= len(lst_2)
# total = 0
# for item in lst_2:
#     total = total + item

# average = total / t_2
# print(average)
# ---------------------------
# t = len(lst)
# total = 0
# c = 0
# t = len(lst)
# half = t // 2

# for i in range (half, t):
#     num = lst[i]
#     total = total + num
#     c = c + 1
    
# average = total / c
# print(average)
# -------------------------------------------------------
# Q27: Find all 3 digit prime numbers

# prime_lst = []
# for x in range(100, 1000):
#     c = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             c = c + 1
#     if c == 2:
#         prime_lst.append(x)

# t = len(prime_lst)
# total = 0
# for item in prime_lst:
#     total = total + item

# average = total / t
# print(average)
# -------------------------------------------------------
# Q28: Orgenize the 1st half of the list and add it with the 2nd list
# lst = [12, 18, 7, 65, 35, 5, 15, 90]
# lst2 = []
# lst1 = []
# t = len(lst)
# half = t //2
# for i in range(half):
#     num = lst[i]
#     lst1.append(num)

# for i in range (half,t):
#     num = lst[i]
#     lst2.append(num)

# lst_sorted = []
# t = len (lst1)
# for i in range(t):
#     mini = lst1[0]
#     for item in lst1:
#         if item < mini:
#             mini = item
#     lst_sorted.append(mini)
#     lst1.remove(mini)

# result = lst_sorted + lst2

# print(result)
# -------------------------------------------------------
# Q29: Find all the perfect numbers under 10000

# for x in range(1, 10000):
#     total = 0

#     for item in range (1, x):
#         if x % item == 0:
#             total = total + item
#     if total == x:
#         print(x)
# -------------------------------------------------------
# Q30: Find the smallest common number
# lst = [12, 18, 7, 65, 35, 5, 15, 90]
# lst_2 = [90, 13, 12, 15, 16, 8, 2, 11]

# mini = []
# maxi = []
# smallest = lst[0]
# for item in lst: # Tries each number in the list
#     if item in lst_2:
#         smallest = item
# for item in lst:
#         if item in lst_2 and item < smallest:
#              smallest = item

# print (smallest)
# ----------------------------
# lst_common = []
# for num in lst:
#     for item in lst_2:
#         if num == item:
#             lst_common.append(num)
# mini = lst_common[0]
# for item in lst_common:
#     if item < mini:
#         mini = item
# print(mini)
# -------------------------------------------------------
# Q31: Find if x is in the list or not?
# lst = [12, 18, 7, 65, 35, 5, 15, 90]
# Yes/No
# x = 13
# if x in (lst):
#     print("Yes")
# else:
#     print("No")
# ----------------------------
# label = "No"
# for item in lst:
#     if x == item:
#         label = "Yes"

# if label == "Yes":
#     print ("Yes, we found the number!")

# else:
#     print("No, we didnt find the number!")
# # -------------------------------------------------------
# Q32: Find the repeated numbers in the list
lst = [12, 18, 7, 65, 35, 12, 15, 90, 7, 65, 4]
# repeated = []

# for item in (lst):
#     if lst.count(item) > 1 and item not in repeated:
#         repeated.append(item)

# print(repeated)
# ----------------------------
# repeated = []
# for num in lst:
#     c = 0
#     for item in lst:
#         if num == item:
#             c = c + 1
#     if c > 1:
#         if num not in repeated:
#             repeated.append(num)
# print (repeated)
# ---------------------------
# repeated = []
# for num in lst:
#     c = lst.count(num)
#     if c > 1:
#         if num not in repeated:
#             repeated.append(num)
# print (repeated)
# ------------------------------------------------------
# Q33: Find the number of digits in a number
#
# 8527 >>>> 4
# 85270073 >>>>> 8
# ------------------------------------------------------
# Q34: Find if the following number is a perfect square
# x = 16

# if (x ** 0.5) % 1 == 0:
#     print("Perfect square")
# else:
#     print("Not a perfect square")
# ----------------------------
# number = "No"
# for item in range(1, x):
#     if item * item == x:
#         number = "Yes"

# if number == "Yes":
#     print(x, "is a squre number")
# else:
#     print(x, "is not a square number")
# --------------------------------------------------------
# Q35: Find the non repeated numbers
# lst = [12, 18, 7, 65, 35, 12, 15, 90, 7, 65, 4]

# non_repeated = []
# for num in lst:
#     if lst.count(num) == 1:
#         non_repeated.append(num)
# print (non_repeated)
# --------------------------------------------------------
# Q36: Find if x is a prime number using label
# x = 12
# label = "Yes"

# for item in range(2, x):
#     if x % item == 0:
#         label = "No"


# if label == "Yes":
#     print("This is a prime number")
# else:
#     print("This is not a prime number")
# --------------------------------------------------------
# Q37: Create a fibonacci number till 20 units
# lst = [1, 1]
# a = 1
# b = 1
# for i in range(20):
#     f = a + b
#     lst.append(f)
#     a = b
#     b = f
# print(lst)
# ----------------------------
# lst = [1, 1]
# f = lst[0] + lst[1]
# lst.append(f)
# #
# f = lst[1] + lst[2]
# lst.append(f)
# #
# f = lst[2] + lst[3]
# lst.append(f)
# print(lst)
# ----------------------------
# lst = [1, 1]
# for i in range (20):
#     f = lst[i] + lst [i + 1]
#     lst.append(f)
# print(lst)
# --------------------------------------------------------
# Q38: Orgenize the following list using bubble sort
lst = [12, 18, 7, 65, 35, 12, 15, 90, 7, 65, 4]

n = len(lst)

for i in range(n - 1):
    # The '- i' part makes sure I don't recheck already sorted elements at the end
    for j in range(n - 1 - i):
        # If the current element is greater than the next one, swap them
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]


print("Sorted list:", lst)
# --------------------------------------------------------
# Q39: Find the average of of 30 fibonacci numbers

lst = [1, 1]
a = 1
b = 1

for i in range(28):   # Loop to repeat for the rest
    f = a + b
    lst.append(f)
    a = b
    b = f

total = 0
for item in lst:
    total = total + item

average = total / 30
print(average)

# --------------------------------------------------------
# Q40: Remove the repeated numbers
lst = [12, 18, 7, 65, 35, 12, 15, 90, 7, 65, 4]

not_repeated = []
for x in lst:
    if x not in not_repeated:
        not_repeated.append(x)

print(not_repeated)