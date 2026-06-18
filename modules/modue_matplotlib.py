############################# MATPLOTLIB #############################
from matplotlib import pyplot
import numpy as np  

# line graph
# x = np.array ([3, 5, 10, 3, 2 ,1])
# y = np.array ([3, 5, 1, 5, 7, 2 ])

#           markerlinecolor
# pyplot.plot(x, y, 'o--b')
# pyplot.xlabel("year")
# pyplot.ylabel("price")
# pyplot.title("Rice price / M")
# pyplot.grid()
# pyplot.show()
# --------------------------------------------------------------------
# x = np.array( range(-10, 10, +1))

# lst_y = []                      # i = -10
# for i in range (-10, 10, +1):   # while i ≤ 10
#     y = i ** 9                  #   y = i ** 2
#     lst_y.append(y)             #   lst_y.append(y)
#                                 #   i = i + 0.2
# y = np.array(lst_y)

# pyplot.plot(x, y, "-b")
# pyplot.grid()
# pyplot.show()
#######################################################################
#

# x = np.array (["AF", "CA", "US", "CH", "IR" ,"IN"])
# y = np.array ([3, 5, 1, 5, 7, 2 ])


# pyplot.bar(x, y)

# pyplot.show()
#######################################################################
# y = np.array ([120, 80, 20, 80 ])
# my_labels = ["RENT", "FOOD", "TRANSPORT", "BILLS"]
# my_colors = ["red", "green", "blue", "black"]
# my_exp = [0.1, 0.2, 0.1, 0.2]


# pyplot.pie(y, colors = my_colors, labels = my_labels, explode = my_exp)

# pyplot.show()
#######################################################################
# Scatter plot
x = np.array([1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400])

y = np.array([4, 6, 5, 8, 10, 10, 13, 12, 3, 5, 6 ])

quality = [50, 200, 100, 400, 500, 800, 1000, 900, 100, 50, 1000]

investment = [10, 20, 30, 50, 40, 60, 30, 80, 20, 40, 100]

# pyplot.scatter(x, y, s = quality, c = investment)
# pyplot.colorbar()
# pyplot.show()
#######################################################################
y_ages = [19, 12, 55, 23, 74, 23, 6, 23, 65, 34, 66, 23, 77, 23, 45, 23, 66,  23, 64, 42, 35, 65, 23, 76, 23, 99, 23, 77, 44, 75, 43, 75]
pyplot.hist(y_ages)
pyplot.show()