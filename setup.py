#!/usr/bin/env python
"""A setuptools script for installing curse-rue"""

from setuptools import setup

setup(
    name="Curse Rue",
    version="0.0.1",
    author="Ryan Himmelwright",
    author_email="ryan.himmelwright@gmail.com",
    url='http://github.com/himmAllRight/curse-rue',
    description="An ncurses GUI appllication for rue-rss",
    license="GPL-3.0",
    keywords="rss",
    packages=['ncrue'],
    scripts=['bin/ncrue']
)
