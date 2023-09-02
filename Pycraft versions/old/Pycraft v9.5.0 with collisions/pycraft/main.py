print("Started <Pycraft_main>")
class Startup:
    def __init__(Class_Startup_variables):
        try:
            import tkinter as tk
            Class_Startup_variables.mod_Tkinter__tk = tk # [Class_Startup_variables] mod (module) (module name) (subsection of module) (name references)
            import tkinter.ttk  # Class _ <class_name> _ variables
            Class_Startup_variables.mod_Tkinter_ttk_ = tkinter.ttk
            from tkinter import messagebox
            Class_Startup_variables.mod_Tkinter_messagebox_ = messagebox
            from PIL import Image, ImageFilter, ImageGrab, ImageTk
            Class_Startup_variables.mod_PIL_Image_ = Image
            Class_Startup_variables.mod_PIL_ImageFilter_ = ImageFilter
            Class_Startup_variables.mod_PIL_ImageTk_ = ImageTk
            Class_Startup_variables.mod_PIL_ImageGrab_ = ImageGrab
            import pygame
            Class_Startup_variables.mod_Pygame__ = pygame
            import numpy
            Class_Startup_variables.mod_Numpy__ = numpy
            import os
            Class_Startup_variables.mod_OS__ = os
            import sys
            Class_Startup_variables.mod_Sys__ = sys
            import random
            Class_Startup_variables.mod_Random__ = random
            import time
            Class_Startup_variables.mod_Time__ = time
            import pygame.locals
            Class_Startup_variables.mod_Pygame_locals_ = pygame.locals
            import OpenGL
            Class_Startup_variables.mod_OpenGL__ = OpenGL
            import OpenGL.GL
            Class_Startup_variables.mod_OpenGL_GL_ = OpenGL.GL
            import OpenGL.GLU
            Class_Startup_variables.mod_OpenGL_GLU_ = OpenGL.GLU
            import OpenGL.GLUT
            Class_Startup_variables.mod_OpenGL_GLUT_ = OpenGL.GLUT
            import moderngl
            Class_Startup_variables.mod_ModernGL__ = moderngl
            import moderngl_window
            Class_Startup_variables.mod_ModernGL_window_ = moderngl_window
            import pyautogui
            Class_Startup_variables.mod_Pyautogui__ = pyautogui
            import psutil
            Class_Startup_variables.mod_Psutil__ = psutil
            import timeit
            Class_Startup_variables.mod_Timeit__ = timeit
            import subprocess
            Class_Startup_variables.mod_Subprocess__ = subprocess
            import traceback
            Class_Startup_variables.mod_Traceback__ = traceback
            import datetime
            Class_Startup_variables.mod_Datetime__ = datetime
            import ctypes
            Class_Startup_variables.mod_Ctypes__ = ctypes
            import json
            Class_Startup_variables.mod_JSON__ = json
            import threading
            Class_Startup_variables.mod_Threading__ = threading
            import cpuinfo
            Class_Startup_variables.mod_CPUinfo__ = cpuinfo
            import array
            Class_Startup_variables.mod_Array__ = array
            import GPUtil
            Class_Startup_variables.mod_GPUtil__ = GPUtil
            from tabulate import tabulate
            Class_Startup_variables.mod_Tabulate_tabulate_ = tabulate
            from pyrr import Matrix44
            Class_Startup_variables.mod_Pyrr_Matrix44_ = Matrix44
            Class_Startup_variables.mod_urllib_request_ = None
            
            moderngl.create_standalone_context()
            
            os.environ['SDL_VIDEO_CENTERED'] = '1'

            Class_Startup_variables.mod_Pygame__.init()
            
            import PycraftStartupTest
            Class_Startup_variables.mod_PycraftStartupTest__ = PycraftStartupTest
            import StartupAnimation
            Class_Startup_variables.mod_StartupAnimation__ = StartupAnimation
            import DisplayUtils
            Class_Startup_variables.mod_DisplayUtils__ = DisplayUtils
            import GetSavedData
            Class_Startup_variables.mod_GetSavedData__ = GetSavedData
            import ThemeUtils
            Class_Startup_variables.mod_ThemeUtils__ = ThemeUtils
            import HomeScreen
            Class_Startup_variables.mod_HomeScreen__ = HomeScreen
            import SoundUtils
            Class_Startup_variables.mod_SoundUtils__ = SoundUtils
            import DrawingUtils
            Class_Startup_variables.mod_DrawingUtils__ = DrawingUtils
            import CaptionUtils
            Class_Startup_variables.mod_CaptionUtils__ = CaptionUtils
            import Credits
            Class_Startup_variables.mod_Credits__ = Credits
            import TkinterUtils
            Class_Startup_variables.mod_TkinterUtils__ = TkinterUtils
            import Achievements
            Class_Startup_variables.mod_Achievements__ = Achievements
            import CharacterDesigner
            Class_Startup_variables.mod_CharacterDesigner__ = CharacterDesigner
            import Settings
            Class_Startup_variables.mod_Settings__ = Settings
            import Benchmark
            Class_Startup_variables.mod_Benchmark__ = Benchmark
            import ExBenchmark
            Class_Startup_variables.mod_ExBenchmark__ = ExBenchmark
            import OGLbenchmark
            Class_Startup_variables.mod_OGLbenchmark__ = OGLbenchmark
            import GLWindowUtils
            Class_Startup_variables.mod_Base__ = GLWindowUtils
            import ShareDataUtil
            Class_Startup_variables.mod_Globals__ = ShareDataUtil
            import TextUtils
            Class_Startup_variables.mod_TextUtils__ = TextUtils
            import Inventory
            Class_Startup_variables.mod_Inventory__ = Inventory
            import ImageUtils
            Class_Startup_variables.mod_ImageUtils__ = ImageUtils
            import MapGUI
            Class_Startup_variables.mod_MapGUI__ = MapGUI
            import ThreadingUtil
            Class_Startup_variables.mod_ThreadingUtil__ = ThreadingUtil
            import IntegratedInstaller
            Class_Startup_variables.mod_IntegInstaller__ = IntegratedInstaller

            Class_Startup_variables.aa = True
            Class_Startup_variables.AccentCol = (237, 125, 49)
            Class_Startup_variables.aFPS = 0
            Class_Startup_variables.BackgroundCol = [30, 30, 30]
            Class_Startup_variables.base_folder = os.path.dirname(__file__)
            Class_Startup_variables.cameraANGspeed = 3.5
            Class_Startup_variables.clock = pygame.time.Clock()
            Class_Startup_variables.Collisions = [False, 0]
            Class_Startup_variables.CompletePercent = 0
            Class_Startup_variables.ctx = 0
            Class_Startup_variables.Load_Progress = 0
            Class_Startup_variables.ConnectionPermission = None
            Class_Startup_variables.ConnectionStatus = False
            Class_Startup_variables.crash = False
            Class_Startup_variables.CurrentlyPlaying = None

            Class_Startup_variables.Data_aFPS_Min = 60
            Class_Startup_variables.Data_aFPS = []
            Class_Startup_variables.Data_aFPS_Max = 1

            Class_Startup_variables.Data_CPUUsE_Min = 60
            Class_Startup_variables.Data_CPUUsE = []
            Class_Startup_variables.Data_CPUUsE_Max = 1

            Class_Startup_variables.Data_eFPS_Min = 60
            Class_Startup_variables.Data_eFPS = []
            Class_Startup_variables.Data_eFPS_Max = 1

            Class_Startup_variables.Data_MemUsE_Min = 60
            Class_Startup_variables.Data_MemUsE = []
            Class_Startup_variables.Data_MemUsE_Max = 1

            Class_Startup_variables.Data_CPUUsE_Min = 60
            Class_Startup_variables.Data_CPUUsE = []
            Class_Startup_variables.Data_CPUUsE_Max = 1
                        
            Class_Startup_variables.Devmode = 0
            Class_Startup_variables.Display = 0
            Class_Startup_variables.eFPS = 60
            Class_Startup_variables.FanSky = True
            Class_Startup_variables.FanPart = True
            Class_Startup_variables.FontCol = (255, 255, 255)
            Class_Startup_variables.FOV = 70
            Class_Startup_variables.FromPlay = False
            Class_Startup_variables.Fullscreen = False
            Class_Startup_variables.FPS = 60
            Class_Startup_variables.FullscreenX, Class_Startup_variables.FullscreenY = pyautogui.size()
            Class_Startup_variables.GameError = None
            Class_Startup_variables.G3Dscale = 600000
            Class_Startup_variables.GetScreenGraphics = True
            Class_Startup_variables.HUD_Surface = None
            Class_Startup_variables.Iteration = 1
            Class_Startup_variables.lastRun = "29/09/2021"
            Class_Startup_variables.Load3D = True
            Class_Startup_variables.LoadMusic = True
            Class_Startup_variables.music = True
            Class_Startup_variables.musicVOL = 5
            Class_Startup_variables.Numpy_map_vertices = 0
            Class_Startup_variables.Outdated = False
            Class_Startup_variables.Progress_Line = []
            Class_Startup_variables.ProgressMessageText = "Initiating"
            Class_Startup_variables.realHeight = 720
            Class_Startup_variables.realWidth = 1280
            Class_Startup_variables.RecommendedFPS = 60
            Class_Startup_variables.RenderFOG = True
            Class_Startup_variables.RunFullStartup = False
            Class_Startup_variables.RunTimer = 0
            Class_Startup_variables.StartAnimation = True
            Class_Startup_variables.SecondFontCol = (100, 100, 100)
            Class_Startup_variables.SavedWidth = 1280
            Class_Startup_variables.SavedHeight = 720
            Class_Startup_variables.ShapeCol = (80, 80, 80)
            Class_Startup_variables.skybox_texture = 0
            Class_Startup_variables.sound = True
            Class_Startup_variables.soundVOL = 75
            Class_Startup_variables.Stop_Thread_Event = Class_Startup_variables.mod_Threading__.Event()
            Class_Startup_variables.SettingsPreference = "Medium"
            Class_Startup_variables.theme = False
            Class_Startup_variables.ThreadStatus = "Running"
            Class_Startup_variables.Timer = 0
            Class_Startup_variables.TotalNumUpdate = 0
            Class_Startup_variables.Total_move_x = 0
            Class_Startup_variables.Total_move_y = 0
            Class_Startup_variables.Total_move_z = 0
            Class_Startup_variables.TotalRotation = 0
            Class_Startup_variables.Total_Vertices = 0
            Class_Startup_variables.version = "0.9.5"
            Class_Startup_variables.vertex = 0
            Class_Startup_variables.X = 0
            Class_Startup_variables.Y = 0
            Class_Startup_variables.Z = 0

            Class_Startup_variables.Thread_StartLongThread = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartVariableChecking, args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_StartLongThread.start()
            Class_Startup_variables.Thread_StartLongThread.name = "Thread_StartLongThread"

            Class_Startup_variables.Thread_GetCPUMetrics = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartCPUlogging, args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_GetCPUMetrics.start()
            Class_Startup_variables.Thread_GetCPUMetrics.name = "Thread_GetCPUMetrics"

            Class_Startup_variables.Thread_AdaptiveMode = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.AdaptiveMode, args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_AdaptiveMode.start()
            Class_Startup_variables.Thread_AdaptiveMode.name = "Thread_AdaptiveMode"
            
            Class_Startup_variables.mod_Globals__.Share.initialize(Class_Startup_variables)
            
            import GameEngine
            Class_Startup_variables.mod_MainGameEngine__ = GameEngine
        except Exception as error:
            print(error)
            try:
                import tkinter as tk
                root = tk.Tk()
                root.withdraw()
                Class_Startup_variables.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")
                quit()
            except:
                try:
                    Class_Startup_variables.mod_Pygame__.quit()
                    sys.exit("0.0.0 -Thank you for playing")
                except:
                    quit()
                    
    def crash(ErrorREPORT):
        Class_Startup_variables.Stop_Thread_Event.set()
        if not ErrorREPORT == None:
            Class_Startup_variables.mod_Pygame__.quit()
            Class_Startup_variables.mod_Time__.sleep(1.01)
            Class_Startup_variables.mod_Pygame__.init()
            Class_Startup_variables.mod_Pygame__.mixer.stop()
            try:
                Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)
                Class_Startup_variables.mod_Pygame__.display.quit()
                Class_Startup_variables.mod_Pygame__.init()
                Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280, 720))
                icon = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                Class_Startup_variables.mod_Pygame__.display.set_icon(icon)
                Class_Startup_variables.mod_Pygame__.display.set_caption(f"Pycraft: An Error Occurred")

                MessageFont = Class_Startup_variables.mod_Pygame__.font.Font(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Fonts\\Book Antiqua.ttf")), 15)

                ErrorMessageText = MessageFont.render(str(ErrorREPORT), True, (255,0,0))
                ErrorMessageTextWidth = ErrorMessageText.get_width()
                ErrorMessageTextHeight = ErrorMessageText.get_height()
                Display = Class_Startup_variables.mod_Pygame__.display.set_mode((1280,720))

                IconImage = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Icon.jpg")))
                Class_Startup_variables.mod_Pygame__.display.set_icon(IconImage)
                image = Class_Startup_variables.mod_Pygame__.image.load(Class_Startup_variables.mod_OS__.path.join(Class_Startup_variables.base_folder,("Resources\\Error_Resources\\Error_Message.png")))
                Clock = Class_Startup_variables.mod_Pygame__.time.Clock()
                while True:
                    Display.fill((20,20,20))
                    Display.blit(image, (0,0))

                    Display.blit(ErrorMessageText, ((((1280/2)-ErrorMessageTextWidth)/2), (720-ErrorMessageTextHeight)/2))

                    for event in Class_Startup_variables.mod_Pygame__.event.get():
                        if event.type == Class_Startup_variables.mod_Pygame__.QUIT:
                            try:
                                Class_Startup_variables.Thread_StartLongThread.join()
                                Class_Startup_variables.Thread_AdaptiveMode.join()
                                Class_Startup_variables.Thread_GetCPUMetrics.join()
                                Class_Startup_variables.Thread_Get_Outdated.join()
                            except Exception as Error:
                                print(Error)
                                pass
                            
                            Class_Startup_variables.mod_Pygame__.quit()
                            Class_Startup_variables.mod_Sys__.exit(f"0.1.0- Thank you for playing")

                    Class_Startup_variables.mod_Pygame__.display.flip()
                    Clock.tick(30)
            except Exception as error:
                Class_Startup_variables.mod_Sys__.exit(f"0.2.0- {error} Thank you for playing")
        else:
            try:
                Class_Startup_variables.mod_Pygame__.quit()
            except Exception as error:
                Class_Startup_variables.mod_Sys__.exit(f"0.3.0- {error} Thank you for playing")
                quit()
            else:
                Class_Startup_variables.mod_Sys__.exit("0.4.0- Thank you for playing")
                quit()

Class_Startup_variables = Startup()
try:
    Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.ReadMainSave(Class_Startup_variables)
except Exception as FileError:
    Report = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.RepairLostSave(Class_Startup_variables)
    ErrorString = "Unable to access saved data, we have atttempted to repair the missing data, please try again", FileError
    Message = "0.0.0- " + str(ErrorString)
    Startup.crash(Message)
    
if Class_Startup_variables.ConnectionPermission == None:
    Class_Startup_variables.mod_TkinterUtils__.TkinterInfo.GetPermissions(Class_Startup_variables)
    
if Class_Startup_variables.ConnectionPermission == True:
    import urllib.request
    Class_Startup_variables.mod_urllib_request_ = urllib.request
    Class_Startup_variables.ConnectionStatus = Class_Startup_variables.mod_IntegInstaller__.CheckConnection.test(Class_Startup_variables)
    if Class_Startup_variables.ConnectionStatus == True:
        Class_Startup_variables.Thread_Get_Outdated = Class_Startup_variables.mod_Threading__.Thread(target=Class_Startup_variables.mod_IntegInstaller__.IntegInstaller.CheckVersions, args=(Class_Startup_variables,))
        Class_Startup_variables.Thread_Get_Outdated.start()
        Class_Startup_variables.Thread_Get_Outdated.name = "Thread_Get_Outdated"

Message = Class_Startup_variables.mod_PycraftStartupTest__.StartupTest.PycraftSelfTest(Class_Startup_variables)
if not Message == None:
    Message = "0.0.3- " + str(Message)
    Startup.crash(Message)

if Class_Startup_variables.theme == False:
    Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetThemeGUI(Class_Startup_variables)
    if not Message == None:
        Message = "0.0.4- " + str(Message)
        Startup.crash(Message)

Message = Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetColours(Class_Startup_variables)

if not Message == None:
    Message = "0.0.5- " + str(Message)
    Startup.crash(Message)
    
Message = Class_Startup_variables.mod_StartupAnimation__.GenerateStartupScreen.Start(Class_Startup_variables)
if not Message == None:
    Message = "0.0.6- " + str(Message)
    Startup.crash(Message)

Class_Startup_variables.Command = "Undefined"
while True:
    if Class_Startup_variables.Command == "saveANDexit":
        Message = Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.7- " + str(Message)
            Startup.crash(Message)
        else:
            Class_Startup_variables.Stop_Thread_Event.set()
            try:
                Class_Startup_variables.Thread_StartLongThread.join()
                Class_Startup_variables.Thread_AdaptiveMode.join()
                Class_Startup_variables.Thread_GetCPUMetrics.join()
                Class_Startup_variables.Thread_Get_Outdated.join()
            except Exception as Error:
                print(Error)
                pass
            
            Class_Startup_variables.mod_Pygame__.quit()
            Class_Startup_variables.mod_Sys__.exit("0.5.0- Thank you for playing") # 0 = Order of running, 5 = 5th occurrence down page
    elif Class_Startup_variables.Command == "Credits":
        Message = Class_Startup_variables.mod_Credits__.GenerateCredits.Credits(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.8- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Undefined"
    elif Class_Startup_variables.Command == "Achievements":
        Message = Class_Startup_variables.mod_Achievements__.GenerateAchievements.Achievements(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.9- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Undefined"
    elif Class_Startup_variables.Command == "CharacterDesigner":
        Message = Class_Startup_variables.mod_CharacterDesigner__.GenerateCharacterDesigner.CharacterDesigner(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.10- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Undefined"
    elif Class_Startup_variables.Command == "Settings":
        Message = Class_Startup_variables.mod_Settings__.GenerateSettings.settings(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.11- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Undefined"
    elif Class_Startup_variables.Command == "Benchmark":
        Message = Class_Startup_variables.mod_Benchmark__.GenerateBenchmarkMenu.Benchmark(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.12- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Undefined"
    elif Class_Startup_variables.Command == "Play":
        Message = Class_Startup_variables.mod_MainGameEngine__.CreateEngine.Play(Class_Startup_variables)
        if Message == None:
            Message = Class_Startup_variables.GameError
        if not Message == None:
            Message = "0.0.13- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.mod_Pygame__.init()
        Class_Startup_variables.FromPlay = True
        Message = Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.14- " + str(Message)
            Startup.crash(Message)
    elif Class_Startup_variables.Command == "Inventory":
        Message = Class_Startup_variables.mod_Inventory__.GenerateInventory.Inventory(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.15- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Play"
    elif Class_Startup_variables.Command == "MapGUI":
        Message = Class_Startup_variables.mod_MapGUI__.GenerateMapGUI.MapGUI(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.16- " + str(Message)
            Startup.crash(Message)
        Class_Startup_variables.Command = "Play"
    else:
        Message, Class_Startup_variables.Command = Class_Startup_variables.mod_HomeScreen__.GenerateHomeScreen.Home_Screen(Class_Startup_variables)
        if not Message == None:
            Message = "0.0.17- " + str(Message)
            Startup.crash(Message)