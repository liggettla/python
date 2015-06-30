#argv is a list containing the arguments passed to the python interpreter
from sys import argv

#run this script like this:
#python ex16.py test16.txt
script, filename = argv

#using %r here allow actual commands to be input and converted to strings
#because %r uses repr() instead of str() to convert to a string, ie:
#d = datetime.date.today()
#str(d) returns '2011-05-15'
#repr(d) returns 'datetime.date(2011, 5, 14)'
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#w+, r+, and a+ will open a file for reading and writing
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#raw_input reads input as a string and assigns to line1,2,3
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

print "Here are the contents of the textfile:"
#opening without -w -r or -a like below implicitly uses -r
#-w writes, -r reads, -a appends
target = open(filename)
print target.read()
