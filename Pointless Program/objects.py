#! urs/bin/env

class Vector:
    # static methods don't have access to "self" or any class variables
    @staticmethod
    def dot(a,b):
        print "no"

#Vector.dot(a,b)

class Enemy(object):
    #underscore means "private variable"
    _objects = []
    """
    # every instance can get to this group
    # _allBullets = Group()

    #def shoot(self):
    ## enemy class tracks all bullets, sprite tracks its own individual bullets
    #   Bullet(Enemy._allBullets, self.bullets)
    # can also stores a group of tie fighters and a group of all enemies
    # then you can just call tiefighters.group.kill() and commit genocide
    # without touching any of the other enemies
    """

    def __init__(self, name):
        self.name = name
        Enemy._objects.append(self)

    def update(self):
        print self.name, "i'm in your base"

    def kill(self):
        print self.name, "is dead"
        Enemy._objects.remove(self)

    # this is per function, each function that is to be
    # a class variable needs to have this thing preceeding it
    @classmethod
    def all(cls):   #cls refers to "class Enemy," not self, the whole class
        # [:] creates a copy of the list
        # returning the actual list will modify the list here as well
        return cls._objects[:] # can return objects or class variables but not instance variables

    @classmethod
    def spawn(cls, bounds):
        x,y = 0,0   #change this from zeros to other stuff
        vx,vy = 0,0
        color = 255,0,100
        ## actually instantiate the enemey
        "return Enemy(x,y,vx,vy,color,bounds)" # calls the __init__ function here

#Enemy.spawn(screen.get_rect())

a = Enemy("A")
b = Enemy("B")
c = Enemy("C")

for enemy in Enemy.all():
    enemy.update()

c.kill()

for enemy in Enemy.all():
    enemy.update()
