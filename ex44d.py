class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

#Child inherits implicit
dad.implicit()
son.implicit()

#Child overrides the override() function from Parent
dad.override()
son.override()

#Child overrides the altered() method from Parent, then uses super
#to inherit and use the original function from Parent
dad.altered()
son.altered()
