################################### Pillow ###################################
#
# python -m pip install Pillow
#
# ----------------------------------------------------------------------------
from PIL import Image

im = Image.open("images/gray_scale.png")
# im.show()
image_size = im.size    #   (768, 512)
print(image_size)       # (width, height)
#
pixels = list(im.getdata())
# print(pixels[:20])
# ----------------------------------------------------------------------------
# convert into a binary image
binary_pixels = []
for p in pixels:
    if p < 128:
        binary_pixels.append(0)
    else:
        binary_pixels.append(255)
# ----------------------------------------------------------------------------
# new_im = Image.new(mode = "L",
#                    size = image_size,
#                    color = 0)
# new_im.putdata(binary_pixels)
# new_im.show()
# print(len(binary_pixels))
# ----------------------------------------------------------------------------
# Q2: convert an RGB image into a gray scale image
#
im = Image.open("images/rgb_image.png")
im_size = im.size   # (768, 512)
print(im_size)     #(width, height)
pixels = list(im.getdata())
print(pixels[:20])
