# coding: utf-8

from setuptools import setup, find_packages

from qtorrent import __version__

REQUIREMENTS = [
    "requests==2.5.1",
    "urwid>=1.3.0",
    "lxml==3.4.2"
]


NAME = 'qtorrent'
DESCRIPTION = 'Simple interface for searching / adding torrents'
VERSION = __version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author="Kacper Krupa",
    author_email="pagenoare@gmail.com",
    packages=find_packages(),
    entry_points={
      "console_scripts": ["qtorrent = qtorrent.ui.ncurses:main"]
    },
    classifiers=[
      "Environment :: Console :: Curses",
      "Intended Audience :: End Users/Desktop",
      "Operating System :: POSIX :: Linux",
    ],
    install_requires=REQUIREMENTS,
)