#argv is a list containing the arguments passed to the python interpreter
from sys import argv
from os.path import exists

#run like this: python ex17.py test17.txt new_file17.txt
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two in one line too, how?
#in_file = open(from_file)
#indata = in_file.read()

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()    #Only needed if line 14 is run as two lines as shown in lines 11 and 12
