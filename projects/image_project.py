################### Image Project #########################
from PIL import Image
from matplotlib import pyplot
from functions.image_functions import *

# w, h, pixels = load_image('images/pumpkin/test_2.webp')
# print(pixels[:10])

# no_bg_pixs = remove_bg(pixels)
# print(no_bg_pixs[:20])

# r_, g_, b_ = rgb_averages(no_bg_pixs)
# print(r_, g_, b_)
#
# family = detect_color_family(r_, g_, b_)
###########################################################
# Assume we have an ORANGE family
#
#                      / Pumpkin
#       orange  ===>
#                      \ Carrot
#
# gray_pixes = rgb2gray(no_bg_pixs)
# print(gray_pixes[:10])
#
# lst_hist = get_hist_data(gray_pixes)
# show_histogram(lst_hist)
# ---------------------------------------------------------
# Analyze Histograms
# family = "ORANGE"
# if family == 'ORANGE':
#     r = calc_ratio(lst_hist, 200)
    # print(r)
#     if r < 0.1:
#         print('Pumpkin')
#     else:
#         print('Carrot')
# elif family == 'RED':
    # Logic ...
#     if 'histogram is sharp':
#         print('Apple')
#     else:
#         if 'over 150 is large':
#             print('Apple')
#         else:
#             print('Strawberry')
###########################################################
#
#                         Type     >>>     for each Type
#
# میوه                    x 10                 x 20 image     سلطانی
#
# صنعتی                   x 10                 x 20 image     صغری
#
# گل                      x 10                 x 20 image     احمدی
#
# ماهی                    x 10                 x 20 image
#
# پرنده                   x 10                 x 20 image     هدایتی
#
# حیوانات وحشی            x 10                 x 20 image
#
# قطعات سخت افزار کامپیوتر (hard)
#
# پرچم کشور ها            x 200                x 1 or 2      اسعدی
#
# -------------------------
# مانیاد رهما
# آریان اسمعیل نژاد
#
###########################################################
# #
# carrots  >>>>>>> (255, 128, 0)
#
#   1       >>      217.6 153.6 100.6
#   2       >>      216.0 185.1 138.1
#   3       >>      201.4 137.1 80.9
#   4       >>      220.1 166.6 106.3
#   5       >>      168.8 122.8 77.3
# --------------------------------------------
# pumpkin  >>>>>>> (255, 128, 0)
#
#   1       >>      201.6 120.4 54.3
#   2       >>      149.3 69.4 16.2
#   3       >>      213.8 112.7 34.9
#   4       >>      215.0 126.2 88.8
#   5       >>      212.9 131.0 56.4
#   6       >>      170.6 83.0 27.2
#
###########################################################
# count each gray level
#   0,    1,    2,   3,    4,    5, ..., 153, 254, 255
#
#   0    32    85  136   165   179  ...
#
# print(ratio)
# carrot 1  >>  0.38297
# carrot 2  >>  0.86165
# carrot 3  >>  0.17889
# carrot 4  >>  0.49937
# carrot 5  >>  0.17848
# -------------------------
# pumpkin 1  >>  0.03036
# pumpkin 2  >>  0.00524
# pumpkin 3  >>  0.07952
# pumpkin 6  >>  0.02693
