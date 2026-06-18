########################## Datetime ##########################
from datetime import date, datetime, timedelta


# ------------------------- Date -----------------------------
# d_1 = date.today()
# print(d_1)
#
# text = "My birthday is: ", + str(d_1)
# print(text)
#
#
# str_d_1 = d_1.strftime("%Y/%b/%d")
# text = "My birthday is: " + str_d_1
# print(text)
# ------------------------------------
# custom date: 
#           year, month, day
# d_1 = date(2020, 5, 18)
# d_2 = date(2010, 1, 1)

# date operators:   -   (differences)   NO  +   *   /
#                   <   >   ==  !=
# z = d_1 - d_2
# print(z)
#
# z = d_1 - d_2
# print(z)
#
# if d_1 > d_2:
#     print("Yayyyy")
#####################################################
# ------------------- datetime-----------------------

# dt = datetime.now
# print(dt)
# str_dt = dt.strftime("%Y/%m/%d      %H:%M")
# text = "My date is: " + str_dt
# print(text)
#
# custom date: 
#           year, month, day, hour, minute, second
# d_1 = date(2020,  5,   18,   9,    30,     40)
# d_2 = date(2020,  6,   11,   2,    40,     10)

# z = d_1 - d_2
# print(z)
#

# if d_1 > d_2:
#     print("Yayyyy")

##################################################
# ----------------- timedelta --------------------
# dt = datetime.now()
# next_week = dt + timedelta(days = 7)
# print("next_week")
# #
# last_week = dt - timedelta(days = 7)
# print(last_week)
# #
# a = dt + timedelta(days = 7,
#                    second = 500,
#                    milliseconds = 10,
#                    microseconds = 65,
#                    hours = 10,
#                    minutes = 350,
#                    weeks = 8)

###################################################################
# Calculate your age in seconds
# birth_date = datetime(2008, 5, 20)
# now = datetime.now()

# age = now - birth_date

# age_in_seconds = age.total_seconds()

# print("I am:", int(age_in_seconds),"seconds old")
###################################################################
# birth_date = datetime(2008, 5, 20)

# future_date = birth_date + timedelta(seconds=500_000_000)

# print("You will be 500,000,000 seconds old on:")
# print(future_date)
###################################################################
# show every Thursday in 2026

# f = open("2026_thu.txt", "w")
# first_thu = date(2026, 1, 1)
# for i in range(52):
#     next_thu = first_thu + timedelta(days = 7)
#     f.write(next_thu.strftime("%Y_%m_%d     Tursday"))
#     f.write("\n")
#     first_thu = next_thu
# f.close()

###################################################################
# convert solar date to gregorian


jy = 1404
jm = 10
jd = 28

solar_start = date(1403, 1, 1)
gregorian_start = date(2024, 3, 20) 


days_passed = (jm - 1) * 31 + (jd - 1)
gregorian_date = gregorian_start + timedelta(days=days_passed)

print("Gregorian date is:", gregorian_date)