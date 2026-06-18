############################# FOR LOOP #############################
# Loops are made to repeat a specific action or command
#
# 
# for list in [5, 2, 5, 3]: # "100" X wrong!          
#     z = list + 100 # Each are embedded one by one 
#     print(z)

# A better and cleaner way
# list = [5, 2, 5, 3]
# for number in list: # "100" X wrong!          
#     z = number + 100 # Each are embedded one by one 
#     print(z)

# Using Range
# x = 1200
# for item in range(1,x+1): # By using +1 you also include the number itself
#     if x % item == 0:
#         print(item)
#
# for item in range(100+1): # Zero to 100
#     print(item)
# 
# for item in range(5, 10): # From 5 to 10
#     print(item)
# 
# for item in range(5, 100, 3 ): # From 5 to 10 (in a 3+ pattern)
#     print(item)
#
# x = range(10) + 10   # ERROR
#
# if range(10) < 20:   # ERROR
#     print("Yayyyyyy")
#
# x = range(10) + [11, 12, 13]    #ERROR
# print (x)
# ---------------------------------------------