################################### Pillow ###################################
#
# python -m pip install Pillow
#
# ----------------------------------------------------------------------------
import random
from PIL import Image

from functions.image_functions import *
# Q1: convert a grayscale image into a binary image
# w, h,pixs = load_image("images/gray_scale.png")
# binary_pixels = gray2binary(pixs)
# view_image(binary_pixels, w, h)
##############################################################################
# Q2: convert an RGB image into a grayscale image
# w, h, pixs = load_image("images/rgb_parrot.png")
# gray_pixels = grb2gray(pixs)
# view_image(gray_pixels, w, h)
# ############################################################################
# Q3: Add some noice to the grayscale image
# w, h, pixs = load_image("images/gray_scale.png")
# noisy_pixels = add_noise(pixs, 50)
# view_image(noisy_pixels, w, h)
# ############################################################################
# Q4: Add some noice to an RGB image
# w, h, pixs = load_image("images/rgb_parrot.png")
# noisy_pixels = add_noise(pixs, 100)
# view_image(noisy_pixels, w, h)
# ----------------------------------------------------------------------------
# new_im = Image.new(mode = "RGB", size = image_size, color=(0,0,0))
# new_im.putdata(noisy_pixels)
# new_im.show()
# ############################################################################
# Q5: Add some noice to an RGB image
# im = Image.open("images/rgb_parrot.png")
# image_size = im.size
# pixels = list(im.getdata())
# ----------------------------------------------------------------------------
# noisy_pixels = []
# for p in pixels:
#     r = p[0]
#     g = p[1]
#     b = p[2] + 100

#     noisy_pixels.append((r, g, b))
# ----------------------------------------------------------------------------
# new_im = Image.new(mode = "RGB", size = image_size, color=(0,0,0))
# new_im.putdata(noisy_pixels)
# new_im.show()
# ############################################################################
# Q6: 
# im = Image.open("images/gray_scale.png")
# image_size = im.size
# pixels = list(im.getdata())
# ----------------------------------------------------------------------------
# new_pixels = []
# for i in range(0, len(pixels), 12):
#     box = pixels[i:i + 10]
#     avg_box = round(sum(box) / 12)
#     for j in range(12):
#         new_pixels.append(avg_box)
        
# ----------------------------------------------------------------------------  
# new_im = Image.new(mode = "L",
#                         size = image_size,
#                         color = 0)
# new_im.putdata(new_pixels)
# new_im.show()

# ############################################################################
# Q7: Detect red and green appls
w, h, pixs = load_image("images/apples/test_2.jpg")
# def apple_color(file):
#     w, h, pixs = load_image(file)
#     red_total = 0
#     green_total = 0

#     for p in pixs:
#         red_total += p[0]
#         green_total += p[1]

#     if red_total > green_total:
#         print("mostly red")
#     else:
#         print("mostly green")

# apple_color("images/apples/test_2.jpg")
# ----------------------------------------------------------------------------
# average R , G , B
# def average_rgb(file):
#     w, h, pixs = load_image(file)
#     total_pixels = w * h
#     sum_r = 0
#     sum_g = 0
#     sum_b = 0

#     for p in pixs:
#         sum_r += p[0]
#         sum_g += p[1]
#         sum_b += p[2]

#     avg_r = round(sum_r / total_pixels, 1)
#     avg_g = round(sum_g / total_pixels, 1)
#     avg_b = round(sum_b / total_pixels, 1)

#     print(avg_r, avg_g, avg_b)


# average_rgb("images/apples/test_2.jpg")
# ----------------------------------------------------------------------------
# gray_pixs = grb2gray(pixs)
# avg_gray = round(sum(gray_pixs) / (w * h), 1)
# print(avg_gray)

# if avg_gray < 100:
#     print("mostly green")
# else:
#     print("mostly red")

# ############################################################################
# Q8: Check indivial apples (read and green)
w, h, pixs = load_image("images/apples/apple.jpg")


bg_less_pixels = []
for p in pixs:
    if p[0] < 250 and p[1] < 250 and p[2] < 250:
        bg_less_pixels.append(p)

total_pixels = len(bg_less_pixels)
sum_r = 0
sum_g = 0
sum_b = 0

for p in bg_less_pixels:
    sum_r += p[0]
    sum_g += p[1]
    sum_b += p[2]

avg_r = round(sum_r / total_pixels, 1)
avg_g = round(sum_g / total_pixels, 1)
avg_b = round(sum_b / total_pixels, 1)

print(avg_r, avg_g, avg_b)