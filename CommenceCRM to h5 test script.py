# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:27:24 2012

@author: paul
"""

import win32com.client
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from tables import *
#from first import Ui_qry_commence



filename = "cdata.h5"

h5file = openFile(filename)
table = h5file.root.Contributions.Person


#
#class People(IsDescription):
#    personID  = StringCol(16, pos=1)   # Integer
#    firstName = StringCol(16, pos=2)   # 16-character String
#    lastName  = StringCol(16, pos=3)
#





#getFields = ["PersonID", "First Name", "Last Name"]
##CMC_MAX_ROWS = int(self.ui.CMC_MAX_ROWS.text())
##CMC_ROW_COUNT = int(self.ui.CMC_ROW_COUNT.text())
#CMC_DELIM =  "<<%\%||%/%>>"
#CMC_CURSOR_CATEGORY = 0
#CMC_FLAG_DEFAULT = 0
#
#cmcCommence = win32com.client.Dispatch("Commence.DB")
#cursPerson = cmcCommence.GetCursor(1, "People", 0)
#cursPerson.SetFilter("", 0)


#ghble = h5file.createTable(group, "Person", People, "People from Commence")


#h5file = openFile(filename)
#table = h5file.root.Contributions.Person


#for x in getFields:
#    cursPerson.SetColumn(getFields.index(x), x, 0)

#h5file.close()
#        self.ui.person_table.data = htable.read()
#

#data = htable.read()
#
