#! usr/bin/env python

class BulletGroup(Group):
    def update(self, screen, playerX, playerY):
        for bullet in self:
            bullet.update(dt)

class ShipGroup(Group):
    newBulletGroup = BulletGroup()

    def update(self, screen):
        for ship in self:
            if ship.getRect().collideRect(screen):
                ##ship exists
                pass
                ## on shoot bullets will be returned here and then
                ## added to the bulletgroup
                ## need to check player coords here I guess
            
            else:
                ship.kill()



class Game(object):
    def __init__(self):
        self.
