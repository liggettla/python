#This is a game made in the style of ex43.py
from sys import exit
from random import randint
from random import choice #chooses random char in string

class Engine():

    def play(self):
        name = raw_input("Input Player Name: ")
        player = Character()
        print "\nPlayer Name: %s" % (player.name)
        print "Player Attack: %i" % (player.attack)
        print "Player Defense: %i" % (player.defense)
        print "Player Perception: %i" % (player.perception)
        print "Player Stealth: %i\n" % (player.stealth)

        #friendName = NPC()
        friend = Character()
        print "\nYour Friend's Name: %s" % (friend.name)
        print "Your Friend's Attack: %i" % (friend.attack)
        print "Your Friend's Defense: %i" % (friend.defense)
        print "Your Friend's Perception: %i" % (friend.perception)
        print "Your Friend's Stealth: %i\n" % (friend.stealth)

        status = 'Alive'
        current_scene = Prison()
        while status == 'Alive':
            status = current_scene.enter()

class Character(object):

    def __init__(self):
        self.attack = randint(1,100)
        self.defense = randint(1,100)
        self.perception = randint(1,100)
        self.stealth = randint(1,100)
        self.name = NPC()

def NPC():
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

#create a dictionary with powerups and how hidden they are to determine chance of finding them
#populate a room with enemies
#Use stealth to determine numebr of moves that can be made before being found
class Scene(object):

    def initializeLoot(self):
        print "shit!"

    def initializeEnemies(self, amount):
        pass

class Prison(Scene):

    def __init__(self):
        self.Scene = Scene()
        self.Scene.initializeLoot()

    def enter(self):
        print 'You wake up in a dark and cold dungeon.\nYou do not remember from where you came but you know you must escape\n'
        action = raw_input("What do you do?  ")

        if action == 'die':
            action = 'Dead'
        elif action == 'look':
            action = 'Alive'

        return action

game = Engine()
game.play()
