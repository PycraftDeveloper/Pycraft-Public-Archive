if not __name__ == "__main__":
    print("Started <Pycraft_Credits>")
    class GenerateCredits:
        def __init__(self):
            pass

        def Credits(self):
            try:
                self.Display.fill(self.BackgroundCol)
                self.mod_Pygame__.display.flip() 
                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")
                VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                LargeCreditsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
                InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = TitleFont.get_width()
                TitleHeight = TitleFont.get_height()
                CreditsFont = InfoTitleFont.render("Credits", self.aa, self.SecondFontCol) 
                Credits1 = LargeCreditsFont.render(f"Pycraft: v{self.version}", self.aa, self.FontCol)
                Credits1Width = Credits1.get_width()
                Credits2 = LargeCreditsFont.render("Game Director: Tom Jebbo", self.aa, self.FontCol)
                Credits2Width = Credits2.get_width()
                Credits3 = LargeCreditsFont.render("Art and Music Lead: Tom Jebbo", self.aa, self.FontCol)
                Credits3Width = Credits3.get_width()
                Credits4 = LargeCreditsFont.render("Other Music Credits:", self.aa, self.FontCol)
                Credits4Width = Credits4.get_width()
                Credits5 = LargeCreditsFont.render("Freesound: - Erokia's 'ambient wave compilation' @ freesound.org/s/473545", self.aa, self.FontCol)
                Credits5Width = Credits5.get_width()
                Credits6 = LargeCreditsFont.render("Freesound: - Soundholder's 'ambient meadow near forest' @ freesound.org/s/425368", self.aa, self.FontCol)
                Credits6Width = Credits6.get_width()
                Credits7 = LargeCreditsFont.render("Freesound: - monte32's 'Footsteps_6_Dirt_shoe' @ freesound.org/people/monte32/sounds/353799", self.aa, self.FontCol)
                Credits7Width = Credits7.get_width()
                Credits8 = LargeCreditsFont.render("With thanks to the developers of:", self.aa, self.FontCol)
                Credits8Width = Credits8.get_width()
                Credits9 = LargeCreditsFont.render("PSutil", self.aa, self.FontCol)
                Credits9Width = Credits9.get_width()
                Credits10 = LargeCreditsFont.render("Python", self.aa, self.FontCol)
                Credits10Width = Credits10.get_width()
                Credits11 = LargeCreditsFont.render("Pygame", self.aa, self.FontCol)
                Credits11Width = Credits11.get_width()
                Credits12 = LargeCreditsFont.render("Numpy", self.aa, self.FontCol)
                Credits12Width = Credits12.get_width()
                Credits13 = LargeCreditsFont.render("Nuitka", self.aa, self.FontCol)
                Credits13Width = Credits13.get_width()
                Credits14 = LargeCreditsFont.render("CPUinfo", self.aa, self.FontCol)
                Credits14Width = Credits14.get_width()
                Credits15 = LargeCreditsFont.render("PyInstaller", self.aa, self.FontCol)
                Credits15Width = Credits15.get_width()
                Credits16 = LargeCreditsFont.render("PyAutoGUI", self.aa, self.FontCol)
                Credits16Width = Credits16.get_width()
                Credits17 = LargeCreditsFont.render("PyWaveFront", self.aa, self.FontCol)
                Credits17Width = Credits17.get_width()
                Credits18 = LargeCreditsFont.render("Microsoft's Visual Studio Code", self.aa, self.FontCol)
                Credits18Width = Credits18.get_width()
                Credits19 = LargeCreditsFont.render("PIL (Pillow/Python Imaging Library)", self.aa, self.FontCol)
                Credits19Width = Credits19.get_width()
                Credits20 = LargeCreditsFont.render("PyOpenGL (and PyOpenGL-accelerate)", self.aa, self.FontCol)
                Credits20Width = Credits20.get_width()
                Credits21 = LargeCreditsFont.render("For more in depth accreditation please check the GitHub Page @ github.com/PycraftDeveloper/Pycraft", self.aa, self.FontCol)
                Credits21Width = Credits21.get_width()
                Credits22 = LargeCreditsFont.render("With thanks to:", self.aa, self.FontCol)
                Credits22Width = Credits22.get_width()
                Credits23 = LargeCreditsFont.render("All my wonderful followers on Twitter, and you for installing this game, that's massively appreciated!", self.aa, self.FontCol)
                Credits23Width = Credits23.get_width()
                Credits24 = LargeCreditsFont.render("For full change-log please visit my aforementioned GitHub profile", self.aa, self.FontCol)
                Credits24Width = Credits24.get_width()
                Credits25 = LargeCreditsFont.render("Disclaimer:", self.aa, self.FontCol)
                Credits25Width = Credits25.get_width()
                Credits26 = VersionFont.render("The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your", self.aa, self.AccentCol)
                Credits26Width = Credits26.get_width()
                Credits27 = VersionFont.render("friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve", self.aa, self.AccentCol)
                Credits27Width = Credits27.get_width()
                Credits28 = VersionFont.render("my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo", self.aa, self.AccentCol)
                Credits28Width = Credits28.get_width()
                Credits29 = VersionFont.render("DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO", self.aa, self.AccentCol)
                Credits29Width = Credits29.get_width()
                Credits30 = VersionFont.render("YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM", self.aa, self.AccentCol)
                Credits30Width = Credits30.get_width()
                Credits31 = VersionFont.render("RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE", self.aa, self.AccentCol)
                Credits31Width = Credits31.get_width()
                Credits32 = VersionFont.render("COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A", self.aa, self.AccentCol)
                Credits32Width = Credits32.get_width()
                Credits33 = VersionFont.render("NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.", self.aa, self.AccentCol)
                Credits33Width = Credits33.get_width()
                Credits34 = VersionFont.render("Thank You!", self.aa, self.FontCol)
                Credits34Width = Credits34.get_width()
                Credits34Height = Credits34.get_height()

                realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                VisualYdisplacement = realHeight
                IntroYDisplacement = (realHeight-TitleHeight)/2
                timer = 5
                tempFPS = self.FPS

                EndClock = 0
                FullscreenX, FullscreenY = self.mod_Pyautogui__.size()

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

                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Credits")
                    self.Display.fill(self.BackgroundCol)
                    self.Display.blit(Credits1, ((realWidth-Credits1Width)/2, 0+VisualYdisplacement))
                    self.Display.blit(Credits2, ((realWidth-Credits2Width)/2, 115+VisualYdisplacement))
                    self.Display.blit(Credits3, ((realWidth-Credits3Width)/2, (115*2)+VisualYdisplacement))
                    self.Display.blit(Credits4, ((realWidth-Credits4Width)/2, (115*3)+VisualYdisplacement))
                    self.Display.blit(Credits5, ((realWidth-Credits5Width)/2, (115*3)+20+VisualYdisplacement))
                    self.Display.blit(Credits6, ((realWidth-Credits6Width)/2, (115*3)+40+VisualYdisplacement))
                    self.Display.blit(Credits7, ((realWidth-Credits7Width)/2, (115*3)+60+VisualYdisplacement))
                    self.Display.blit(Credits8, ((realWidth-Credits8Width)/2, 540+VisualYdisplacement))
                    self.Display.blit(Credits9, ((realWidth-Credits9Width)/2, 540+20+VisualYdisplacement))
                    self.Display.blit(Credits10, ((realWidth-Credits10Width)/2, 540+40+VisualYdisplacement))
                    self.Display.blit(Credits11, ((realWidth-Credits11Width)/2, 540+60+VisualYdisplacement))
                    self.Display.blit(Credits12, ((realWidth-Credits12Width)/2, 540+80+VisualYdisplacement))
                    self.Display.blit(Credits13, ((realWidth-Credits13Width)/2, 540+100+VisualYdisplacement))
                    self.Display.blit(Credits14, ((realWidth-Credits14Width)/2, 540+120+VisualYdisplacement))
                    self.Display.blit(Credits15, ((realWidth-Credits15Width)/2, 540+140+VisualYdisplacement))
                    self.Display.blit(Credits16, ((realWidth-Credits16Width)/2, 540+160+VisualYdisplacement))
                    self.Display.blit(Credits17, ((realWidth-Credits17Width)/2, 540+180+VisualYdisplacement))
                    self.Display.blit(Credits18, ((realWidth-Credits18Width)/2, 540+200+VisualYdisplacement))
                    self.Display.blit(Credits19, ((realWidth-Credits19Width)/2, 540+220+VisualYdisplacement))
                    self.Display.blit(Credits20, ((realWidth-Credits20Width)/2, 540+240+VisualYdisplacement))
                    self.Display.blit(Credits21, ((realWidth-Credits21Width)/2, 540+260+VisualYdisplacement))
                    self.Display.blit(Credits22, ((realWidth-Credits22Width)/2, 915+VisualYdisplacement))
                    self.Display.blit(Credits23, ((realWidth-Credits23Width)/2, 935+VisualYdisplacement))
                    self.Display.blit(Credits24, ((realWidth-Credits24Width)/2, 1050+VisualYdisplacement))
                    self.Display.blit(Credits25, ((realWidth-Credits25Width)/2, 1165+VisualYdisplacement))
                    self.Display.blit(Credits26, ((realWidth-Credits26Width)/2, 1167+15+VisualYdisplacement))
                    self.Display.blit(Credits27, ((realWidth-Credits27Width)/2, 1167+30+VisualYdisplacement))
                    self.Display.blit(Credits28, ((realWidth-Credits28Width)/2, 1167+45+VisualYdisplacement))
                    self.Display.blit(Credits29, ((realWidth-Credits29Width)/2, 1167+60+VisualYdisplacement))
                    self.Display.blit(Credits30, ((realWidth-Credits30Width)/2, 1167+75+VisualYdisplacement))
                    self.Display.blit(Credits31, ((realWidth-Credits31Width)/2, 1167+90+VisualYdisplacement))
                    self.Display.blit(Credits32, ((realWidth-Credits32Width)/2, 1167+105+VisualYdisplacement))
                    self.Display.blit(Credits33, ((realWidth-Credits33Width)/2, 1167+120+VisualYdisplacement))

                    if timer >= 1:
                        self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))
                        timer -= 1/(self.aFPS/self.Iteration)
                        VisualYdisplacement = realHeight
                    else:
                        if IntroYDisplacement <= 0:
                            cover_Rect = self.mod_Pygame__.Rect(0, 0, FullscreenX, 90)
                            self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)
                            self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                            self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50))
                            if int(1402+VisualYdisplacement) <= int(realHeight/2):
                                self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, (realHeight-Credits34Height)/2))
                                VisualYdisplacement -= 60/(self.aFPS/self.Iteration)
                                if EndClock >= 5:
                                    GoTo = "Home"
                                else:
                                    EndClock += 1/(self.aFPS/self.Iteration)
                            else:
                                self.Display.blit(Credits34, ((realWidth-Credits34Width)/2, 1402+VisualYdisplacement))
                                VisualYdisplacement -= 60/(self.aFPS/self.Iteration)
                        else:
                            cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)
                            self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)
                            self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0+IntroYDisplacement))
                            self.Display.blit(CreditsFont, (((realWidth-TitleWidth)/2)+65, 50+IntroYDisplacement))
                            IntroYDisplacement -= 90/(self.aFPS/self.Iteration)
                            VisualYdisplacement = realHeight

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