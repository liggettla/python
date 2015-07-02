from time import sleep

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there aren't 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #this is the same as more_stuff.pop(0)
    print "Adding: ", next_one
    sleep(1)
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #whoa! fancy
print stuff.pop()
print ' '.join(stuff) #join together all list elements with the ' ' char
print '#'.join(stuff[3:5]) #join elements stuff[3] and stuff[4] together because this is 3-5 not including 5
