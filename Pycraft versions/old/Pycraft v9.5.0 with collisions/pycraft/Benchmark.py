if not __name__ == "__main__":
    print("Started <Pycraft_Benchmark>")
    class GenerateBenchmarkMenu:
        def __init__(self):
            pass

        def Benchmark(self):
            try:
                self.mod_Pygame__.mixer.Channel(2).pause()
                self.Display.fill(self.BackgroundCol) 
                self.mod_Pygame__.display.flip()
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")
                self.VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
                InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                DetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 20)
                InfoDetailsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                TitleFont = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = TitleFont.get_width()

                BenchmarkFont = InfoTitleFont.render("Benchmark", self.aa, self.SecondFontCol)
                FPSinfoTEXT = DetailsFont.render("FPS benchmark results", self.aa, self.FontCol)
                FPSinfoTEXTWidth = FPSinfoTEXT.get_width()
                FILEinfoTEXT = DetailsFont.render("Read test results", self.aa, self.FontCol)
                FILEinfoTEXTWidth = FILEinfoTEXT.get_width()
                HARDWAREinfoTEXT = DetailsFont.render("Hardware results", self.aa, self.FontCol)
                HARDWAREinfoTEXTwidth = HARDWAREinfoTEXT.get_width()

                SixtyFPSData = DataFont.render("60 Hz", self.aa, self.AccentCol)
                OneFourFourFPSData = DataFont.render("144 Hz", self.aa, self.AccentCol)
                TwoFortyFPSData = DataFont.render("240 Hz", self.aa, self.AccentCol)

                InfoFont1 = DataFont.render("Welcome to Benchmark mode, press the SPACE bar to continue or press ANY other key to cancel, or press 'X'", self.aa, self.FontCol)
                InfoFont2 = DataFont.render("Benchmark mode is used to make the 'ADAPTIVE' feature in settings function and also to give an indication of the experience you are likely to get on this device", self.aa, self.FontCol)
                InfoFont3 = DataFont.render("Benchmark mode consists of several stages:", self.aa, self.FontCol)
                InfoFont4 = DataFont.render("First it will gather some basic information about your system", self.aa, self.FontCol)
                InfoFont5 = DataFont.render("Then it will test your maximum frame rate on a blank screen, then with a basic animation, and finally in a 3D OpenGL space", self.aa, self.FontCol)
                InfoFont6 = DataFont.render("After its done that the focus moves on to a quick storage test, before finishing", self.aa, self.FontCol)
                InfoFont7 = DataFont.render("Your results will then be displayed on screen with your frame rate scores on a line graph and the rest detailed to the right", self.aa, self.FontCol)
                InfoFont8 = DataFont.render("During the time the benchmark is running the window may appear unresponsive, don't panic this can be expected.", self.aa, self.FontCol)
                InfoFont9 = DataFont.render("In addition to achieve the best scores try to avoid doing anything else on the computer whilst the benchmark runs", self.aa, self.FontCol)
                InfoFont10 = DataFont.render("This benchmark may show some system instability or cause your device to get warm, you use this at your own risk!", self.aa, (255, 0, 0))

                stage = 0

                resize = False

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

                    if stage == 0:
                        self.Display.fill(self.BackgroundCol)
                        cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)
                        self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)
                        self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                        self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))
                        self.Display.blit(InfoFont1, (3, 100))
                        self.Display.blit(InfoFont2, (3, 130))
                        self.Display.blit(InfoFont3, (3, 145))
                        self.Display.blit(InfoFont4, (3, 160))
                        self.Display.blit(InfoFont5, (3, 175))
                        self.Display.blit(InfoFont6, (3, 190))
                        self.Display.blit(InfoFont7, (3, 220))
                        self.Display.blit(InfoFont8, (3, 235))
                        self.Display.blit(InfoFont9, (3, 250))
                        self.Display.blit(InfoFont10, (3, 280))

                    if stage == 1:
                        self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Getting System Information")
                        CPUid = f"{self.mod_CPUinfo__.get_cpu_info()['brand_raw']} w/{self.mod_Psutil__.cpu_count(logical=False)} cores @ {self.mod_Psutil__.cpu_freq().max} MHz"
                        RAMid = f"{round((((self.mod_Psutil__.virtual_memory().total)/1000)/1000/1000),2)} GB of memory, with {self.mod_Psutil__.virtual_memory().percent}% used"
                        CPUhwINFO = DataFont.render(CPUid, self.aa, (255, 255, 255))
                        CPUhwINFOwidth = CPUhwINFO.get_width()

                        RAMhwINFO = DataFont.render(RAMid, self.aa, (255, 255, 255))
                        RAMhwINFOwidth = RAMhwINFO.get_width()
                        stage += 1

                    if stage == 2:
                        try:
                            Message, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3 = self.mod_ExBenchmark__.LoadBenchmark.run(self)
                            if not Message == None:
                                return Message
                            self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)
                        except:
                            self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")
                            return None
                        else:
                            self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished self.FPS based benchmarks")
                        stage += 1

                    if stage == 3:
                        self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Starting disk read test")
                        ReadIteration = 50
                        for i in range(ReadIteration):
                            with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:
                                Benchdata = Bench.read()

                        aTime = 0
                        ReadIteration = 50
                        for i in range(ReadIteration):
                            start = self.mod_Time__.perf_counter()
                            with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\BenchmarkData.txt")), "r") as Bench:
                                Benchdata = Bench.read()
                            aTime += self.mod_Time__.perf_counter()-start
                        aTime = aTime/(ReadIteration+1)
                        ReadSpeed = (1/(aTime))
                        stage += 1
                    
                    if stage == 4:
                        self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results.")
                        Max1 = 0
                        Min1 = 60
                        for i in range(len(FPSlistY)):
                            if FPSlistY[i] > Max1:
                                Max1 = FPSlistY[i]
                            if FPSlistY[i] < Min1:
                                Min1 = FPSlistY[i]

                        Max2 = 0
                        Min2 = 60
                        for i in range(len(FPSlistY2)):
                            if FPSlistY2[i] > Max2:
                                Max2 = FPSlistY2[i]
                            if FPSlistY2[i] < Min2:
                                Min2 = FPSlistY2[i]

                        self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results..")
                        Max3 = 0
                        Min3 = 60
                        for i in range(len(FPSlistY3)):
                            if FPSlistY3[i] > Max3:
                                Max3 = FPSlistY3[i]
                            if FPSlistY3[i] < Min3:
                                Min3 = FPSlistY3[i]

                        if Max2 > Max1:
                            GlobalMax = Max2
                        elif Max3 > Max2:
                            GlobalMax = Max3
                        else:
                            GlobalMax = Max1

                        self.RecommendedFPS = GlobalMax/2

                        self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Processing Results...")
                        multiplier = len(FPSlistY)/(realWidth-20)
                        temp = []
                        for i in range(len(FPSlistY)):
                            temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))
                        FPSListY = temp

                        temp = []
                        for i in range(len(FPSlistY2)):
                            temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))
                        FPSListY2 = temp

                        temp = []
                        for i in range(len(FPSlistY2)):
                            temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))
                        FPSListY3 = temp

                        Results1 = []
                        for i in range(len(FPSlistY)):
                            Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])

                        Results2 = []
                        for i in range(len(FPSlistY2)):
                            Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])

                        Results3 = []
                        for i in range(len(FPSlistY3)):
                            Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])

                        stage += 1

                    if stage == 5:
                        self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Results")

                        self.Display.fill(self.BackgroundCol)

                        self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                        self.Display.blit(BenchmarkFont, (((realWidth-TitleWidth)/2)+65, 50))

                        FPSRect = self.mod_Pygame__.Rect(10, 130, realWidth-20, 300)
                        self.mod_Pygame__.draw.rect(self.Display, self.ShapeCol, FPSRect, 0)

                        self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*60)))), (realWidth-20, int(130+(300-((300/GlobalMax)*60)))))
                        self.Display.blit(SixtyFPSData, (13, int(130+(300-((300/GlobalMax)*60)))))

                        self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*144)))), (realWidth-20, int(130+(300-((300/GlobalMax)*144)))))
                        self.Display.blit(OneFourFourFPSData, (13, int(130+(300-((300/GlobalMax)*140)))))

                        self.mod_Pygame__.draw.line(self.Display, self.AccentCol, (10, int(130+(300-((300/GlobalMax)*240)))), (realWidth-20, int(130+(300-((300/GlobalMax)*240)))))
                        self.Display.blit(TwoFortyFPSData, (13, int(130+(300-((300/GlobalMax)*240)))))

                        self.mod_Pygame__.draw.lines(self.Display, (0, 255, 0), False, Results1)
                        self.mod_Pygame__.draw.lines(self.Display, (0, 0, 255), False, Results2)
                        self.mod_Pygame__.draw.lines(self.Display, (255, 0, 0), False, Results3)

                        HideRect = self.mod_Pygame__.Rect(0, 110, realWidth, 330)
                        self.mod_Pygame__.draw.rect(self.Display, self.BackgroundCol, HideRect, 20)
                        
                        self.Display.blit(FPSinfoTEXT, ((realWidth-FPSinfoTEXTWidth)-3, 100))
                        self.Display.blit(FILEinfoTEXT, ((realWidth-FILEinfoTEXTWidth)-3, 430))

                        FileResults = DataFont.render(f"Your device achieved a score of: {round(ReadSpeed, 2)}/100 ({round((100/100)*ReadSpeed)}%)", self.aa, self.FontCol)
                        FileResultsWidth = FileResults.get_width()
                        self.Display.blit(FileResults, ((realWidth-FileResultsWidth)-3, 460))
                        
                        self.Display.blit(HARDWAREinfoTEXT, ((realWidth-HARDWAREinfoTEXTwidth)-3, 480))

                        self.Display.blit(CPUhwINFO, ((realWidth-CPUhwINFOwidth)-3, 500))
                        self.Display.blit(RAMhwINFO, ((realWidth-RAMhwINFOwidth)-3, 516))

                        GreenInfo = InfoDetailsFont.render(f"Blank screen test (green); Minimum: {round(Min1, 4)} FPS, Maximum: {round(Max1, 4)} FPS", self.aa, self.FontCol)
                        BlueInfo = InfoDetailsFont.render(f"Drawing test (blue); Minimum: {round(Min2, 4)} FPS, Maximum: {round(Max2, 4)} FPS", self.aa, self.FontCol)
                        RedInfo = InfoDetailsFont.render(f"OpenGL test (red); Minimum: {round(Min3, 4)} FPS, Maximum: {round(Max3, 4)} FPS", self.aa, self.FontCol)
                        self.Display.blit(GreenInfo, (3, 430))
                        self.Display.blit(BlueInfo, (3, 445))
                        self.Display.blit(RedInfo, (3, 460))

                        if resize == True:
                            stage = 4
                            resize = False

                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE) and stage <= 3) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): 
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            self.StartAnimation = True
                            self.RunTimer = 0
                            GoTo = "Home"
                        if (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_SPACE) and stage == 0:
                            stage += 1
                        if event.type == self.mod_Pygame__.VIDEORESIZE:
                            resize = True

                    if GoTo == None:
                        self.mod_DisplayUtils__.DisplayAnimations.FadeIn(self)
                    else:
                        self.mod_DisplayUtils__.DisplayAnimations.FadeOut(self, GoTo)

                    if self.StartAnimation == False and (not GoTo == None):
                        return None

                    self.mod_Pygame__.display.flip()
                    self.clock.tick(self.FPS)
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