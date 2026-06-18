######################### Write to Files #########################
from my_functions import *
#
# f = open("prime_numbers.txt", "w") # mode ~ w allows to create a file
# f.write (str(13))
# f.close()
######################################################

# f = open("prime_numbers.txt", "w")
# for num in range (1, 1000):
#     if is_prime(num) == "A prime number":
#         f.write(str(num))
#         f.write("\n")
# f.close()
# ----------------------------------------------------
#
# f = open("prime_numbers.txt", "w")
# lst_primes = all_primes(1, 1000)
# f.write(str(lst_primes))
# f.close()
######################################################
#
# f = open("banana.txt", "w")         
# f.write("I am a BANANA AKA Moz")
# f.close()
# #
# f = open("banana.txt", "w")         # "w" always overwrites the old text
# f.write("I am Moz")
# f.close()
# # ----------------------------------------------------
# f = open("banana.txt", "a")         # "a" stands for append which adds
# f.write("I am a BANANA AKA Moz \n") 
# f.close()
# #
# f = open("banana.txt", "a")         
# f.write("I am Moz \n")
# f.close()
######################################################
f = open("data_3.txt")
str_1 = f.read()
f.close()
lst_s = spliting(str_1, " " )
lst_c = custom_cleaning(lst_s, ",")
lst_f = str_num_to_float_num(lst_c)
avg = average(lst_f)
f = open('data_3.txt', "a")
f.write('\n')
f.write("The average is: ")
f.write(str(avg))
f.close()