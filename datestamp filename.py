# -*- coding: utf-8 -*-
"""
#==============================================================================
                #                   .~- datetime-rename ~-.
                #
                #                    Created on 12/11/12
                #                          10:20 am
                #                        @author: paul
                #
                #            ~ Living Water International ~
#==============================================================================

"""
    # Our import statements which import external libraries.
import os
from datetime import datetime


    # The fallowing three lines set the runtime directory for python to the directory
    # containing the script. It is only necessary when the script is being run from another
    # program or service- such as Commence - it is not needed if you manually run the file,
    # it may even need to be commented out when running it manually.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

    # using the datetime library to get todays date,
    # then setting the format we want it in
    # unformatted the value of 'd' would return
    # this> 'datetime.datetime(2012, 10, 6, 0, 11, 37, 641000)'
d = datetime.today()
dstamp = d.strftime("-%d%m%Y")

    # here were just setting the name of the file that we want to change
    # I will probably edit this to be a value that is passed in to the script
    # at runtime- so that the same script can be used for different filenames.
    # this is done using 'sys.argv' - http://docs.python.org/2/library/sys.html
filename = 'new'
extension = '.txt'

    # Combine the filename and extension to create the actual filename
    # then doing the same thing but adding in the timestamp
oldname = str(filename + extension)
newname = str(filename + dstamp + extension)

    # This is a Try/Catch statement to catch the error in the event
    # that the file does not exist. The Except statement
    # tells it what to do in the event an exception is raised. In this case
    # just printing some text to the console, could modify it to write to an
    # error log.
try: os.rename(oldname, newname)
except: print('file is not there')