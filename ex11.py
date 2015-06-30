#input() can be used in place of raw_input(), but it tries to convert input
#into python code, potentially causing security problems

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#print raw_input('What is your name? ')
x = raw_input('What is your name? ')
print "Your name is " + x


print "Enter a number"
x = input()
print "This is your number %r" % x
#x = int(raw_input()),
#print x + "5"
