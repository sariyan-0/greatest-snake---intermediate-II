############### Image Project ####################

from PIL import Image
from functions.image_functions import *

w, h, pixels = load_image('images/pumpkin/6.jpg')

# print(pixels[:10])

no_bg_pixs = remove_bg(pixels)

# print(no_bg_pixs[:20])

r_, g_, b_ = rgb_averages(no_bg_pixs)

print(r_, g_, b_)


# carrots >>>>>>> (255, 128, 0)
#
# 1   >>   217.6 153.6 100.6
# 2   >>   216.0 185.1 138.1
# 3   >>   201.4 137.1 80.9
# 4   >>   220.1 166.6 106.3
# 5   >>   168.8 122.8 77.3
#
# --------------------------------------------
#
# pumpkin >>>>>>> (255, 128, 0)
#
# 1   >>   201.6 120.4 54.3
# 2   >>   149.3 69.4 16.2
# 3   >>   213.8 112.7 34.9
# 4   >>   215.0 126.2 88.8
# 5   >>   212.9 131.0 56.4
# 6   >>   170.6 83.0 27.2


def detect_color_family(r_, g_, b_):

    color_fam = None

    # RED
    if r_ > g_ and r_ > b_:
        color_fam = 'RED'

    # GREEN
    if g_ > r_ and g_ > b_:
        color_fam = 'GREEN'

    # BLUE
    if b_ > r_ and b_ > g_:
        color_fam = 'BLUE'

    # ORANGE
    if r_ > 150 and g_ > 60 and g_ < 190 and b_ < 120:
        color_fam = 'ORANGE'

    # BLACK
    if r_ < 40 and g_ < 40 and b_ < 40:
        color_fam = 'BLACK'

    # WHITE
    if r_ > 200 and g_ > 200 and b_ > 200:
        color_fam = 'WHITE'

    # YELLOW
    if r_ > 180 and g_ > 150 and b_ < 120:
        color_fam = 'YELLOW'

    # PINK
    if r_ > 180 and b_ > 130 and g_ < 190:
        color_fam = 'PINK'

    return color_fam


color_family = detect_color_family(r_, g_, b_)

print("Color Family:", color_family)


##################################################
#
#                   Type     >>>     for each Type
#
# سبز               x 10              x 20 image
#
# طلایی             x 10              x 20 image
#
# گل                x 10              x 20 image
#
# نارنجی            x 10              x 20 image
#
# سفید              x 10              x 20 image
#
# میوه              x 10              x 20 image
#
# قطعات سخت افزار کامپیوتر (hard)
#
# اجسام             x 200             x 1 or 2
#
##################################################