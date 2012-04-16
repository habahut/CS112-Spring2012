#! usr/bin/env python

"""
#singleton design pattern
class InputManager(object):
    # this will only allow you to create one of the method type
    # prevents you from making too many of something
    _instance = None
    
    ## this gets called before __init__ method
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            ## super means: "the class above me, aka the class I inherited from"
            cls_instance = super(InputManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance


i = InputManager()
i2 = InputManager()

print id(i)

#useful because you can run the constructor to get the pointer to the object
print id(i2)
"""

#Manager design pattern

    # both stores information and has methods for controlling
    # and manipulating that data


"""
Game
   Main
       While not done:
           for event
                if event.type == KEYDOWN and event.key == K_SPACE
                    player.jump()

    better way:
    __init__(self):
        self.input = InputManager()
    
    for event in events:
        self.input.handle_event(event)
"""

import pygame
from pygame.locals import *

from core.input import InputManager, KeyDownListener

class Player(object):
    def move(self, direction):
        print "players moves %d, %d" %direction

    def jump(self):
        print "player jumps"


class SoundManager(object):
    def play(self, which):
        print "player %s sound" %which


class SoundController(KeyDownListener):
    def on_keydown(self, event):
        pass

class PlayerController(KeyDownListener):
    def __init__(self,player):
        self.player = player

    def on_keydown(self, event):
        if event.key == K_SPACE:
            self.player.jump()


class Game(object):
    size = 800,600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.player = Player()
        
        self.input = InputManager()
        self.input.add_listener(PlayerController(self.player),K_SPACE)

    def Quit(self):
        self._done = True

    def run(self):
        self._done = False

        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.Quit()
                else:
                    self.input.handle_event(event)

        #update

        #draw
        self.screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
        


        
