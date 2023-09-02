if not __name__ == "__main__":
    print("Started <Pycraft_Achievements>")
    class GenerateAchievements:
        def __init__(self):
            pass

        def Achievements(self):
            try:
                self.Display.fill(self.BackgroundCol) 
                self.mod_Pygame__.display.flip()
                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
                InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)

                TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = TitleFont.get_width()

                AchievementsFont = InfoTitleFont.render("Achievements", self.aa, self.SecondFontCol)
                tempFPS = self.FPS

                self.StartAnimation = True
                self.RunTimer = 0

                GoTo = None

                while True:
                    StartTime = self.mod_Time__.perf_counter()
                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()

                    if realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                    self.eFPS = self.clock.get_fps()
                    self.aFPS += self.eFPS 
                    self.Iteration += 1
                    
                    tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)

                    for event in self.mod_Pygame__.event.get(): 
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): 
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            self.StartAnimation = True
                            self.RunTimer = 0
                            GoTo = "Home"
                        elif event.type == self.mod_Pygame__.KEYDOWN: 
                            if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: 
                                self.Devmode += 1 
                            if event.key == self.mod_Pygame__.K_q:
                                self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)
                            if event.key == self.mod_Pygame__.K_F11:
                                self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)
                            if event.key == self.mod_Pygame__.K_x: 
                                self.Devmode = 1 

                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Achievements")
                            
                    self.Display.fill(self.BackgroundCol)

                    cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)
                    self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)
                    self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                    self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))

                    Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)
                    if not Message == None:
                        return Message

                    if GoTo == None:
                        self.mod_DisplayUtils__.DisplayAnimations.FadeIn(self)
                    else:
                        self.mod_DisplayUtils__.DisplayAnimations.FadeOut(self, GoTo)

                    if self.StartAnimation == False and (not GoTo == None):
                        return None

                    self.mod_Pygame__.display.flip() 
                    self.clock.tick(tempFPS)
                    self.RunTimer += self.mod_Time__.perf_counter()-StartTime
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