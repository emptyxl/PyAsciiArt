#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""AsciiArt
    Convert image to character painting.

Usage:
    asciiArt.py <file>...   [--contrast C_NUMBER]
                            [--resize WIDTH]
                            [-o OUTPUT_FILE]
                            [-r]
    asciiArt.py (-h | --help)
    asciiArt.py --version

Example:
    asciiArt.py example.png
    asciiArt.py example.png --resize 100 -o result.txt
    asciiArt.py example.png --resize 100 --contrast 0.5 -r

Options:
    --contrast C_NUMBER     Change the image contrast.
    --resize WIDTH          Modify image size, keep proportion by default.
    -o OUTPUT_FILE          Output filename.
    -r                      Reverse the result, Dark background image may get better result
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
            im = resize(im, float(arguments['--resize']))

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
        for i in range(height):
            s = ''
            for j in range(width):
                k = im.getpixel((j, i)) // interval
                s += character[int(k)]
            s += '\n'
            f.writelines(s)
        f.close()


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
