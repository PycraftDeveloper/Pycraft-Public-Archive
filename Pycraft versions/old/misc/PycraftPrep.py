import os, shutil, send2trash, subprocess, sys

print("Initializing")

base_folder = os.path.dirname(__file__)

source_folder = r"D:\MyFiles\Pycraft"
destination_folder = r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft"

print("Clearing resources folder in preparation for backup")

send2trash.send2trash(destination_folder)

print("Backing up Pycraft")

shutil.copytree(source_folder, destination_folder)

print("Removing unnessasary files")

try:
    send2trash.send2trash(r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft\test.py")
    send2trash.send2trash(r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft\test2.py")
    send2trash.send2trash(r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft\Damage calc.py")
    send2trash.send2trash(r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft\PycraftInstaller3.py")
    send2trash.send2trash(r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft\PycraftInstaller2.py")
    send2trash.send2trash(r"C:\Users\pamj0\Documents\Pycraft_AutoPrep\Resources\Pycraft\desktop.ini")
except:
    print("No file found here")

print("Coverting Pycraft.py to pep8 regs")

if os.path.isfile("C:/Users/pamj0/Documents/Pycraft_AutoPrep/Resources/Pycraft/Pycraft.py"):
    print("Sucsessfully checked command")

os.system('cmd /c "autopep8 --in-place --aggressive --aggressive C:/Users/pamj0/Documents/Pycraft_AutoPrep/Resources/Pycraft/Pycraft.py"')

print("Complete!")

print("Coverting PycraftRunUtl.py to pep8 regs")

if os.path.isfile("C:/Users/pamj0/Documents/Pycraft_AutoPrep/Resources/Pycraft/PycraftRunUtl.py"):
    print("Sucsessfully checked command")

os.system('cmd /c "autopep8 --in-place --aggressive --aggressive C:/Users/pamj0/Documents/Pycraft_AutoPrep/Resources/Pycraft/PycraftRunUtl.py"')

print("Complete")

print("Coverting PycraftInstaller.py to pep8 regs")

if os.path.isfile("C:/Users/pamj0/Documents/Pycraft_AutoPrep/Resources/Pycraft/PycraftInstaller.py"):
    print("Sucsessfully checked command")

os.system('cmd /c "autopep8 --in-place --aggressive --aggressive C:/Users/pamj0/Documents/Pycraft_AutoPrep/Resources/Pycraft/PycraftInstaller.py"')

print("Complete")

print("Conversion to pep8 structure complete, please test project now to make sure everything still works")

test = str(input("Enter 1 if test worked to continue: "))

if not test == "1":
    quit()

print("Opening py to exe converter")

os.system('cmd /c "autopytoexe"')




