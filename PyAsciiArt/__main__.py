#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""PyAsciiArt
    Convert image to character painting.

Usage:
    PyAsciiArt.py <file>... [--contrast C_NUMBER]
                            [--resize WIDTH]
                            [-o OUTPUT_FILE]
                            [-r]
    PyAsciiArt.py (-h | --help)
    PyAsciiArt.py --version

Example:
    PyAsciiArt.py example.png
    PyAsciiArt.py example.png --resize 100 -o result.txt
    PyAsciiArt.py example.png --resize 100 --contrast 0.5 -r

Options:
    --contrast C_NUMBER     Change the image contrast.
    --resize WIDTH          Modify image size, keep proportion by default. The unit is pixel.
    -o OUTPUT_FILE          Output filename.
    -r                      Reverse the result, dark background image may get better result
    -h --help               Show help.
    --version               Show version.

"""
import os
from docopt import docopt
from PIL import Image, ImageEnhance


def resize(image, WIDTH):

    original_width = image.size[0]
    original_height = image.size[1]
    return image.resize((int(WIDTH), int(original_height /
                                         original_width * WIDTH)), Image.NEAREST)


def main(arguments):

    for imageFile in arguments['<file>']:
        im = Image.open(imageFile)
        filename = os.path.basename(imageFile).split('.')[0]
        character = r'$@%#=;-. '

        if arguments['--resize'] is not None:
            im = resize(im, int(arguments['--resize']))

        if arguments['--contrast'] is not None:
            enh = ImageEnhance.Contrast(im)
            im = enh.enhance(1.0 + float(arguments['--contrast']))

        if arguments['-r']:
            character = character[::-1]

        interval = 256 / len(character)
        height = im.size[1]
        width = im.size[0]
        im = im.convert('L')
        if arguments['-o'] is not None:
            f = open(arguments['-o'], 'w')
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


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
