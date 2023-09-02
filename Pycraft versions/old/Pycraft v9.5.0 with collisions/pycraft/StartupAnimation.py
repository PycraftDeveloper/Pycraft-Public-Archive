if not __name__ == "_main_":
    print("Started <Pycraft_StartupAnimation>")
    class GenerateStartupScreen:
        def _init_(self):
            pass

        def Start(self):
            try:
                PresentsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                PycraftFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                NameFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 45)

                NameText = NameFont.render("Tom Jebbo", True, self.FontCol)
                NameTextWidth = NameText.get_width()
                NameTextHeight = NameText.get_height()

                self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()

                self.Display.fill(self.BackgroundCol)
                self.mod_Pygame__.display.flip()
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version} | Welcome")

                PresentsText = PresentsFont.render("presents", True, self.FontCol)
                presentOffSet = 100

                PycraftText = PycraftFont.render("Pycraft", True, self.FontCol)
                TitleTextWidth = PycraftText.get_width()
                PycraftStartPos = self.mod_Pygame__.Vector2(((self.realWidth-TitleTextWidth)/2, self.realHeight/2 - NameTextHeight))

                PycraftEndPos = self.mod_Pygame__.Vector2(PycraftStartPos.x, 0)

                self.clock = self.mod_Pygame__.time.Clock()

                InterpolateSpeed = 0.002

                self.mod_Pygame__.time.delay(2000)

                timer = 5
                deltaTime = 0
                
                while timer > 0 and self.RunFullStartup == True:
                    self.Display.fill(self.BackgroundCol)
                    timer -= deltaTime
                    self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, self.realHeight/2 - NameTextHeight))
                    
                    if timer <= 1.5:
                        self.Display.blit(PresentsText, ((self.realWidth-NameTextWidth)/2 + presentOffSet, self.realHeight/2 + NameTextHeight - 70))

                    deltaTime = self.clock.tick(30) / 1000
                    self.mod_Pygame__.display.flip()

                while True:
                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT:
                            self.Stop_Thread_Event.set()
                            try:
                                self.Thread_StartLongThread.join()
                                self.Thread_AdaptiveMode.join()
                                self.Thread_StartLongThread.join()
                                self.Thread_Get_Outdated.join()
                            except Exception as Error:
                                print(Error)
                                pass

                            self.mod_Pygame__.quit()
                            self.mod_Sys__.exit("Thanks for playing")
                            quit()

                    if self.realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if self.realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)
                    
                    self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()
                    self.Display.fill(self.BackgroundCol)

                    PycraftStartPos = self.mod_Pygame__.math.Vector2.lerp(PycraftStartPos, PycraftEndPos, InterpolateSpeed)
                    self.Display.blit(PycraftText, (PycraftStartPos.x, PycraftStartPos.y))

                    self.mod_Pygame__.display.flip()
                    if PycraftStartPos.y <= 1:
                        PycraftStartPos = PycraftEndPos
                        self.RunFullStartup = False
                        break
                

            except Exception as Message:
                self.RunFullStartup = False
                return Message
    
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()