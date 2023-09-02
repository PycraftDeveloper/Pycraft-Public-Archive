if not __name__ == "__main__":
    print("Started <Pycraft_ExBenchmark>")
    class LoadBenchmark:
        def __init__(self):
            pass

        def run(self):
            try:
                FPSlistX = []
                FPSlistY = []

                FPSlistX2 = []
                FPSlistY2 = []

                FPSlistX3 = []
                FPSlistY3 = []

                SetFPS = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 200, 250, 300, 350, 500]

                self.Display = self.mod_Pygame__.display.set_mode((1280, 720))

                iteration = 0
                FPScounter = 0
                MaxIteration = 500

                while iteration < 7500:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Blank Window Benchmark @ {SetFPS[FPScounter]} FPS")
                    while not iteration == MaxIteration:
                        if not self.clock.get_fps() == 0:
                            FPSlistX.append(iteration)
                            FPSlistY.append(self.clock.get_fps())
                        self.Display.fill(self.BackgroundCol)
                        for event in self.mod_Pygame__.event.get():
                            if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):
                                return False

                        self.mod_Pygame__.display.flip()
                        iteration += 1
                        self.clock.tick(SetFPS[FPScounter])
                    FPScounter += 1
                    MaxIteration += 500

                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing Animated Benchmark")

                iteration = 0
                FPScounter = 0
                MaxIteration = 500
                run = 0
                y = 10

                while not iteration == 60:
                    self.Display.fill(self.BackgroundCol)
                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):
                            return False

                    self.mod_Pygame__.display.flip()
                    iteration += 1
                    self.clock.tick(60)

                        
                iteration = 0
                FPScounter = 0
                MaxIteration = 500

                while iteration < 7500:
                    run += 1
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running Animated Window Benchmark @ {SetFPS[FPScounter]} FPS")
                    while not iteration == MaxIteration:
                        if not self.clock.get_fps() == 0:
                            FPSlistX2.append(iteration)
                            FPSlistY2.append(self.clock.get_fps())
                        self.Display.fill(self.BackgroundCol)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        self.mod_DrawingUtils__.DrawRose.CreateRose(self, 1, 1, False)
                        for event in self.mod_Pygame__.event.get():
                            if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):
                                return False

                        self.mod_Pygame__.display.flip()
                        iteration += 1
                        self.clock.tick(SetFPS[FPScounter])
                    FPScounter += 1
                    MaxIteration += 500

                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Preparing OpenGL Benchmark")

                iteration = 0
                FPScounter = 0
                MaxIteration = 500
                run = 0
                y = 10

                while not iteration == 60:
                    self.Display.fill(self.BackgroundCol)
                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):
                            return False

                    self.mod_Pygame__.display.flip()
                    iteration += 1
                    self.clock.tick(60)

                self.Display = self.mod_Pygame__.display.set_mode((1280, 720), self.mod_Pygame__.OPENGL|self.mod_Pygame__.DOUBLEBUF)

                iteration = 0
                FPScounter = 0
                MaxIteration = 500
                vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
                edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))

                self.mod_OGLbenchmark__.LoadOGLBenchmark.CreateBenchmark(self)

                while iteration < 7500:
                    self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Running OpenGL Benchmark @ {SetFPS[FPScounter]} FPS")
                    while not iteration == MaxIteration:
                        if not self.clock.get_fps() == 0:
                            FPSlistX3.append(iteration)
                            FPSlistY3.append(self.clock.get_fps())
                        self.mod_OGLbenchmark__.LoadOGLBenchmark.RunBenchmark(self, edges, vertices)
                        for event in self.mod_Pygame__.event.get():
                            if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and (not event.key == self.mod_Pygame__.K_SPACE)):
                                return None

                        self.mod_Pygame__.display.flip()
                        iteration += 1
                        self.clock.tick(SetFPS[FPScounter])
                    FPScounter += 1
                    MaxIteration += 500

                    
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark | Finished Animated Benchmark")
                self.mod_Time__.sleep(5)
            except Exception as Message:
                print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                return Message, None, None, None, None
            else:

                return None, FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()