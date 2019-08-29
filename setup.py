# setup file for py2exe
# It seems to work only on Windows

from distutils.core import setup
import py2exe

setup(console = ['target.py'])  # target is the program to compile

