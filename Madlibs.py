import os
import sys
import re
import string
from pprint import pprint

fileContent = ""        # Gobal var for fileContent
f = open(sys.argv[1])   # Open the given file at sys.argv[1]

if f:
    fileContent = f.read().splitlines()     # read file and split into lines

f.close()               # close the file

out = open(sys.argv[2], 'w')    # open in write mode so as to clear out any previous text from testing

if out:
    vowels = ["a", "e", "i", "o", "u"]
    for line in fileContent:
        # get array of square braces and inside capture group as well
        inputsNeeded = re.findall('(\[(.+?)\])', line)
        numInputs = len(inputsNeeded)

        # loop over array to generate output
        if numInputs == 0:          # If line has no inputs needed, just write the line
            out.write(line + "\n")
        else:
            for item in inputsNeeded:                                           # loop over inputsNeeded
                article = "a "                                                  # just working on the grammar
                if item[1][0].lower() in vowels:                                # update the grammar
                    article = "an "
                userInput = input("Please enter " + article + item[1] + ":  ")     # get user input using second capture group
                line = line.replace(item[0], userInput, 1)                         # construct new line with user inputs
            out.write(line + "\n")                                              # write to output file

out.close()     # close output file
