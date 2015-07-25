#Inheritance can be used to first call a function from an inherited class and then
#override it with a new function in the inheriting class

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        #super is aware of inheritance and will get the Parent class using Child and self as arguments
        #then returns whatever the altered() function returns from Parent
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
