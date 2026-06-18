############################### Module OS ###############################

# Always use / (forward slash) instead of \
# path_1 = "/Users/ari/Movies/TV" # (Mac Only)
#
# print(path_1)
#
# use r-string
# path_2 = r"\Users\ari\Movies/TV"
#       raw
# print(path_2)
#
# use double bacl-slash
# path_3 = "\\Users\\ari\\Movies\\TV"
#
# print(path_3)
# -----------------------------------------------------------------------
# \ is an operator
# a = "I'm a programmer." # Works with double quotation
# b = 'I\'m a programmer' # Works with single
# print(a, b)
# do not    >>>     don't
# \n    \t      \U
# print("\U0001F600")
##########################################################################
import os


#         get current working directory
home = os.getcwd()
# print(home)         # home / cwd / main / root
#
# lst = os.listdir()    # prints as a list by default
# print(lst)
#
# lst = os.listdir("/Users/ari/Movies/TV")
# print(lst)
#
# lst = os.listdir("/Users")
# print(lst)
# ------------------------------------------------------------------------
# change directory  
# os.chdir("/Users/ari/Movies/TV")
# f = open("data_1000.txt", "w")
# f.write("Hi there >:) ")
# f.close()
#
# os.chdir(home)
# ------------------------------------------------------------------------
#   
#   make directory
# os.mkdir("Lol")
# os.chdir("/Users/ari/Movies/TV/lol")
# f = open("secrets.txt", "w")
# f.write("I'm a programmer")
# f.close
#
# os.chdir(home)
############# or
# os.mkdir("/Users/ari/Movies/TV/lol")
# f = open("/Users/ari/Movies/TV/lol/secrets.txt", "w")
# f.write("I'm a programmer")
# f.close
# ------------------------------------------------------------------------
# os.chdir("/Users/ari/Movies/TV/")
# os.remove("data_1000.txt")      # deletes a file !!!
#
# or
# os.remove("/Users/ari/Movies/TV/data_1000.txt")

# ------------------------------------------------------------------------
# os.chdir("/Users/ari/Movies/TV/")
# remove a directory
# os.rmdir("lol") # directory not empty
#
##########################################################################
# Q1: Delete the lol directory
# os.chdir("/Users/ari/Movies/TV/")

# for file in os.listdir("lol"):
    # os.remove("lol/" + file)
    # os.remove(f"lol/{file}")        # f-string (format string)

# os.rmdir("lol")
# os.chdir(home)
##########################################################################
# Q2: create a folder in Desktop >>> project_data and create 26 folders named a, b, c, d.... z inside the project data.

# go to Desktop
os.chdir('/Users/ari/Desktop')
#
os.mkdir('project_data')
#
os.chdir('project_data')
for char in 'abcdefghijklmnopqrstuvwxyz':
    os.mkdir(char)
os.chdir(home)
##########################################################################
# Q3: create a folder in Desktop >>> project_data and create 26 folders named a, b, c, d.... z inside the project data, but create 20 folders in each and name them like 1, 2, 3....20. within each of them create 6 extra .txt files with an additional random number in each