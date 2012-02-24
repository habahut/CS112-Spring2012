#! usr/env/bin python

class Mochila:
    CONST = 5
    
    def __init__ (self, f, l):
        print "squiggly"
        self.x = f
        self.g = l

    def lawl(self):
        print self.CONST
        return int(self.x + self.CONST)

    def fandango(self,i):
        print i
        return i + self.g
###
        
