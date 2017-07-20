#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from PIL import Image, ImageEnhance


def crop(image, WIDTH):

    original_width = image.size[0]
    original_height = image.size[1]
    return image.resize((int(WIDTH), int(original_height /
                                         original_width * WIDTH)), Image.NEAREST)


def convert(fname, resize=None, contrast=None, reverse=False, output=None):
    """
    Use this function to convert image to a character painting

    - fname     Input filename
    - resize    Modify image size, keep proportion by default
                the unit is pixel, default does not crop
    - contrast  The value of changing the image contrast
    - reverse   Reverse the result, dark background image may get better
    - output    Output filename
    """

    im = Image.open(fname)
    filename = os.path.basename(fname).split('.')[0]
    character = r'$@%#=;-. '

    if resize is not None:
        im = crop(im, resize)

    if contrast is not None:
        enh = ImageEnhance.Contrast(im)
        im = enh.enhance(1.0 + float(contrast))

    if reverse:
        character = character[::-1]

    interval = 256 / len(character)
    height = im.size[1]
    width = im.size[0]
    im = im.convert('L')

    if output is not None:
        f = open(output, 'w')
    else:
        f = open(filename + '_ascii.txt', 'w')
    for row in range(height):
        s = ''
        for column in range(width):
            value = im.getpixel((column, row)) // interval
            s += character[int(value)]
        s += '\n'
        f.writelines(s)
    f.close()
