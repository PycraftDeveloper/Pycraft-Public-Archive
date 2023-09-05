print("--Running PycraftRunUtil")
try: # checks all modules are installed
    from tkinter import *
    from tkinter.ttk import *
    from PIL import Image, ImageTk
    import pygame, numpy
    from pygame.locals import *
    pygame.init()
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    import pyautogui
    import timeit
except: # is a module is not installed then
    try:
        import PycraftINIT # ...and run the installer (To FIX)
    except:
        crash = True
    else:
        contINT=0
else: # if the modules are installed then:
    contINT=0 # ingnore this and move on to the rest of the program

import os, sys, time, random, pip, subprocess

if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'

def crash(error):
    try:
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
                self.pack(fill=BOTH, expand=1)
                load = Image.open("D:\\PYGAME\\Resources\\Error_Resources\\Error_Message.JPG")
                render = ImageTk.PhotoImage(load)
                img = Label(self, image=render)
                img.image = render
                img.place(x=-10, y=0)
                
        root = Tk()
        app = Window(root)
        root.wm_title("An Error Occured")
        root.iconbitmap("D:\\PYGAME\\Resources\\Error_Resources\\Icon.ico")
        root.geometry("1200x590")
        root.resizable(False,False)
        root.configure(bg="#141414")
        pygame.quit()
        errorID = Label(root, text=str(error), background="#141414", foreground='red', font=("Book Antiqua", 15))
        errorID.pack(expand=True)
        root.mainloop()
    except Exception as InternalError:
        print(InternalError)
        sys.exit("Oops something didn't work as intended")
    else:
        contINT=0

if crash == True:
    crash()
else:
    contINT=0

try:
    import Pycraft_20p1009_20a
except Exception as error:
    print(error)
    crash(error)
else:
    contINT=0