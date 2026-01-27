#!/use/bin/env python3

import sys
import jupyterlab
import pandas

# NOTE: DIFFERENCES (HYPHEN VS UNDERSCORE)!
# conda install pandas-datareader vs import pandas_datareader
# Note: pep8 underlines. Here, incorrectly identifying import errors!
import pandas_datareader
import numpy
import matplotlib
import sklearn
import django
import tensorflow
import scipy
import keras
import seaborn
import cv2  # opencv-python
import nltk
import statsmodels

# print default conda environment
# import os
# print(os.environ['CONDA_DEFAULT_ENV'] + "\n")

########## Resources: Formatting strings ####################
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/string.html#formatstrings
#
# F-Strings:
# https://the-examples-book.com/programming-languages/python/printing-and-f-strings#f-strings
########## END Resources: Formatting strings ################

# old school print using % (DON'T USE! DEPRECATED!):
# print('Python version: %s' % sys.version)

# new school:
# print('Python version: {}'.format(sys.version))

# or, using F-Strings...
# print(f"Python version: {sys.version}")

# adding newlines
print('Python version: \n{}'.format(sys.version), "\n")

# print all Python version info
# print('Python version info: \n{}'.format(sys.version_info), "\n")

# jupyterlab
print('jupyterlab: {}'.format(jupyterlab.__version__))

# pandas
print('pandas: {}'.format(pandas.__version__))

# pandas-datareader
print('pandas_datareader: {}'.format(pandas_datareader.__version__))

# numpy
print('numpy: {}'.format(numpy.__version__))

# matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

# scikit-learn
print('sklearn: {}'.format(sklearn.__version__))

# django
print('django: {}'.format(django.__version__))

# tensorflow
print('tensorflow: {}'.format(tensorflow.__version__))

# scipy
print('scipy: {}'.format(scipy.__version__))

# keras
print('keras: {}'.format(keras.__version__))

# seaborn
print('seaborn: {}'.format(seaborn.__version__))

# cv2 (opencv-python)
print('cv2 (opencv-python): {}'.format(cv2.__version__))

# nltk
print('nltk: {}'.format(nltk.__version__))

# statsmodels
print('statsmodels: {}'.format(statsmodels.__version__))
