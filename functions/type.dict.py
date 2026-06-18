# #################################### Tuple ####################################
# ####################################
# #
# tup_1 = (10, 25, 30, 12)
# # print(tu_1)
# t = len(tup_1)
# # print(t)
# first_element = tup_1[0]
# # print(first_element)
# # ----------------------------------
# #
# # for item in tup_1:
# #     print(item + 1000)
# # ----------------------------------
# c = tup_1.count(25)             # 2
# print(c)
# #
# ind = tup_1.index(25)           # 3
# print(ind)
#################################### Dictionary ####################################
#
#   They store data like a real dictionary
#
#   KEY: VALUE
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
#
#
#
d_2 = {"John": "US", "Ali": "UAE", "Mark": "UK", "Kim": "JP"}

d_3 = {"Rock": [14, 23, 18], "Vick" : [19, 11, 76]}
# print(d_3)
# --------------------------------------------------------------------
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}

t = len(d_1)
# print(t)
# first = d_1[0]        # ERROR: NO INDEX IN DICTIONARY
# print(first)
#
first = d_1["Joe"]      # ONLY access values by keys
# print(first)
#
# first = d_1[18]       # ERROR!
# print(first)
# --------------------------------------------------------------------
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
#
# a = dl_1.get("John")
# print(a)
#       return <None> if the key is NOT found
# --------------------------------------------------------------------
# a = d_1.pop("Sara")
# print(a)
# print(d_1)
# ----------------------------------
d_1.update({"Joe": 17})
# print(d_1)
# ----------------------------------
k = d_1.keys()
# print(k)
v = d_1.values()
# print(v)
# ----------------------------------
a = d_1.items()
# print(a)
# ----------------------------------
# loop on dictionary
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
# 1:
# for k in d_1.keys():
#     if d_1.get(k):
#         print(k)
# ----------------------------------
# 2:
# total = 0
# for v in d_1.values:
#     total += v
# average = total / len(d_1)
# print(average)
# ----------------------------------
# 3: (Best Prcatice)
# for k, v in d_1.items():
#     if v > 17:
#         print(k)
########################################################################
# Q1: Find the lowest mark
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
#
# 10
# mini = 21
# for v in d_1.values():
#     if v < mini:
#         mini = v
# print (mini)
########################################################################
# Q2: Find the best student
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
# maxi = 0

# for k, v in d_1.items():
#     if v > maxi:
#         maxi = v
#         name = k

# print(name, maxi)
########################################################################
# Q3: Organize based on the marks
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
result = {}

for i in range(len(d_1)):
    mini = 1000
    for k, v in d_1.items():
        if v < mini:
            mini = v
            name = k

    result[name] = mini
    d_1.pop(name)

print(result)
########################################################################
# Q4: Organize the dictionary based on the name of the students
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
# output: 
#       A > B > C > D
result = {}
t = len(d_1)

for i in range(t):
    mini = "z"
    for k, v in d_1.items():
        if k < mini:
            mini = k
            marks = v
    result.update({mini: marks})
    d_1.pop(mini)

print(result)


########################################################################
# Q5 : Find the common names in the dictionary
d_1 = { "Joe": 14, "Dan": 81, "Sara": 8, "Amir": 17}
d_2 = { "Joe": 54, "Leo": 11, "Sara": 9, "Ellie": 17}
# output:
#      {"joe: ???", "Sara:???"}
common = []

for v in d_1.keys():
    if v in d_2.keys():
        if v not in common:
            common.append(v)

print(common)
########################################################################
# Q6 : Find the common marks in the dictionary
d_1 = { "Joe": 11, "Dan": 81, "Sara": 8, "Amir": 17}
d_2 = { "Joe": 54, "Leo": 11, "Sara": 9, "Ellie": 17}
# output:
#       {????????}
common = []

for v in d_1.values():
    if v in d_2.values():
        if v not in common:
            common.append(v)

print(common)
# ---------------------------------------------
common = {}

for k_1, v_1 in d_1.items():
    for k_2, v_2 in d_1.items():
        if v_1 == v_2:
            common.update({v_1: [k_1, k_2]})
print(common)
# ---------------------------------------------
# Q1: Function of the smallest member of the dictionary
def find_smallest(d):
    mini = 1000
    for v in d.values():
        if v < mini:
            mini = v
    return mini

########################################################################
# Q2: function to organize gictionary
def organize_by_marks(d):
    result = {}
    for i in range(len(d)):
        mini = 1000
        for k, v in d.items():
            if v < mini:
                mini = v
                name = k
        result[name] = mini
        d.pop(name)
    return result

########################################################################
# Q3: Function to organize the member of a dictionary
def organize_by_name(d):
    result = {}
    t = len(d)
    for i in range(t):
        mini = "z"
        for k, v in d.items():
            if k < mini:
                mini = k
                marks = v
        result.update({mini: marks})
        d.pop(mini)
    return result

########################################################################
# Q4: function to find the similar items in two dictionary
def find_common_keys(d_1, d_2):
    common = []
    for v in d_1.keys():
        if v in d_2.keys():
            if v not in common:
                common.append(v)
    return common
