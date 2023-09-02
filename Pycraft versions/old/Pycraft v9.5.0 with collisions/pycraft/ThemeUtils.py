if not __name__ == "__main__":
    print("Started <Pycraft_ThemeUtils>")
    class DetermineThemeColours:
        def __init__(self):
            pass

        def GetColours(self):
            try:
                self.themeArray = [[(255, 255, 255), [30, 30, 30], (80, 80, 80), (237, 125, 49), (255, 255, 255)], [(0, 0, 0), [255, 255, 255], (80, 80, 80), (237, 125, 49), (100, 100, 100)]]
                if self.theme == "dark":
                    self.FontCol = self.themeArray[0][0]
                    self.BackgroundCol = self.themeArray[0][1]
                    self.ShapeCol = self.themeArray[0][2]
                    self.AccentCol = self.themeArray[0][3]
                    self.SecondFontCol = self.themeArray[0][4]
                elif self.theme == "light":
                    self.FontCol = self.themeArray[1][0]
                    self.BackgroundCol = self.themeArray[1][1]
                    self.ShapeCol = self.themeArray[1][2]
                    self.AccentCol = self.themeArray[1][3]
                    self.SecondFontCol = self.themeArray[1][4]
            except Exception as Message:
                return Message


        def GetThemeGUI(self):
            try:
                clock = self.mod_Pygame__.time.Clock()
                TitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                Title = TitleFont.render("Pycraft", True, (255, 255, 255))
                MiddleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)
                DarkModeFont = MiddleFont.render("Dark", True, (255, 255, 255))
                LightModeFont = MiddleFont.render("Light", True, (255, 255, 255))
                mousebuttondown = False
                while self.theme == False:
                    self.Display.fill([30, 30, 30])
                    mX, mY = self.mod_Pygame__.mouse.get_pos()
                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT:
                            self.Stop_Thread_Event.set()

                            self.Thread_StartLongThread.join()
                            self.Thread_AdaptiveMode.join()
                            self.Thread_StartLongThread.join()
                            
                            self.mod_Pygame__.quit()
                            self.mod_Sys__.exit("Thanks for playing")
                        if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:
                            mousebuttondown = True
                        if event.type == self.mod_Pygame__.MOUSEBUTTONUP:
                            mousebuttondown = False
                        
                    self.Display.blit(Title, (540, 0))
                    self.Display.blit(DarkModeFont, (320, 360))
                    self.Display.blit(LightModeFont, (890, 360))
                    DarkRect = self.mod_Pygame__.Rect(260, 300, 200, 160)
                    self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), DarkRect, 3)
                    LightRect = self.mod_Pygame__.Rect(820, 300, 200, 160)
                    self.mod_Pygame__.draw.rect(self.Display, (80, 80, 80), LightRect, 3)
                    if mX >= 260 and mX <= 460 and mY >= 300 and mY <= 460:
                        if mousebuttondown == True:
                            self.theme = "dark"
                            self.base_folder = self.mod_OS__.path.dirname(__file__)
                            self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))
                            
                            self.mod_Pygame__.mixer.music.set_volume(50)
                            
                            self.mod_Pygame__.mixer.music.play()
                            mousebuttondown = False
                    elif mX >= 820 and mX <= 980 and mY >= 300 and mY <= 460:
                        if mousebuttondown == True:
                            self.theme = "light"
                            self.base_folder = self.mod_OS__.path.dirname(__file__)
                            self.mod_Pygame__.mixer.music.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.wav")))
                            
                            self.mod_Pygame__.mixer.music.set_volume(50)
                            
                            self.mod_Pygame__.mixer.music.play()
                            mousebuttondown = False
                    self.mod_Pygame__.display.update()
                    clock.tick(60)
            except Exception as Message:
                Message = str(Message)+" in <Pycraft_ThemeUtils>"
                return Message

            return None
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()