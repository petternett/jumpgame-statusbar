import sys
import imageio.v3 as iio
from Common import map_to_coords
# import numpy as np

# TODO support for SPACE, and symbols
# TODO bounds checking

class Text:

    CHAR_WIDTH = 3

    def __init__(self, img_path):

        self.char_coords  = {}


        # Read image data
        img_data = iio.imread(img_path)

        # Get rid of color channels and flatten them
        img_data = img_data[:,:,-1:].reshape(4,-1)

        # Convert into dictionary of 2D arrays
        start = 0
        end = start + Text.CHAR_WIDTH

        # A-Z
        for letter_ord in range(ord('A'), ord('Z')+1):
            # Slice character and map to coordinates
            self.char_coords[letter_ord] = map_to_coords(img_data[:, start:end].tolist())
            start += Text.CHAR_WIDTH + 1
            end = start + Text.CHAR_WIDTH

        # 0-9
        for number in range(0, 10):
            # Slice character and map to coordinates
            self.char_coords[number] = map_to_coords(img_data[:, start:end].tolist())
            start += Text.CHAR_WIDTH + 1
            end = start + Text.CHAR_WIDTH

    def get_char(self, char):
        return self.char_coords[ord(str(char))] if isinstance(char, int) else self.char_coords[ord(char)]

    def to_string(self, chars, pos_x):
        ret_coords = []

        offs_x = pos_x
        for char in chars:
            char = self.get_char(char)
            ret_coords += (list(tuple(map(lambda x: (x[0]+offs_x, x[1]), char))))
            offs_x += Text.CHAR_WIDTH + 1

        return ret_coords
