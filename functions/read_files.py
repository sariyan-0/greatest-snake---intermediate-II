from functions.my_functions import *
############################## READ FILES ##############################
#
#       .pdf        .vlsx       .mp3        ,mp4        .json
#
# ----------------------------------------------------------------------
# .txt      (notepad)
# f = open("data_1.txt")
# print(f)

# str_1 = f.read()                # string
# print(str_1)
# f.close()
# str_1 ~ 18\n 12\n 11\n.....
# ----------------------------------------------------------------------
# f = open("data_1.txt")
# print(f)

# str_1 = f.readlines()             # list
# print(str_1)
# f.close()
# lst ~[18\n, 12\n, 91\n, ....]
# ----------------------------------------------------------------------
f = open("data_1.txt")
for i in range(19):
    line = f.readline()
    print(line)

f.close()
# line ~ '18/n'
########################################################################

# f = open("data_1.txt")
# print(f)

# lst = f.readlines()             # list
# f.close()
# list_c = corrected_words(lst)
# print(list_c)

# lst_int = []
# for item in list_c:
#     num = int(item)
#     lst_int.append(num)
# print(lst_int)

# av  = average(lst_int)
# print(av)
# ----------------------------------------------------------------------
# approach : readline()
# total = 0
# f = open("data_1.txt")
# for i in range(10):
#     line = f.readline()
#     num = line[0] + line [1]
#     total += int(num)

# f.close()
# avg = total / 10
# print(avg)
########################################################################

# Approach : read()
# f = open("data_1.txt")
# str_1 = f.read()
# f.close()
# lst_s = splitting(str_1)
# lst_int = []
# for item in lst_s:
#     num = int(item)
#     lst_int.append(num)
# avg = average(lst_int)
# print(avg)
########################################################################
# Q2: find the average of file "data_2" 
# f = open("data_2.txt")        ********************
# lst_marks = []
# for i in range(10):
#     line = f.readline()
#     lst_s = splitting(line, " ")
#     mark  = lst_s[1]
#     print(lst_s)

#     lst_marks.append(mark)
# f.close()

# lst_c = corrected_words(lst_marks)
# lst_int = []
# for item in lst_c:
#     num = int(item)
#     lst_int.append(num)

# avg = average(lst_int)
# print(avg)
########################################################################
# Q1: Find he best student in the data_1 file
########################################################################
# Q2:Check the quality of the password
password = "VerySecret"