#!usr/bin/python
from random import randrange

import pygame
from pygame import Color,Rect,Surface
from pygame.locals import *
from pygame.sprite import Sprite

class Player(Sprite):
    size = w,h = 40,40
    color = 0,255,0
    health = 10
    def __init__(self, game):
        Sprite.__init__(self)
        self.image = Surface(self.size).convert_alpha()
        pygame.draw.polygon(self.image,self.color,[(0,self.h),(self.w/2,0),(self.size)])
        self.rect = self.image.get_rect()
        self.rect.midbottom = game.w/2, game.h - self.h/2
        self.game = game

    def hurt(self, n):
        self.health -= n
        if self.health <= 0:
            self.kill()
            
    def update(self,x):
        self.rect.centerx = x
        self.rect = self.rect.clamp(self.game.bounds)

class Enemy(Sprite):
    size = w,h = 40,40
    color = 255,0,0
    dx,dy = 4,2
    score = 1
    
    def __init__(self, game, pos=None):
            
        Sprite.__init__(self)
        self.game = game
        self.image = Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        
        pygame.draw.ellipse(self.image,self.color,self.rect)

        if pos is None:
            pos = randrange(self.game.w - self.w), -self.h
        self.rect.topleft = pos
        self.dx = self.dx if randrange(2) else -self.dx
        
    def update(self):
        self.rect.move_ip(self.dx, self.dy)
        self.rect = self.rect.clamp(self.game.bounds)
        if self.rect.left == 0 or self.rect.right == self.game.bounds.right:
            self.dx = -self.dx

        if self.rect.bottom == self.game.bounds.bottom:
            self.kill()
            if self.game.player.alive():
                self.game.score -= self.score
                print self.game.score

class Missile(Enemy):
    color = 0,128,128
    size = w,h = 10,40
    dx,dy = 0,8
    score = 0


class Spawner():
    def __init__(self,game,group):
        self.game = game
        self.group = group
        self.types = {}
        
    def add(self,typ,freq):
        self.types[typ] = freq

    def create(self, typ):
        return typ(self.game)

    def spawn(self):
        step = self.game.step
        for typ,freq in self.types.items():
            if step % freq ==  0:
                obj = self.create(typ)
                self.group.add(obj)

class Broodling(Enemy):
    size = w,h = 10,10
    dx,dy = 5,5
    score = 0.5
    color = 200,200,200
    

class Breeder(Enemy,Spawner):
    color = 128,128,128
    size = w,h = 50,50
    dx,dy = 0,1
    score = 5
    health = 10
    def __init__(self,game):
        Enemy.__init__(self,game)
        Spawner.__init__(self,game,game.enemies)
        Spawner.add(self,-1,30)
        Spawner.add(self,0,30)
        Spawner.add(self,1,30)

    def create(self,speed):
        x,y = self.rect.midbottom
        x -= Broodling.w/2
        ling = Broodling(self.game, (x,y))
        ling.dx = abs(ling.dx) * speed
        return ling
        
    def update(self):
        self.spawn()
        Enemy.update(self)        
    
    def kill(self):
        self.health -= 1
        if self.health <= 0:
            Enemy.kill(self)
                   
class Bullet(Sprite):
    size = w,h = 5,15
    color = 255,255,0
    dy = 15
    def __init__(self,game,pos):
        Sprite.__init__(self)
        self.game = game
        self.image = Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        self.rect.midbottom = pos
    def update(self):
        self.rect.y -= self.dy
        if self.rect.top == 0:
            self.kill()

class Shield(Sprite):
    size = w,h = 80,40
    health = 255
    def __init__(self,pos):
        Sprite.__init__(self)
        self.image = Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image.fill((255,0,255))
    def hurt(self, n):
        self.health -= n
        if self.health <= 0:
            self.kill()
        else:
            self.image.fill((self.health, 0, self.health))

class Explosion(Sprite):
    color = 255,128,0
    def __init__(self,obj):
        self.image = Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        pygame.draw.ellipse

class Game():
    size = w,h = 800,600
    title = "Title"
    background = Color(0,0,0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size,HWSURFACE|DOUBLEBUF)
        pygame.display.set_caption(self.title)
        pygame.mouse.set_visible(False)
        self.score = 0
        self.bounds = self.screen.get_rect()
        self.player = Player(self)
        self.player_grp = pygame.sprite.GroupSingle(self.player)
        self.enemies = pygame.sprite.Group()
        self.spawner = Spawner(self, self.enemies)
        self.spawner.add(Missile, 40)
        self.spawner.add(Enemy, 20)
        self.spawner.add(Breeder, 80)
        
        self.bullets = pygame.sprite.Group()
        self.shields = pygame.sprite.Group()
        self.shields.add(Shield((80,480)))
        self.shields.add(Shield((240,480)))
        self.shields.add(Shield((620,480)))
        self.shields.add(Shield((460,480)))
        
    def run(self):
        done = False
        self.step = 0
        clock = pygame.time.Clock()
        while not done:
            #input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    self.bullets.add(Bullet(self,self.player.rect.midtop))
                    
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(30)
            self.step+=1
            
    def update(self):
        x,y = pygame.mouse.get_pos()
        self.player.update(x)

        self.spawner.spawn()

        self.enemies.update()
        self.bullets.update()
        
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.player.hurt(1)

        for bullet,enemy in pygame.sprite.groupcollide(self.bullets, self.enemies,True, True).items():
            self.score+=1
            print self.score
            
        for shield,sprite in pygame.sprite.groupcollide(self.shields, self.bullets, False, True).items():
            shield.hurt(20)
            
        for shield,enemy in pygame.sprite.groupcollide(self.shields, self.enemies, False, True).items():
            shield.hurt(64)
            
    def draw(self):
        self.screen.fill(self.background)
        self.player_grp.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)
        self.shields.draw(self.screen)
        # healthbar
        self.screen.fill((0,255,255), (0,0,self.player.health*80,10))

if __name__ == "__main__":
    Game().run()
    print "Bye"
