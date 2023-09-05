def Module_Setup_Check ():
    NoModules = []
    Found = []
    temp = 0
    try:
        import pygame
    except ModuleNotFoundError:
        NoModules.append("Pygame")
    finally:
        Found.append("Pygame")
        try:
            import OpenGL
        except ModuleNotFoundError:
            NoModules.append("PyOpenGL")
        finally:
            Found.append("PyOpenGL")
            try:
                import numpy
            except ModuleNotFoundError:
                NoModules.append("Numpy")
            finally:
                Found.append("Numpy")
                try:
                    import tkinter
                except ModuleNotFoundError:
                    NoModules.append("Tkinter")
                finally:
                    Found.append("Tkinter")
                    try:
                        import pyautogui
                    except ModuleNotFoundError:
                        NoModules.append("PyAutoGUI")
                    finally:
                        Found.append("PyAutoGUI")
                        try:
                            import time
                        except ModuleNotFoundError:
                            NoModules.append("Time")
                        finally:
                            Found.append("Time")
                            try:
                                import random
                            except ModuleNotFoundError:
                                NoModules.append("Random")
                            finally:
                                Found.append("Random")
                                try:
                                    import sys
                                except ModuleNotFoundError:
                                    NoModules.append("Sys")
                                finally:
                                    Found.append("Sys")
                                    try:
                                        import matplotlib
                                    except ModuleNotFoundError:
                                        NoModules.append("Matplotlib")
                                    finally:
                                        Found.append("Matplotlib")
                                        try:
                                            import kiwisolver
                                        except ModuleNotFoundError:
                                            NoModules.append("Kiwisolver")
                                        finally:
                                            Found.append("Kiwisolver")
                                            try:
                                                import six
                                            except ModuleNotFoundError:
                                                NoModules.append("Six")
                                            finally:
                                                Found.append("Six")
                                                try:
                                                    import cycler
                                                except ModuleNotFoundError:
                                                    NoModules.append("Cycler")
                                                finally:
                                                    Found.append("Cycler")
                                                    try:
                                                        import pyparsing
                                                    except ModuleNotFoundError:
                                                        NoModules.append("Pyparsing")
                                                    finally:
                                                        Found.append("Pyparsing")
                                                        try:
                                                            import dateutil
                                                        except ModuleNotFoundError:
                                                            NoModules.append("Dateutil")
                                                        finally:
                                                            Found.append("Dateutil")
                                                            try:
                                                                import PIL
                                                            except ModuleNotFoundError:
                                                                NoModules.append("PIL")
                                                            finally:
                                                                Found.append("PIL")
                                                                try:
                                                                    import mouseinfo
                                                                except ModuleNotFoundError:
                                                                    NoModules.append("Mouseinfo")
                                                                finally:
                                                                    Found.append("Mouseinfo")
                                                                    try:
                                                                        import pip
                                                                    except ModuleNotFoundError:
                                                                        NoModules.append("Pip")
                                                                    finally:
                                                                        Found.append("Pip")
                                                                        try:
                                                                            import pygetwindow
                                                                        except ModuleNotFoundError:
                                                                            NoModules.append("Pygetwindow")
                                                                        finally:
                                                                            Found.append("Pygetwindow")
                                                                            try:
                                                                                import pymsgbox
                                                                            except ModuleNotFoundError:
                                                                                NoModules.append("Pymsgbox")
                                                                            finally:
                                                                                Found.append("Pymsgbox")
                                                                                try:
                                                                                    import pyperclip
                                                                                except ModuleNotFoundError:
                                                                                    NoModules.append("Pyperclip")
                                                                                finally:
                                                                                    Found.append("Pyperclip")
                                                                                    try:
                                                                                        import pyrect
                                                                                    except ModuleNotFoundError:
                                                                                        NoModules.append("Pyrect")
                                                                                    finally:
                                                                                        Found.append("Pyrect")
                                                                                        try:
                                                                                            import pyscreeze
                                                                                        except ModuleNotFoundError:
                                                                                            NoModules.append("Pyscreeze")
                                                                                        finally:
                                                                                            Found.append("Pyscreeze")
                                                                                            try:
                                                                                                import pytweening
                                                                                            except ModuleNotFoundError:
                                                                                                NoModules.append("Pytweening")
                                                                                            finally:
                                                                                                Found.append("Pytweening")
                                                                            
                                                                                                return NoModules
 
def GetFileSize(DidNotFind):
    TotalFileSize = 0
    for i in range(len(DidNotFind)):
        if DidNotFind[i] == "Pygame":
            TotalFileSize += 4.0
        elif DidNotFind[i] == 
 
 
DidNotFind = Module_Setup_Check()
GetFileSize(DidNotFind)
print(DidNotFind)

