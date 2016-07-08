#!/usr/bin/env python
"""
Takes in arguments and parses through all .txt files in the current directory
and all subdirectories searching for the specified string(s). If one of the
strings is found, it will print the line number and the whole line in which
it was found.

__author__ = "Steve McLaughlin"
__updated__ = "7/8/2016"

__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Steve McLaughlin"
__status__ = "Prototype"

"""

import os
import os.path
import sys
from itertools import islice

if len(sys.argv) < 2:
    print 'No arguments passed in. Exiting...'
    sys.exit(0)

argz = []
for arg in sys.argv:
    argz.append(arg)

# Converts a line into all lower case letters for case insensitive parsing
def iterLower(line):
    s = line
    return s.lower()

print 'Starting to search'

# Goes through the current directory and its subdirectories and counts
# the number of files with the file extension
files = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".txt")]: # Any .txt
        files.append(os.path.join(dirpath, filename))

print'There are {0} files with that extension in this directory and its subdirectories'.format(len(files))

# Parses through each file and checks for the specified strings
# Note: This is currently a case insensitive search
for file in files:
    if(os.path.isfile):
        fileData = open(file, 'r')
        for num, line in enumerate(fileData, 1):
            if any(s.lower() in iterLower(line) for s in argz):
                lineNum = file + ' Line: ' + `num`
                print lineNum.rstrip('\n')
                print (line).rstrip('\n')
                #print (line.join(islice(fileData,1))).rstrip('\n') # prints the current line and the next line
                print # this is just here for formatting
        fileData.close()
