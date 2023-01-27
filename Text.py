import sys
import imageio.v3 as iio
# import numpy as np


def img_to_font(img):

    # Read image data
    img_data = iio.imread(img)

    # Get rid of color channels and flatten them
    img_data = img_data[:,:,-1:].reshape(4,-1)

    # Convert into dictionary of 2D arrays
    char_width = 3
    start = 0
    end = start + char_width

    char_dict = {}
    # A-Z
    for letter_ord in range(ord('A'), ord('Z')+1):
        char_dict[letter_ord] = img_data[:, start:end].tolist()
        start += char_width + 1
        end = start + char_width

    # 0-9
    for number in range(0, 10):
        char_dict[number] = img_data[:, start:end].tolist()
        start += char_width + 1
        end = start + char_width


    return char_dict
