class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    #This replaces the functionality of the function of the same name
    #in the class behing inherited by Child, which is Parent in this case
    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
