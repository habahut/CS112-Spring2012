#! usr/env/bin python

class Student(object):      #classes should have a capital letter
    def __init__(self, name="Jane Doe"):
        self.name = name
        
    def say(self, message):
        print self.name + " : " + message

    def sayTo(self, other, message):
        self.say(message +"," +other.name)

    def printMe(self):
        print self.name

class Course(object):
    def __init__(self,name):
        self.name = name
        self.enrolled = []

    def enroll(self, student):
        self.enrolled.append(student)

    def printMe(self):
        for s in self.enrolled:
            s.printMe()


bob = Student("Bob")

fred = Student("Fred")
j = Student()

j.say("pointless")
bob.say("hi fred")
fred.say("go away bob")

cs112 = Course("CS112")
cs112.enroll(bob)
cs112.enroll(fred)
cs112.printMe()

bob2 = bob
print bob2 is bob
