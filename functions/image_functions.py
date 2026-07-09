############################### Image Processing Functions ###############################
from PIL import Image
import random



def load_image(image_file):
    im = Image.open(image_file)
    width, height = im.size          # Tuple Unpacking
    pixels = list(im.getdata())
    return width, height, pixels


def view_image(some_pixels, im_w, im_h):
    if type(some_pixels[0]) == int:
        new_im = Image.new(mode = "L",
                    size = (im_w, im_h),
                    color = 0)
    if type(some_pixels[0]) == tuple:
        new_im = Image.new(mode = "RGB",
                    size = (im_w, im_h),
                    color = (0, 0, 0))
    new_im.putdata(some_pixels)
    new_im.show()

def gray2binary(gray_pixels):
    binary_pixels = []
    for p in gray_pixels:
        if p < 128:
            binary_pixels.append(0)
        else:
            binary_pixels.append(255)
    return binary_pixels

def grb2gray(rgb_pixels):
    gray_pixels = []
    for p in rgb_pixels:
        avg_p = (p[0] + p[1] + p[2]) / 3
        gray_pixels.append(round(avg_p))
    return gray_pixels

# def add_noise(pixels):
#     noisy_pixels = []
#     for p in pixels:
#         noise = random.randint(-150, 150)
#         new_p = p + noise
#         noisy_pixels.append(new_p)
#     return noisy_pixels

def add_noise(pixels, intensity):
    noisy_pixels = []
    if type(pixels[0]) == int:
        for p in pixels:
            noise = random.randint(-intensity, intensity)
            new_p = p + noise
            noisy_pixels.append(new_p)
    if type(pixels[0]) == tuple:
        for p in pixels:
            noisy_r = p[0] + random.randint(-intensity, intensity)
            noisy_g = p[1] + random.randint(-intensity, intensity)
            noisy_b = p[2] + random.randint(-intensity, intensity)

            noisy_pixels.append((noisy_r, noisy_g, noisy_b))

    return noisy_pixels