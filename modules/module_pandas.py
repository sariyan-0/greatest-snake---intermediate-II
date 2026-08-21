############################# pandas ##############################
#
# python -m pip install pandas
#
# -----------------------------------------------------------------
import pandas as pd

student_df = pd.read_csv("student.csv")
# print(student_df)
# print(type(student_df))
# -----------------------------------------------------------------
# Access Columns
# 1:
# ages = student_df.age
# print(ages)
# print(type(ages))           # Series
# # 2:
# marks = student_df["score"]
# print(marks)
# print(type(marks))          # Series
# -----------------------------------------------------------------
# Access Rows
#                    index location
# row_0 = student_df.iloc[0]
# print(row_0)                # Series
#
# a = student_df.iloc[1:3] # row 1-3 (excluded)
# print(a)
#
# a = student_df.iloc[:3] # row 0-3 (excluded)
# print(a)
#
# a = student_df.iloc[3:] # row 3-the end
# print(a)
#
# a = student_df.iloc[:] # row 0-the end
# print(a)
###################################################################
# Access Rows and columns
#                 row, column
# a = student_df.iloc[0, 2]
# print(a)
#
# a = student_df.iloc[0, 2:]
# print(a)
#
# a = student_df.iloc[1:3, 2:]
# print(a)
#
# a = student_df.iloc[1:3, 2:]
# print(a)
#
# a = student_df.iloc[3:, :]
# print(a)
###################################################################
# Loop on series
# all_marks = student_df.score
# total = 0
# for item in all_marks:
#     total += item

# average = total / len(all_marks)
# print(average)
###################################################################
# Q1:
sport_df = pd.read_csv("sport.csv")
# print(sport_df)
# sport_df.info()

# a = sport_df.iloc[100]
# print(a)
# -----------------------------------------------------------------
# Q2: Find the # of gold medals
# c = 0
# for item in sport_df.Medal:
#     if item == "Gold":
#         c += 1
# print(c)
# -----------------------------------------------------------------
# Q3: Find the # of gold medals won by male athletes
# c = 0
# for i in range(31165):
#     if sport_df.iloc[i, 8] == "Gold":
#         if sport_df.iloc[i, 6] == "Men":
#             c += 1

# print(c)
# -----------------------------------------------------------------
# Q3: Find the medal-winning trends of different countries throughout the Olympic Games

#     1896   1900    1904    1908    ...     2012
# USA  ?       ?       ?       ?               ?
# FRA  ?       ?       ?       ?               ?
# ...
# f = open("olympic_data.txt", "w")
# f.write("Country,Year,Golds")
# lst_countries = []
# for item in sport_df.Country:
#     if item not in lst_countries:
#         lst_countries.append(item)
# #
# lst_countries = []
# for item in sport_df.Country:
#         if item not in lst_countries:
#             lst_countries.append(item)
# #
# lst_years = []
# for item in sport_df.Year:
#     if item not in lst_years:
#         lst_countries.append(item)
# # ----------------------------------
# for country in lst_countries:
#     for year in lst_years:
#         c = 0
#         for i in range(31165):
#             if sport_df.iloc[i, 5] == country:
#                 if sport_df.iloc[i, 0] == year:
#                     if sport_df.iloc[i, 8] == "Gold":
#                         c += 1
#         print(f"Country: {country} >>> Year: {year} >>> Golds {c}")
#         f.write(f"{country},{year},{c}\n")
#     print("_" * 50)

# f.close()

# <class 'pandas.DataFrame'>
# RangeIndex: 31165 entries, 0 to 31164
# Data columns (total 9 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   Year        31165 non-null  int64
#  1   City        31165 non-null  str  
#  2   Sport       31165 non-null  str  
#  3   Discipline  31165 non-null  str  
#  4   Athlete     31165 non-null  str  
#  5   Country     31161 non-null  str  
#  6   Gender      31165 non-null  str  
#  7   Event       31165 non-null  str  
#  8   Medal       31165 non-null  str  
# dtypes: int64(1), str(8)
# memory usage: 2.1 MB
###################################################################
movie_df = pd.read_csv("movies.csv")
movie_df.info()
# -----------------------------------------------------------------
# Q1: Find the best movie in the history of cinama