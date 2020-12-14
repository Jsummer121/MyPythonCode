# -*- coding: utf-8 -*-

import numpy
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
import pylab as plot


url = ""
data = urllib.request.urlopen(url)
xlist = []
labels = []
names = []
firstline = True
for line in data:
    if firstline:
        names = line.strip().split(b';')
        firstline = False
    else:
        row = line.strip().split(b';')
