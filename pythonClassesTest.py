class Glass(object):
    def __init__(self, size):
        assert size > 0
        self.size = float(size) #an attribute of a class
        self.content = float(0.0) #another attribute

    def __repr__(self):
        if self.content == 0.0:
            return "An empty glass of size %s" %(self.size)
        else:
            return "A glass of size %s cl containing %s cl of water" %(self.size, self.content)

    def fill(self):
        self.content = self.size

    def empty(self):
        self.content = float(0.0)

    def fillAndDrink(self):
        self.content = self.size
        self.content = self.content - 1.0

    def drink(self):
        self.content = self.content - 1.0

def main():
    myGlass = Glass(10)
    print myGlass
    myGlass.fill()
    print myGlass
    myGlass.empty()
    print myGlass
    myGlass.fillAndDrink()
    print myGlass
    myGlass.drink()
    print myGlass
    myGlass.drink()
    print myGlass
    myGlass.drink()
    print myGlass
    myGlass.drink()
    print myGlass


main()
