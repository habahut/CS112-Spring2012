#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,500))


## all letters are within 40 width by 100 height boxes
def drawP(x,y, color):
    pygame.draw.line(screen, color, (x,y), (x,y+100), 5)
    pygame.draw.line(screen, color, (x,y,), (x+30,y),5)
    pygame.draw.line(screen, color, (x+30,y), (x+30,y+30), 5)
    pygame.draw.line(screen, color, (x+30,y+30), (x,y+30), 5)

def drawV(x,y, color):
    pygame.draw.line(screen, color, (x+10,y+50), (x+18,y+100),5)
    pygame.draw.line(screen, color, (x+18,y+100), (x+35,y+50), 5)
    

def drawA(x,y, color):
    pygame.draw.line(screen, color, (x,y+100), (x+18,y), 5)
    pygame.draw.line(screen, color, (x+18,y), (x+35,y+100), 5)
    pygame.draw.line(screen, color, (x+9,y+50), (x+20,y+50), 5)

def drawI(x,y, color):
    pygame.draw.line(screen, color, (x+20,y+50), (x+20,y+100), 5)
    pygame.draw.circle(screen, color, (x+20,y+25), 5)

def drawQ(x,y, color):
    pygame.draw.ellipse(screen, color, (x,y,40,100), 5)
    pygame.draw.line(screen, color, (x+25, y+75), (x+35, y+90), 5)

def drawT(x,y, color):
    pygame.draw.line(screen, color, (x+20, y+5), (x+20, y+100), 5)
    pygame.draw.line(screen, color, (x, y+5), (x+35, y+5), 5)

def drawU(x,y, color):
    pygame.draw.line(screen, color, (x,y,), (x,y+100),5)
    pygame.draw.line(screen, color, (x,y+100), (x+35,y+100), 5)
    pygame.draw.line(screen, color, (x+35,y+100), (x+35,y), 5)                     


def drawMenu(screen):
    
    ## boxes and letters
    pygame.draw.rect(screen, (100,100,100), (0,80,150,120), 3)
    drawP(20,90, (255,0,0))
    drawV(55,90, (255,255,255))
    drawP(100,90, (0,0,255))
                  
    pygame.draw.rect(screen, (100,100,100), (160,80,200,120), 3)
    drawP(185,90, (255,0,0))
    drawV(225,90, (255,255,255))
    drawA(265,90, (0,0,255))
    drawI(305,90, (0,0,255))                 

    pygame.draw.rect(screen, (100,100,100), (0,200,360,120), 3)
    drawQ(100,210, (255,255,255))
    drawU(145,210, (255,255,255))
    drawI(185,210, (255,255,255))
    drawT(220,210, (255,255,255))                    
