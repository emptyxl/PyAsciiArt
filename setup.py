#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyAsciiArt',
    version='0.1.0',
    description='Convert image to character painting.',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ],
    keywords='python PyAsciiArt character painting',
    author='empty_xl',
    author_email='empty_xl@163.com',
    license='MIT',
    packages=['PyAsciiArt'],
    url='https://github.com/emptyxl/PyAsciiArt',
    install_requires=[
        'Pillow',
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'PyAsciiArt = PyAsciiArt.PyAsciiArt:main'
        ]
    },
)
