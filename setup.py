from distutils.core import setup
from Cython.Build import cythonize
from commonMethods_zhaozl import printWithColor

import os
import glob


files_all = os.listdir("./")
files_selected_methods = glob.glob("Method*.py")
files_selected_runs = glob.glob("run*.py")
files_selected = files_selected_methods + files_selected_runs

for item in files_selected:
	printWithColor(_msg="Now processing with >>> " + item, _fontColor='red', _backColor='yellow')
	setup(ext_modules = cythonize(item))

files_all = os.listdir("./")
files_selected_methods = glob.glob("Method*.so")
files_selected_runs = glob.glob("run*.so")
files_selected = files_selected_methods + files_selected_runs

for item in files_selected:
	print(">> ", item)
	os.rename(item, item.replace('.cpython-37m-x86_64-linux-gnu', ''))
	