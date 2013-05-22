# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:06:50 2012

@author: paul
"""
import win32com.client
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from tables import *


filename = "..\cdata.h5"

class Gift(IsDescription):
    giftRef = Int16Col(10, pos=1)   # Integer
    personID = StringCol(8, pos=2)   # 16-character String
    giftDate = Time64Col(pos=3)
    initials = StringCol(3, pos=4)
    total = Float32Col(pos=5)
    checkNumber = StringCol(15, pos=6)
    address1 = StringCol(16, pos=7)
    address2 = StringCol(16, pos=8)
    aptNo = StringCol(16, pos=9)



h5file = openFile(filename, "a")
group = h5file.root.Contributions
table = h5file.createTable(group, "Gift", Gift, "Gifts")