#This is a game made in the style of ex43.py
from sys import exit
from random import randint
from random import choice #chooses random char in string

class Engine():

    def play(self):
        name = raw_input("Input Player Name: ")
        player = Character(name)
        print "\nPlayer Name: %s" % (player.name)
        print "Player Attack: %i" % (player.attack)
        print "Player Defense: %i" % (player.defense)
        print "Player Speed: %i\n" % (player.speed)

        friendName = friends()
        friend = Character(friendName)
        print "\nYour Friend's Name: %s" % (friend.name)
        print "Your Friend's Attack: %i" % (friend.attack)
        print "Your Friend's Defense: %i" % (friend.defense)
        print "Your Friend's Speed: %i\n" % (friend.speed)

class Character(object):

    def __init__(self, object):
        self.attack = randint(1,100)
        self.defense = randint(1,100)
        self.speed = randint(1,100)
        self.name = object

class Scene(object):
    pass

def friends():
    capitals = 'QWRTYPSDFGHJKLZXVBNM'
    vowels = 'aeiou'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    name = ''

    for i in range(randint(2,10)):
        if i == 0:
            letter = choice(capitals)
            name = name + letter
        elif i%2 == 1:
            letter = choice(vowels)
            name = name + letter
        elif i%2 == 0:
            letter = choice(consonants)
            name = name + letter
    return name


game = Engine()
game.play()
