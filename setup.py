#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='PyAsciiArt',
    version='1.2.2',
    description='Convert image to character painting.',
    long_description='More information you can see: https://github.com/emptyxl/PyAsciiArt',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
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
