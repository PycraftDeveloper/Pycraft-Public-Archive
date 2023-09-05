print("--Running PycraftSetup")
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
import subprocess, pip, time

global root
root = Tk()
root.title("Pycraft Setup Wizard")
root.minsize(500,500)
frame = Frame(root)
frame.pack()
leftframe = Frame(root)
leftframe.pack(side=LEFT)
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
title = Label(frame, text="Pycraft", font=("Book Antiqua", 20))
title.pack()

def play():
    global root
    try:
        Display = pygame.display.set_mode((1200, 720))
        Display.fill([255,255,255])
        pygame.display.set_caption("Pycraft | Loading")
        icon = pygame.image.load("D:\\PYGAME\\Resources\\General_Resources\\Icon.jpg")
        pygame.display.set_icon(icon)
        img = pygame.image.load("D:\\PYGAME\\Resources\\General_Resources\\Pycraft_Short_Loading.JPG")
        Display.blit(img, (0,0))
        pygame.display.update()
        root.destroy()
        import PycraftRunUtil
    except Exception as error:
        print(error)
    
def install():
    if messagebox.askyesno("Caution!", "Are you sure you want to do that?") == True:
        root = Tk()
        root.title("Pycaft Setup Wizard | Installing Pycraft!")
        root.minsize(500,500)
        title = Label(root, text="Pycraft", font=("Book Antiqua", 20))
        title.pack()
        command = Label(root, text="Sucsessfully Installed:", font=("Book Antiqua", 10))
        command.pack()
        modules = Listbox(root, fg="Green")
        progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = 'determinate') 
        subprocess.check_call([sys.executable, "-m","pip","install","pygame"], False)
        modules.insert(1, "Pygame")
        progress["value"]=14
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pyopengl"], False)
        modules.insert(2, "Pyopengl")
        progress["value"]=8
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","numpy"], False)
        modules.insert(3, "Numpy")
        progress["value"]=38
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pyautogui"], False)
        modules.insert(4, "Pyautogui")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","matplotlib"], False)
        modules.insert(5, "Matplotlib")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","kiwisolver"], False)
        modules.insert(6, "Kiwisolver")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","six"], False)
        modules.insert(7, "Six")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","cycler"], False)
        modules.insert(8, "Cycler")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pyparsing"], False)
        modules.insert(9, "Pyparsing")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","python-dateutil"], False)
        modules.insert(10, "Python-dateutil")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","mouseinfo"], False)
        modules.insert(11, "Mouseinfo")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pygetwindow"], False)
        modules.insert(12, "Pygetwindow")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pymsgbox"], False)
        modules.insert(13, "Pymsgbox")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pyperclip"], False)
        modules.insert(14, "Pyperclip")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pyrect"], False)
        modules.insert(15, "Pyrect")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pytweening"], False)
        modules.insert(16, "Pytweening")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        subprocess.check_call([sys.executable, "-m","pip","install","pyscreeze"], False)
        modules.insert(17, "Pyscreeze")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)
        command = Label(root, text="Installation Complete!", font=("Book Antiqua", 10))
        command.pack()
        time.sleep(3)
        root.destroy()
        root.mainloop()

def update():
    if messagebox.askyesno("Caution!", "Are you sure you want to do that?") == True:
        root = Tk()
        root.title("Pycaft Setup Wizard | Updating Pycraft")
        root.minsize(500,500)
        
        title = Label(root, text="Pycraft", font=("Book Antiqua", 20))
        title.pack()
        command = Label(root, text="Sucsessfully Updated:", font=("Book Antiqua", 10))
        command.pack()
        
        modules = Listbox(root, fg="Red")
        
        progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = 'determinate') 
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pygame"], False)
            modules.insert(1, "Pygame")
            progress["value"]=14
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except Exception as error:
            print(error)
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyopengl"], False)
            modules.insert(2, "Pyopengl")
            progress["value"]=8
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","numpy"], False)
            modules.insert(3, "Numpy")
            progress["value"]=38
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyautogui"], False)
            modules.insert(4, "Pyutogui")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","matplotlib"], False)
            modules.insert(5, "Matplotlib")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","kiwisolver"], False)
            modules.insert(6, "Kiwisolver")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","six"], False)
            modules.insert(7, "Six")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","cycler"], False)
            modules.insert(8, "Cycler")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyparsing"], False)
            modules.insert(9, "Pyparsing")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","python-dateutil"], False)
            modules.insert(10, "Python-dateutil")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","mouseinfo"], False)
            modules.insert(11, "Mouseinfo")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pygetwindow"], False)
            modules.insert(12, "Pygetwindow")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pymsgbox"], False)
            modules.insert(13, "Pymsgbox")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyperclip"], False)
            modules.insert(14, "Pyperclip")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyrect"], False)
            modules.insert(15, "Pyrect")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pytweening"], False)
            modules.insert(16, "Pytweening")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyscreeze"], False)
            modules.insert(17, "Pyscreeze")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()

        subprocess.check_call([sys.executable, "-m","pip","install","pygame"], False)
        modules.insert(1, "Pygame")
        progress["value"]=14
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pyopengl"], False)
        modules.insert(2, "Pyopengl")
        progress["value"]=8
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","numpy"], False)
        modules.insert(3, "Numpy")
        progress["value"]=38
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pyautogui"], False)
        modules.insert(4, "Pyautogui")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","matplotlib"], False)
        modules.insert(5, "Matplotlib")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","kiwisolver"], False)
        modules.insert(6, "Kiwisolver")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","six"], False)
        modules.insert(7, "Six")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","cycler"], False)
        modules.insert(8, "Cycler")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pyparsing"], False)
        modules.insert(9, "Pyparsing")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","python-dateutil"], False)
        modules.insert(10, "Python-dateutil")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","mouseinfo"], False)
        modules.insert(11, "Mouseinfo")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pygetwindow"], False)
        modules.insert(12, "Pygetwindow")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pymsgbox"], False)
        modules.insert(13, "Pymsgbox")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pyperclip"], False)
        modules.insert(14, "Pyperclip")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pyrect"], False)
        modules.insert(15, "Pyrect")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pytweening"], False)
        modules.insert(16, "Pytweening")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        subprocess.check_call([sys.executable, "-m","pip","install","pyscreeze"], False)
        modules.insert(17, "Pyscreeze")
        progress["value"]=0.2
        root.update_idletasks()
        progress.pack()
        modules.pack()
        root.after(1)

        command = Label(root, text="Installation Complete!", font=("Book Antiqua", 10))
        command.pack()

        time.sleep(3)
        root.destroy()
        command = Label(root, text="Sucsessfully updated Pycraft", font=("Book Antiqua", 10))
        command.pack()

def uninstall():
    if messagebox.askyesno("Caution!", "Are you sure you want to do that?") == True:
        root = Tk()
        root.title("Pycaft Setup Wizard | Uninstalling Pycraft")
        root.minsize(500,500)
        title = Label(root, text="Pycraft", font=("Book Antiqua", 20))
        title.pack()
        command = Label(root, text="Sucsessfully uninstalled:", font=("Book Antiqua", 10))
        command.pack()
        modules = Listbox(root, fg="Red")
        progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = 'determinate') 
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pygame"], False)
            modules.insert(1, "Pygame")
            progress["value"]=14
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except Exception as error:
            print(error)
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyopengl"], False)
            modules.insert(2, "Pyopengl")
            progress["value"]=8
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","numpy"], False)
            modules.insert(3, "Numpy")
            progress["value"]=38
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyautogui"], False)
            modules.insert(4, "Pyutogui")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","matplotlib"], False)
            modules.insert(5, "Matplotlib")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","kiwisolver"], False)
            modules.insert(6, "Kiwisolver")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","six"], False)
            modules.insert(7, "Six")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","cycler"], False)
            modules.insert(8, "Cycler")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyparsing"], False)
            modules.insert(9, "Pyparsing")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","python-dateutil"], False)
            modules.insert(10, "Python-dateutil")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","mouseinfo"], False)
            modules.insert(11, "Mouseinfo")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pygetwindow"], False)
            modules.insert(12, "Pygetwindow")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pymsgbox"], False)
            modules.insert(13, "Pymsgbox")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyperclip"], False)
            modules.insert(14, "Pyperclip")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyrect"], False)
            modules.insert(15, "Pyrect")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pytweening"], False)
            modules.insert(16, "Pytweening")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        try:
            subprocess.check_call([sys.executable, "-m","pip","uninstall","pyscreeze"], False)
            modules.insert(17, "Pyscreeze")
            progress["value"]=0.2
            root.update_idletasks()
            progress.pack()
            modules.pack()
            root.after(1)
        except:
            print()
        command = Label(root, text="Sucsessfully Uninstalled", font=("Book Antiqua", 10))
        command.pack()
        time.sleep(3)
        root.destroy()
        root.mainloop()
install_button = Button(leftframe, text="Install", command=install)
install_button.pack(side=LEFT, padx=1)
update_button = Button(leftframe, text="Uninstall", command=uninstall)
update_button.pack(side=RIGHT)
uninstall_button = Button(leftframe, text="Update", command=update)
uninstall_button.pack(side=RIGHT, padx=200)
try:
    import pygame, numpy, PIL, timeit, time, random, tkinter, random, os, sys, pip, subprocess, time, OpenGL.GL, OpenGL.GLU, OpenGL.GLUT, pyautogui, psutil
    pygame.init()
except:
    print()
else:
    play_button = Button(frame, text="Play", command=play)
    play_button.pack()
root.mainloop()