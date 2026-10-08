################################## numpy ##################################
import numpy as np
from PIL import Image

# 1-D array
# [10 5 -6 12 50 2 80]
#
# a = np.array([10, 5, -6, 12, 50, 2, 80])
# print(a)
# # print(a.shape)      # (7,)
# # print(a[0])         # 10    (1 index to access elements)
# #
# print(a[2:5])       # [-6 12 50]
# #
# print(a[:4])        # [10 5 -6 12]
# #
# print(a[5:])        # [2 80]
# #
# print(a[:])         # [10 5 -6 12 50 2 80]
###########################################################################
# 2-D array
#
# | 2 3 8 |
# | 6 5 2 |     row x col
# | 9 9 9 |       5 x 3
# | 0 6 1 |
# | 5 5 5 |

# a = np.array([
#     [2, 3, 8],
#     [6, 5, 2],
#     [9, 9, 9],
#     [0, 6, 1],
#     [5, 5, 5],
# ])
# print(a)            # row, col
# print(a.shape)      # (5, 3)

# print(a[0])         # [2 3 8]
#       row, col
# print(a[0, 1])      # 3 (2 indexes to access elements)
#
# print(a[1:3, 2])    # [2 9]
#
# print(a[3, :2])     # [0 6]
#
# print(a[3:, :2])    # [[0 6]
                    #  [5 5]]
###########################################################################
# Reshape a 2-D array
a = np.array([
    [2, 3, 8, -1],
    [6, 5, 2, -2],
    [9, 9, 9, -3],
    [0, 6, 1, -4],
    [5, 5, 5, -5],
])                      # 5 x 4

# b = a.reshape(2, 10)
# print(b)  # [[2 3 8 -1 6 5 2 -2 9 9]
            #  [9 -3 0 6 1 -4 5 5 5 -5]]
# c = a.reshape(4, 5)
# print(c)
#
# c = a.reshape(4, 4)
# print(c)
# ------------------------------------------------------------------------
arr = np.zeros((5, 8), dtype='uint8')
print(arr)

arr = np.ones((5, 8), dtype='uint8')
print(arr)

###########################################################################
#
im = Image.open("images/gray_scale.png")
width, height = im.size              # (768, 512)
#                                      width, height
pixels = list(im.getdata())
#
im_arr = np.array(pixels, dtype=np.uint8)

image_array = im_arr.reshape(height, width)

# image_array[:, 375:] = 0
# --------------------------
# new_array = image_array[:, :375]
# --------------------------
# for i in range(0, width, 48):
#     image_array[:, i:i + 16] = 0
# --------------------------
new_arr = np.zeros((height, width), dtype=np.uint8)
#
for i in range(0, height, 16):
    for j in range(0, width, 16):
        slice = image_array[i:i + 16, j:j + 16]
        avg = round(slice.mean())
        new_arr[i:i + 16, j:j + 16] = avg

new_im = Image.fromarray(new_arr)
new_im.show()
