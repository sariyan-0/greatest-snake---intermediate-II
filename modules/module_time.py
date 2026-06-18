############################### Module Time ###############################

import time

# t = time.time()             # 01/01/1970    Why this date?
# print(t)
#
# ct = time.ctime()
# print(ct)
#
# gt = time.gmtime()            # Greenwich mean times
# print(gt)
# print(gt.tm_year)
# print(gt.tm_hour)
# print(gt.tm_isdst)
#
# gt = time.localtime()            # Your local time
# print(gt)
# print(gt.tm_year)
# print(gt.tm_hour)
# print(gt.tm_isdst)
#
# print("Hello")

# time.sleep(5)                      # 5 seconds delay!

# print("My name is Ari")
################################################################
# Q1: 

t_1 = time.time()
total = 0
for num in range(1, 1):
    total += num
print(total)

t_2 = time.time()
duration = t_2 - t_1
print(f"This process took {duration} secounds")