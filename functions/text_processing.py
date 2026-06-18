################################## Text Processing ##################################
# str_1 = "My name is Mr. Robot and im here to save the world"
#
# ---------------------------------------------------------------
# Operators:  + ( Concatenation)   NO: "-", "/", "*", "**", "//"
#              <    <=  ?   >=
#                   ==      !=
#
# str_1 = "powersof"
# str_2 = "zero"

# z = str_1 + str_2
# print(z)
#
# if str_1 < str_2:       # A < B < C < ..... < Z < a < b < c ..... < z
#     print("PPOOWWEERR")
# ---------------------------------------------------------------
#       0123456
# str_1 = "zero"

# t = len(str_1)              # 7
# print(t)


# first = str_1[0]            # Index
# print(first)
# ---------------------------------------------------------------
# str_1 = "zero"
# g = ""
# for char in str_1:
#     if char == "e":
#         g += "*"
#     else:
#         g += char
# print(g)
###################################################################
# Q1: Show the hidden phone number
#
#       09124447755     >>>     0912---7755
#       09128482241     >>>     0912---2241
#       09123456789     >>>     0912---6789
#
phone = "09124447755"
#
# g = ""
# for i in range(len(phone)):
#     if 4 <= i <= 6:     # indices 4,5,6
#         g = g + "-"
#     else:
#         g = g + phone[i] # 

# print(g)
###################################################################
# Q2: Remove the selected words from the following string
str_1 = "M,y na.me is Mr. Robo@t and im h;ere to s-a-v-e the wo`rld"
#                       ^^^^^                ^^^^
# ["My", "name", "is", "Mr.", .....]
#
# str_1 = str_1 + " "
# lst_word = []
# g = ""
# for char in str_1:      # char ~ "M" >> "y" >> " " >> "i" >> "s"
#     if char != " ":     #         OK     OK
#         g += char       #   g ~ "My"
#     else:               #                        OK
#         lst_word.append(g)
#         g = ""
# print(lst_word)
###################################################################
# Q3: Clean the seperated words
# ['My', 'name', 'is', 'Mr.', 'Robot', 'and', 'im', 'here', 'to', 's-a-v-e', 'the', 'world']
# ---------------------------------------------------------------
# for item in lst_word:
#     if item == "save":
#         print("Error: Must be filterd")
# lst_clean = []

# for word in lst_word:
#     g = ""
#     for char in word:
#         if char != "-" and char != "=" and char != "+" and char != "/" and char != "*" and char != "_" and char != "@" and char != "#" and char != "$" and char != "%" and char != "^" and char != "&" and char != "(" and char != ")" and char != "." and char != "?" and char != ">" and char != "<" and char != "," and char != "!" and char != "?" and char != "'" and char != "[" and char != "]" and char != ";" and char != ":" and char != "~" and char != "`" and char != "|": 
#             g += char
#     lst_clean.append(g)

# print(lst_clean)

###################################################################
# Q4: Convert question 2 to function
def clean_words(lst_word):
    lst_clean = []

    for word in lst_word:
        g = ""
        for char in word:
            if char != "-" and char != "=" and char != "+" and char != "/" and char != "*" and char != "_" and char != "@" and char != "#" and char != "$" and char != "%" and char != "^" and char != "&" and char != "(" and char != ")" and char != "." and char != "?" and char != ">" and char != "<" and char != "," and char != "!" and char != "?" and char != "'" and char != "[" and char != "]" and char != ";" and char != ":" and char != "~" and char != "`" and char != "|":
                g += char
        lst_clean.append(g)

    return lst_clean

###################################################################
# Q5: Convert question 3 to function
def corrected_words(lst_word):
    lst_correct = []

    for word in lst_word:
        g = ""
        for char in word:
            if char not in "~!@#$%^&*()_+=-|/}]{[]}:;'.,><":
                g += char
        lst_correct.append(g)

    return lst_correct

# call
# a = corrected_words(["bo!m$b", "Ex@plo.de"])
# print (a)

###################################################################
# Q5: Convert lower-case letters to higher-case and alse the other way around

lst = ["jOe", "miKe", "VivA"]

lst_lower = []




# for name in lst:
#     lst_lower.append(name.lower())
# print (lst_lower)

lst = ["jOe", "miKe", "VivA"]
lst_swap = []

for word in lst:
    g = ""
    for char in word:
        if char == "A": 
            g += "a"
        elif char == "a": 
            g += "A"
        elif char == "B": 
            g += "b"
        elif char == "b": 
            g += "B"
        elif char == "C": 
            g += "c"
        elif char == "c": 
            g += "C"
        elif char == "D": 
            g += "d"
        elif char == "d": 
            g += "D"
        elif char == "E": 
            g += "e"
        elif char == "e": 
            g += "E"
        elif char == "F": 
            g += "f"
        elif char == "f": 
            g += "F"
        elif char == "G": 
            g += "g"
        elif char == "g": 
            g += "G"
        elif char == "H": 
            g += "h"
        elif char == "h": 
            g += "H"
        elif char == "I": 
            g += "i"
        elif char == "i": 
            g += "I"
        elif char == "J": 
            g += "j"
        elif char == "j": 
            g += "J"
        elif char == "K": 
            g += "k"
        elif char == "k": 
            g += "K"
        elif char == "L": 
            g += "l"
        elif char == "l": 
            g += "L"
        elif char == "M": 
            g += "m"
        elif char == "m": 
            g += "M"
        elif char == "N": 
            g += "n"
        elif char == "n": 
            g += "N"
        elif char == "O": 
            g += "o"
        elif char == "o": 
            g += "O"
        elif char == "P": 
            g += "p"
        elif char == "p": 
            g += "P"
        elif char == "Q": 
            g += "q"
        elif char == "q": 
            g += "Q"
        elif char == "R": 
            g += "r"
        elif char == "r": 
            g += "R"
        elif char == "S": 
            g += "s"
        elif char == "s": 
            g += "S"
        elif char == "T": 
            g += "t"
        elif char == "t": 
            g += "T"
        elif char == "U": 
            g += "u"
        elif char == "u": 
            g += "U"
        elif char == "V": 
            g += "v"
        elif char == "v": 
            g += "V"
        elif char == "W": 
            g += "w"
        elif char == "w": 
            g += "W"
        elif char == "X": 
            g += "x"
        elif char == "x": 
            g += "X"
        elif char == "Y": 
            g += "y"
        elif char == "y": 
            g += "Y"
        elif char == "Z": 
            g += "z"
        elif char == "z": 
            g += "Z"
        else:
            g += char
    lst_swap.append(g)

print(lst_swap)
