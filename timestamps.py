# -*- coding: utf-8 -*-
"""
#==============================================================================
        #             Created on Sat Oct 06 00:19:50 2012
        #
        #                    @author: paul
        #
        #             ~ Living Water International ~
#==============================================================================


http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior

"""

from datetime import datetime

d = datetime.today()
#==============================================================================
# >>>datetime.today()   # RETURNS
# datetime.datetime(2012, 10, 6, 0, 11, 37, 641000)
#==============================================================================


dstamp = d.strftime("%d/%m/%Y")
#==============================================================================
# >>>dstamp         # RETURNS
# '06/10/2012'
#==============================================================================


tstamp = d.strftime("%d/%m/%Y - %I:%M%p")
#==============================================================================
# tstamp         # RETURNS
# '06/10/2012 - 12:11AM'
#==============================================================================


pretstamp = d.strftime("%A, %d. %B %Y %I:%M%p")
#==============================================================================
# >>>pretstamp         # RETURNS
# 'Saturday, 06. October 2012 12:11AM'
#==============================================================================


pretstamp = d.strftime("%A, %B %d. %Y %I:%M%p")
#==============================================================================
# >>>pretstamp         # RETURNS
# 'Saturday, October 06. 2012 12:11AM'
#==============================================================================
