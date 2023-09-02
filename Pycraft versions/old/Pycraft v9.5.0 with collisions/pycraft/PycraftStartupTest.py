if not __name__ == "__main__":
    print("Started <Pycraft_PycraftStartupTest>")
    class StartupTest:
        def __init__(self):
            pass

        def PycraftSelfTest(self):
            try:
                import OpenGL.GL as gl
                self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.DOUBLEBUF|self.mod_Pygame__.OPENGL|self.mod_Pygame__.HIDDEN)

                icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                self.mod_Pygame__.display.set_icon(icon)

                OpenGLversion = str(gl.glGetString(gl.GL_VERSION))[2:5]
                SDLversion = self.mod_Pygame__.get_sdl_version()[0]
                RAM = (((self.mod_Psutil__.virtual_memory().available)/1000)/1000) # expressed in MB

                if float(OpenGLversion) < 2.8:
                    root = self.mod_Tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror("Invalid OpenGL version", f"OpenGL version: {OpenGLversion} is not supported; try a version greater than 2.7")
                    quit()
                if SDLversion < 2:
                    root = self.mod_Tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror("Invalid SDL version", f"SDL version: {SDLversion} is not supported; try a version greater than or equal to 2")
                    quit()
                if RAM < 100:
                    root = self.mod_Tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror("Minimum system requirements not met", f"Your system does not meet the minimum 100mb free memory specification needed to play this game")
                    quit()
                if RAM < 200:
                    root = self.mod_Tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showwarning("Recommended system requirements not met", f"Your system's free memory does not meet the requirement recommended to play this game (200mb), you are still able to, however your experience may not be satisfactory")
                    from PIL import Image, ImageTk, ImageGrab
                    import OpenGL.GL
                    
                if self.mod_Sys__.platform == "win32" or self.mod_Sys__.platform == "win64":
                    self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"

                self.mod_Pygame__.display.quit()
                self.mod_Pygame__.display.init()

                self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)

                current_time = self.mod_Datetime__.datetime.now()
                currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
                if not currentDate == self.lastRun or self.crash == True:
                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                    yScaleFact = realHeight/720
                    xScaleFact = realWidth/1280
                    self.Display.fill(self.BackgroundCol)
                    TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                    Title = TitleFont.render("Pycraft", True, self.FontCol)
                    TitleWidth = Title.get_width()
                    self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                    defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] 
                    self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    data = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Error_Message.png"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Error_Resources\\Icon.jpg"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\Folder_Resources\\FolderIcon.ico"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).convert()
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2)
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONlight.jpg")).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    data = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, f"Resources\\General_Resources\\selectorICONdark.jpg")).convert()
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 1)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.wav")))
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 2)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
                    data = self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 3)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                else:
                    self.Display.fill(self.BackgroundCol)
                    TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                    Title = TitleFont.render("Pycraft", True, self.FontCol)
                    TitleWidth = Title.get_width()
                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                    self.Display.blit(Title, ((realWidth-TitleWidth)/2, 0))
                    self.mod_CaptionUtils__.GenerateCaptions.GetLoadingCaption(self, 0)
                    
                    yScaleFact = realHeight/720
                    xScaleFact = realWidth/1280
                    defLargeOctagon = [(205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact)] 
                    self.mod_Pygame__.draw.polygon(self.Display, self.ShapeCol, defLargeOctagon, width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 142*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (51*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (205*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (51*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (205*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 666*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 512*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (51*xScaleFact, 295*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2) 
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (422*xScaleFact, 666*yScaleFact), (575*xScaleFact, 295*yScaleFact), width=2)
                    self.mod_Pygame__.draw.line(self.Display, self.ShapeCol, (575*xScaleFact, 512*yScaleFact), (422*xScaleFact, 142*yScaleFact), width=2)
                    self.mod_Pygame__.display.update()
            except Exception as Message:
                return Message
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()