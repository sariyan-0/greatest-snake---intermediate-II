######################################### Regular Expressions #########################################
#########################################        RegEx        #########################################
import re
# from functions.my_functions import *



def splitting(str_x, sp_char):
    str_x += sp_char
    lst_word = [] 
    g = ''
    for char in str_x:
        if char != sp_char:
            g += char
        else:
            lst_word.append(g)
            g = ''
    return lst_word



def cleaning(lst_word_x):
    lst_clean = []
    for word in lst_word_x:
        g = ""
        for char in word:
            if char not in "~!@#$%^&*()_+=-|/}]{[]}:;'.,><":
                g += char
        lst_clean.append(g)

    return lst_clean

def custom_cleaning(lst_word_x, char_to_be_cleaned):
    lst_clean = []
    for word in lst_word_x:
        g = ""
        for char in word:
            if char != char_to_be_cleaned:
                g += char
        lst_clean.append(g)
    return lst_clean

def str_num_to_int_num(lst_x):
    lst_int = []
    for item in lst_x:
        num = int(item)
        lst_int.append(num)
    return lst_int

def sum_lst(lst_x):
    g = 0
    for item in lst_x:
        g = g + item
    return g

# -------------------------------------------------------

# f = open("wikipedia.txt")
# str_data = f.read()
# f.close
#
#       re.method(PATTERN. String)
#
# search: findes the first matching in the str_data
# result = re.search(r"\d{4}", str_data) # \d means digit and {4} means length
# print(result)
#   
# -------------------------------------------------------
# match: findes all the matching values IN THE FIRST STRING
# result = re.match(r"\d{4}", str_data)
# print(result)
#
# -------------------------------------------------------
# fullmatch: the value MUST match the entire str_data
# result = re.fullmatch(r"\d{4}", str_data)
# print(result)
#
# -------------------------------------------------------
# findall: findes all of the matching values(unrestricted)
# result = re.findall(r"\d{4}", str_data)
# print(result)
#
# -------------------------------------------------------
# findall: replaces 
# result = re.sub(r"\d{4}", "----", str_data)
# print(result)
#
# result = re.sub(r"\d{4}", "----", str_data, count = 2)
# print(result)
#
# subn: adds the number of the values in modified
# result = re.subn(r"\d{4}", "----", str_data)
# print(result)
#
# -------------------------------------------------------
# result = re.split()
#
#########################################################
# PATTERNS
# result = re.findall(r"\d{4}", str_data)
# print(result)

# ----------------- Quantity
# {4}    >>>        exactly 4 characters
# {4, 6} >>>        4, 5 and 6
# {4,}   >>>        ≥ 4( 4 or bigger)
# {,6}   >>>        ≤ 6 (6 or les)
#
#
#
# --------------------------- Sequence (different words or patterns)
# \d        >>>         a digit             >>>         0-9
# \D        >>>         a non digit         >>>         a-z or !@#$%^&*()_+-= etc..
#
#
# \w        >>>         an alphanumeric     >>>         a-z A-Z 0-9
# \W        >>>         a non alphanumeric  >>>         !@#$%^&*()_+-=  space   \n
#
#
# \s        >>>         a white space       >>>         space   \n
# \S        >>>         a non white space   >>>         a-z A-Z 0-9 !@#$%^&*()_+-=  
#
# .         >>>         any character       >>>         (except \n)
#########################################################
# Q1: Find all the 8 letter words
# result = re.findall(r"\s\w{8}\s", str_data)
# print(result)
#
#########################################################
# Q2: Find the collocation
#
# ex: high-level
#
# result = re.findall(r"\w{1,}-\w{1,}", str_data)
# print(result)
#
# result = re.findall(r"Python", str_data)
# print(result)
#
#########################################################
# Q4: Proper email format
#
# example@domain.com
#
# email = input("Please enter your email: ")
# result = re.fullmatch(r"\w{1,}@\w{1,15}.com", email)
# if result == None:
#     print("Invalied Email")
# else:
#     print("Email Accepted")
#########################################################
# Q5: Total of all gold medals in Olympics
#
# f = open("sport.csv", encoding="utf-8")
# sport_data = f.read
# f.close
# result = re.findall(r"gold", sport_data)
# print(len(result))
#
# Golds: 10486
# Silver: 103
# Bronze: 10369
#########################################################
# Q6: Find all the medals from France/Italy
#########################################################
# Q7: Find all the gold medals earned by a single gender
#########################################################
# Q8: Iranian national code format checker
#########################################################
# Q9: Iranian phone number format checker. Ex: Landline, mobile....
#########################################################
# Q10: Password strength checker
#
#
#
#
#
#
#
#   
# -------------------------------------------------------
# find the detes mentioned in the file 
# f = open("wikipedia.txt")
# str_data = f.read()
# f.close
# lst_w = splitting (str_data, " ")

# lst_c = cleaning(lst_w)
# result = []
# for item in lst_c:
#     if len(item) == 4:
#         result.append(item)
# print(result)
#########################################################
# Q10: Find ip of the computers with core i7 CPU
    # f = open("ip_data.txt")
    # str_data = f.read()
    # f.close

# result = re.findall(r"corei7 \w{2,} \S{7,15}", str_data )
# for item in result :
#     ip = re.sub(r"corei7 \w{2,}", "", item)
#     print(ip)
#########################################################
# Q11: Find ip of the computers with core 16gb RAM
# result = re.findall(r"16G \S{7,15}", str_data )
# for item in result :
#     ram = re.sub(r"16G ", "", item)
#     print(ram)
#########################################################
# Q12: Find ip of the computers with core 16gb RAM
# result = re.findall(r"\d{1,2}G", str_data)
# print(result)
# #
# clean = custom_cleaning(result, "G")
# print(clean)
# #
# str_rams = str_num_to_int_num(clean)
# total = sum_lst(str_rams)
# print(total)
# #
# print(f"The total ram is {total} GB")
# -------------------------------------------------------
# result = re.findall(r"\d{1,2}G", str_data)
# total_ram = 0
# for item in result:
#     ram = re.sub(r"G", "", item)        # "16"
#     total += int(ram)

# print(total)
# #
# print(f"The total ram is {total} GB")
#########################################################
# Q13: find all medals in each country in each year
#
# Output:
#
# USA   1896    6
# USA   1900    12
# ...
# USA   2012    450
# IRI   1896    0
# IRI   1900    0
# ...
# IRI   2012    8
# FRA   1896    0
# FRA   1900    2
# ...
# FRA   2012    110