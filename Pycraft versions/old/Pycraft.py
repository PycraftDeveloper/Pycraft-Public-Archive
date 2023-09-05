import tkinter as tk 
import pygame 
from numpy import *
from math import *
from random import *
from time import *
from os import *
from PIL import ImageTk, Image

pygame.init()

root = tk.Tk()
GameSurface = tk.Canvas(root, width = 1500, height = 659, bg = 'Yellow', relief = 'flat')
GameSurface.pack()
root.title('Pycraft')
root

Home_Background = tk.PhotoImage(file="C:\\Users\\pamj0\\Documents\\Thomas' computer files\\Thomas' persional files and computer programming\\PYcraft\\PYcraft_Background.gif")
GameSurface.create_image(0, 0, anchor = tk.NW, image=Home_Background)

title = tk.Label(root, text='PYcraft', background='white')
title.config(font=('Papyrus', 70))
GameSurface.create_window(685, 80, window=title)

def Play ():
    print('Playing')
def Settings ():
    print('settings')
def Ability_Controls ():
    print('Ability Controls')
def Player_skin ():
    print('skinning')
def Credits ():
    credit = tk.Label(root, text="First, can I just say thanks to those who have read these credits,", background='white')
    credit.config(font=('Papyrus', 20))
    GameSurface.create_window(685, 150, anchor = tk.CENTER, window=credit)
    credit1 = tk.Label(root, text="If you didn't want to press this just press __ to return to the homepage.", background='white')
    credit1.config(font=('Papyrus', 20))
    GameSurface.create_window(685, 195, anchor = tk.CENTER, window=credit1)
    credit2 = tk.Label(root, text="Thanks to the coding language and all it’s extensions;", background='white')
    credit2.config(font=('Papyrus', 20))
    GameSurface.create_window(685, 240, anchor = tk.CENTER, window=credit2)
    credit3 = tk.Label(root, text="Python – 3.6.4; random, math, time, tkinter, os", background='white')
    credit3.config(font=('Papyrus', 10))
    GameSurface.create_window(685, 280, anchor = tk.CENTER, window=credit3)
    credit4 = tk.Label(root, text="Pygame", background='white')
    credit4.config(font=('Papyrus', 10))
    GameSurface.create_window(685, 300, anchor = tk.CENTER, window=credit4)
    credit5 = tk.Label(root, text="Numpy", background='white')
    credit5.config(font=('Papyrus', 10))
    GameSurface.create_window(685, 325, anchor = tk.CENTER, window=credit5)
    credit6 = tk.Label(root, text="PIL or Pillow or Python Imaging Libary", background='white')
    credit6.config(font=('Papyrus', 10))
    GameSurface.create_window(685, 350, anchor = tk.CENTER, window=credit6)

play_button = tk.Button(text='            Play           ', command=Play, bg='green', fg='white', font=('Papyrus', 12, 'bold'))
GameSurface.create_window(685, 380, window=play_button)
settings = tk.Button(text='          Settings         ', command=Settings, bg='green', fg='white', font=('Papyrus', 12, 'bold'))
GameSurface.create_window(685, 430, window=settings)
ability_controls = tk.Button(text='      Ability Controls     ', command=Ability_Controls, bg='green', fg='white', font=('Papyrus', 12, 'bold'))
GameSurface.create_window(685, 480, window=ability_controls)
player_skin = tk.Button(text='           Skin            ', command=Player_skin, bg='green' ,fg='white', font=('Papyrus', 12, 'bold'))
GameSurface.create_window(685, 530, window=player_skin)
credits = tk.Button(text='          Credits          ', command=Credits, bg='green' ,fg='white', font=('Papyrus', 12, 'bold'))
GameSurface.create_window(685, 580, window=credits)

GameSurface.mainloop()
