#argv is a list containing the arguments passed to the python interpreter
from sys import argv
from os.path import exists

#run scipt like this: python ex17.py test17.txt new_file17.txt
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do thes two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

#len() here gives the size of the file in bytes
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
