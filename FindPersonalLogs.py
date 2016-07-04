#!/usr/bin/env python
"""
Takes in arguments and parses through all .txt files in the current directory
and all subdirectories searching for the specified string(s). If one of the
strings is found, it will print the line number and the whole line in which
it was found.

__author__ = "Steve McLaughlin"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Steve McLaughlin"
__status__ = "Prototype"

"""

import os
import os.path
import sys

if len(sys.argv) < 2:
    print 'No arguments passed in. Exiting...'
    sys.exit(0)

argz = []
for arg in sys.argv:
    argz.append(arg)


print 'Starting to search'

# Goes through the current directory and its subdirectories and counts
# the number of files with the file extension
def getNumFiles():
    numfiles = 0
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".txt")]: # Any .txt
            numfiles += 1
    return 'There are {0} files with that extension in this directory and its subdirectories'.format(numfiles)

# Converts a line into all lower case letters for case insensitive parsing
def iterLower(line):
    s = line
    return s.lower()

# Parses through each file and checks for the specified strings
# Note: This is currently a case insensitive search
def parseFiles():
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".txt")]: # Any .txt
            print os.path.join(dirpath, filename)
            with open(os.path.join(dirpath, filename), "r") as infile:
                for num, line in enumerate(infile, 1):
                    if any(s.lower() in iterLower(line) for s in argz):
                        output = 'Line ' + `num`
                        print output
                        print line
            print #Just a newline for formatting purposes


print getNumFiles()
parseFiles()
