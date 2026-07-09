################################### Pillow ###################################
#
# python -m pip install Pillow
#
# ----------------------------------------------------------------------------
import random
from PIL import Image

from functions.image_functions import *

w, h,pixs = load_image("images/gray_scale.png")



im = Image.open("images/gray_scale.png")
# im.show()
image_size = im.size    #   (768, 512)
# print(image_size)       # (width, height)
#
pixels = list(im.getdata())
# print(pixels[:20])
# ----------------------------------------------------------------------------
# convert into a binary image
binary_pixels = []
for p in pixs:
    if p < 128:
        binary_pixels.append(0)
    else:
        binary_pixels.append(255)
# ----------------------------------------------------------------------------
view_image(binary_pixels, w, h)
# ----------------------------------------------------------------------------
# Q2: convert an RGB image into a grayscale image
#
im = Image.open("images/rgb_parrot.png")
im_size = im.size   # (768, 512)
print(im_size)     #(width, height)
pixels = list(im.getdata())
# print(pixels[:20])
# ----------------------------------------------------------------------------
gray_pixels = []
for p in pixels:
    avg_p = (p[0] + p[1] + p[2]) / 3
    gray_pixels.append(round(avg_p))

# print(gray_pixels[:20])
# ----------------------------------------------------------------------------
new_im = Image.new(mode = "L",
                     size = im_size,
                        color = 0)
# new_im.putdata(gray_pixels)
# new_im.show()
# ############################################################################
# Q3: Add some noice to the grayscale image
# im = Image.open("images/gray_scale.png")
# image_size = im.size
# pixels = list(im.getdata())
# ----------------------------------------------------------------------------
# noisy_pixels = []
# for p in pixels:
#     noise = random.randint(-20, 20)
#     new_p = p + noise
#     noisy_pixels.append(new_p)
# ----------------------------------------------------------------------------
# new_im = Image.new(mode = "L",
#                         size = image_size,
#                         color = 0)
# new_im.putdata(noisy_pixels)
# new_im.show()
# ############################################################################
# Q4: Add some noice to an RGB image
# im = Image.open("images/rgb_parrot.png")
# image_size = im.size
# pixels = list(im.getdata())
# ----------------------------------------------------------------------------
# noisy_pixels = []
# for p in pixels:
#     noisy_r = p[0] + random.randint(-150, 150)
#     noisy_g = p[1] + random.randint(-150, 150)
#     noisy_b = p[2] + random.randint(-150, 150)

#     noisy_pixels.append((noisy_r, noisy_g, noisy_b))
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
