import pygame 
from numpy import *
from math import *
from random import *
from time import *
from os import *
from PIL import ImageTk, Image
import sys
#=====
pygame.init()
#=====
white = (255,255,255) 
black = (0,0,0) 
red = (255,0,0) 
orange = () 
yellow = (255,255,0) 
green = (0,255,0) 
blue = (0,0,255) 
indigo = () 
magenta = ()
#=====
Button_text = pygame.font.SysFont('Garamond',40)
Pycraft_logo_text = pygame.font.SysFont('Garamond', 100)
smallIcon_Text = pygame.font.SysFont('Garamond', 10)
#=====
Button_output = 'HomeScreen'
#=====
running = True
#=====
FPS = 60
Display_X = 1350
Display_Y = 659
clock = pygame.time.Clock()
#FramesPerSec = pygame.time.Clock.get_fps()
gameSurface = pygame.display.set_mode((Display_X,Display_Y))
pygame.display.set_caption("Pycraft")
#=====
while running == True:
#=====
    clock.tick(FPS)
#=====
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get(): 
        if (event.type == pygame.KEYDOWN): 
            if (event.key == pygame.K_ESCAPE):
                running = False
#=====
    Frames = smallIcon_Text.render(FramesPerSec, 1, white)
    gameSurface.blit(Frames, [0,0])
#=====
    if Button_output == 'HomeScreen':
        gameSurface.fill(black)

        label1 = Button_text.render("Play", 1, white)
        gaButton_face.blit(label1, [1000, 100])
        label2 = Button_text.render("Settings", 1, white)
        gaButton_face.blit(label2, [1000, 160])
        label3 = Button_text.render("Ability Controls", 1, white)
        gaButton_face.blit(label3, [1000, 220])
        label4 = Button_text.render("Player Skin", 1, white)
        gaButton_face.blit(label4, [1000, 280])
        label5 = Button_text.render("Credits", 1, white)
        gaButton_face.blit(label5, [1000, 340])
        label6 = Pycraft_logo_text.render("Pycraft", 1, white)
        gameSurface.blit(label6, [500, 0])
#=====
    pygame.display.update()
#=====
sys.exit("Shutting Down...")