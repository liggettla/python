#argv is a list containing the arguments passed to the python interpreter
from sys import argv

#run this script like this:
#python ex15.py ex15_sample.txt
script, filename = argv

#this opens the ex15_sample.txt file
txt = open(filename)

#prints out the contents of ex15_sample.txt with txt.read()
print "Here's your file %r:" %filename
print txt.read()

#takes user input for the ex15_sample.txt
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
