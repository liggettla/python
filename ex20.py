#argv requires arguments to be passed when running the file
#run the file like this:
#python ex20.py test.txt

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)  #This seeks to the nth character in the file, not the nth line

def print_a_line(line_count, f):
    print line_count, f.readline()  #prints a particular line and advances each time it is called
                                    #readline() scans each byt of a file until if finds and \n character then stops
                                    #reading and returns what it has scanned so for

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
