#dont need the thing at the top because this is not an executable file

import pygame
from pygame.locals import *

class KeyDownListener(object):
    def on_keydown(self,event):
        pass

    def on_keyup(self, event):
        pass

class MouseListener(object):
    def on_click(self,event):   pass
    def on_motion(self,event):  pass

class InputManager(object):

    def __init__(self):
        self._key = []
        self._mouse = []

    def add_listener(self, listener):
        self._keydown.append(listener)

    def add_mouse_listener(self,listener):
        self._mouse.append(listener)

    """
    def old_add_listener(self):
        for key in keys:
            if key not in self._listeners:
                self._listeners[key] = []
            self._listeners[key].appened(listener)
            ####
            # key : objects listening for that key to be pressed
    """

    def handle_event(self,event):
        if event.type == KEYDOWN
            for listener in self._key:
                listener.on_keydown(event)
        elif event.type == KEYUP:
            for listener in self._key:
                listener.on_keyup(event)
        elif event.type == MOUSEBUTTONDOWN:
            for listener in self._mouse:
                listener.on_buttondown(event)
        elif event.type == MOUSEBUTTONUP:
            for listener in self._mouse:
                listener.on_buttonup(event)
        elif event.type == MOUSEMOTION:
            for listener
                # for each key that is pressed, call key_down on the objects
                # that are going to be affected by keypress
        """
        if event.type == KEYDOWN and event.key == K_SPACE:
            ##  dont want this:
            #print "game.player.jump()"
            #print "sounds.play(jump)"

            "want to call the methods from somewhere else so the"
            "input manager doesn't need to have access to every other class"
            
        elif event.type == KEYDOWN and event.key == K_RETURN:
            ##  also dont want this:
            #print "game.pause()"
            #print "game.openMenu()"
            #print "sounds.play(pause)"
        """
