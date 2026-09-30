############################### Image Processing Functions ###############################
from PIL import Image
import random



def load_image(image_file):
    # Convert every image to RGB so the rest of the functions always receive
    # (red, green, blue) tuples, even for PNG or WebP files with transparency.
    with Image.open(image_file) as im:
        rgb_im = im.convert("RGB")
        width, height = rgb_im.size          # Tuple Unpacking
        pixels = list(rgb_im.getdata())
    return width, height, pixels


def remove_bg(pixels, white_threshold=250):
    """Return the pixels that are not part of a near-white background."""
    no_bg_pixels = []

    for p in pixels:
        r, g, b = p[:3]
        if r < white_threshold or g < white_threshold or b < white_threshold:
            no_bg_pixels.append((r, g, b))

    return no_bg_pixels


def rgb_averages(pixels):
    """Calculate and return the average red, green, and blue values."""
    if not pixels:
        raise ValueError("Cannot calculate RGB averages: no foreground pixels found.")

    sum_r = 0
    sum_g = 0
    sum_b = 0

    for p in pixels:
        sum_r += p[0]
        sum_g += p[1]
        sum_b += p[2]

    total_pixels = len(pixels)
    avg_r = round(sum_r / total_pixels, 1)
    avg_g = round(sum_g / total_pixels, 1)
    avg_b = round(sum_b / total_pixels, 1)

    return avg_r, avg_g, avg_b


def detect_color_family(r_, g_, b_):
    color_fam = None

    # RED
    if r_ > g_ and r_ > b_:
        color_fam = "RED"

    # GREEN
    if g_ > r_ and g_ > b_:
        color_fam = "GREEN"

    # BLUE
    if b_ > r_ and b_ > g_:
        color_fam = "BLUE"

    # ORANGE
    if r_ > 150 and g_ > 60 and g_ < 190 and b_ < 120:
        color_fam = "ORANGE"

    # BLACK
    if r_ < 40 and g_ < 40 and b_ < 40:
        color_fam = "BLACK"

    # WHITE
    if r_ > 200 and g_ > 200 and b_ > 200:
        color_fam = "WHITE"

    # YELLOW
    if r_ > 180 and g_ > 150 and b_ < 120:
        color_fam = "YELLOW"

    # PINK
    if r_ > 180 and b_ > 130 and g_ < 190:
        color_fam = "PINK"

    return color_fam


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

def rgb2gray(rgb_pixels):
    gray_pixels = []
    for p in rgb_pixels:
        avg_p = (p[0] + p[1] + p[2]) / 3
        gray_pixels.append(round(avg_p))
    return gray_pixels


# Keep the old misspelled function name working for earlier exercises.
def grb2gray(rgb_pixels):
    return rgb2gray(rgb_pixels)


def get_hist_data(gray_pixels):
    """Count how many pixels have each grayscale value from 0 to 255."""
    lst_hist = [0] * 256

    for p in gray_pixels:
        lst_hist[p] += 1

    return lst_hist


def calc_ratio(lst_hist, threshold):
    """Return the ratio of pixels at or above a grayscale threshold."""
    total_pixels = sum(lst_hist)

    if total_pixels == 0:
        return 0

    bright_pixels = sum(lst_hist[threshold:])
    return bright_pixels / total_pixels


def show_histogram(lst_hist):
    """Display grayscale histogram data as a bar chart."""
    from matplotlib import pyplot

    pyplot.bar(range(256), lst_hist)
    pyplot.xlabel("Gray value")
    pyplot.ylabel("Number of pixels")
    pyplot.title("Grayscale Histogram")
    pyplot.show()

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
