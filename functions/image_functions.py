############################### Image Processing Functions ###############################
from PIL import Image




def load_image(image_file):
    im = Image.open(image_file)
    width, height = im.size          # Tuple Unpacking
    pixels = list(im.getdata())
    return width, height, pixels


def view_image(some_pixels, im_w, im_h):

    new_im = Image.new(mode = "L",
                    size = (im_w, im_h),
                    color = 0)
    new_im.putdata(some_pixels)
    new_im.show()
