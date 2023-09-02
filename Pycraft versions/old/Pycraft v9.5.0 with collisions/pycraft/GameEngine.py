if not __name__ == "__main__":
    print("Started <Pycraft_GameEngine>")
    
    from ShareDataUtil import Class_Startup_variables as SharedData
    import collisiondetectionUtil as col
    
    SharedData.mod_ModernGL_window_.setup_basic_logging(0)
    
    
    class Cubemap(SharedData.mod_Base__.CameraWindow):
        SharedData.mod_Base__.CameraWindow.title = f"Pycraft: v{SharedData.version}: Playing"
        SharedData.mod_Base__.CameraWindow.resource_dir = SharedData.base_folder
        
        
        def Exit(self, SharedData, Command):
            try:
                if SharedData.mod_Pygame__.mixer.Channel(3).get_busy() == True:
                    SharedData.mod_Pygame__.mixer.Channel(3).stop()
                    SharedData.mod_Pygame__.quit()
                    
                self.wnd.mouse_exclusivity = False
            except Exception as Error:
                print("GE", Error)
                pass
            self.wnd._set_fullscreen(False)
            self.wnd.close()
            self.wnd.destroy()
            SharedData.CurrentlyPlaying = None
            SharedData.LoadMusic = True
            SharedData.Command = Command
            if self.wnd.fullscreen == True:
                SharedData.Fullscreen = False
            else:
                SharedData.Fullscreen = True
            self.cube.release()
            self.obj.release()
            self.SkyBox_texture.release()
            del self


        def __init__(self, **kwargs):
            try:
                super().__init__(**kwargs)
            
                self.size = self.wnd.buffer_size
                        
                WindowSize = SharedData.realWidth, SharedData.realHeight
                CurrentWindowSize = WindowSize
                
                self.wnd.size = WindowSize
                self.wnd.mouse_exclusivity = False
                                
                self.camera.projection.update(near=0.1, far=100.0)
                self.camera.zoom = 2.5
                                
                self.obj = self.load_scene(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")))
                #print(self.obj.diagonal_size)
                            
                self.cube = SharedData.mod_ModernGL_window_.geometry.cube(size=(20, 20, 20))
                
                self.prog = self.load_program(SharedData.mod_OS__.path.join(SharedData.base_folder, ("programs//cubemap.glsl")))

                self.SkyBox_texture = self.load_texture_cube(
                    neg_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg")),
                    neg_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg")),
                    neg_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg")),
                    pos_x=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg")),
                    pos_y=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg")),
                    pos_z=SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg")),
                    flip_x=True,
                )
                    
                Prev_Mouse_Pos = (0,0)
                Mouse_Pos = (0,0)
                DeltaX, DeltaY = 0, 0
                
                self.wnd.exit_key = None
                
                MouseUnlock = True
                
                Jump = False
                JumpID = 0
                
                self.camera.position.y += 0.7
                                
                WkeydownTimer = 0
                AkeydownTimer = 0
                SkeydownTimer = 0
                DkeydownTimer = 0
                
                RunForwardTimer = 0
                
                FPS = 0
                
                Iteration = 0
                                            
                while True:
                    try:
                        if SharedData.mod_Pygame__.mixer.get_busy() == False:
                            SharedData.mod_SoundUtils__.PlaySound.PlayAmbientSound(SharedData)
                    except Exception as Error:
                        print(Error)
                        pass
                        
                    if Iteration == 0:
                        if SharedData.Fullscreen == False:
                            self.wnd.fullscreen = True
                        else:
                            self.wnd.fixed_aspect_ratio = SharedData.realWidth / SharedData.realHeight
                            self.wnd.window_size = SharedData.realWidth, SharedData.realHeight
                            CurrentWindowSize = self.window_size
                            self.wnd.position = (int((SharedData.FullscreenX-CurrentWindowSize[0])/2), int((SharedData.FullscreenY-CurrentWindowSize[1])/2))
                    
                    if Iteration >= 5000:
                        Iteration = 0
                        
                    start = SharedData.mod_Time__.perf_counter()
                    
                    self.ctx.clear(1.0, 1.0, 1.0)
                    
                    CurrentWindowSize = self.window_size

                    Prev_Mouse_Pos = Mouse_Pos 
                    Mouse_Pos = SharedData.mod_Pyautogui__.position()
                    DeltaX, DeltaY = Mouse_Pos[0]-Prev_Mouse_Pos[0], Mouse_Pos[1]-Prev_Mouse_Pos[1]
                    
                    if self.wnd.is_key_pressed(self.wnd.keys.ESCAPE):
                        Cubemap.Exit(self, SharedData, "Undefined")
                        return None
                    if self.wnd.is_key_pressed(self.wnd.keys.W):
                        RunForwardTimer += (1/FPS)
                        if RunForwardTimer <= 10:
                            if SharedData.sound == True: 
                                WkeydownTimer += (1/FPS)
                                if WkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):
                                    SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)
                                    WkeydownTimer = 0
                            self.camera.position.x += 0.005 # 1.42
                        else:
                            if SharedData.sound == True:
                                WkeydownTimer += (1/FPS)
                                if WkeydownTimer >= (SharedData.mod_Random__.randint(25, 75)/100):
                                    SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)
                                    WkeydownTimer = 0
                            self.camera.position.x += 0.005 # 2.2352
                    else:
                        RunForwardTimer = 0
                        
                    if self.wnd.is_key_pressed(self.wnd.keys.A):
                        if SharedData.sound == True: 
                            AkeydownTimer += (1/FPS)
                            if AkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):
                                SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)
                                AkeydownTimer = 0
                        self.camera.position.z += 0.005 # 1.42
                        
                    if self.wnd.is_key_pressed(self.wnd.keys.S):
                        if SharedData.sound == True: 
                            SkeydownTimer += (1/FPS)
                            if SkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):
                                SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)
                                SkeydownTimer = 0
                        self.camera.position.x -= 0.005 # 1.42
                        
                    if self.wnd.is_key_pressed(self.wnd.keys.D):
                        if SharedData.sound == True: 
                            DkeydownTimer += (1/FPS)
                            if DkeydownTimer >= (SharedData.mod_Random__.randint(50, 100)/100):
                                SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)
                                DkeydownTimer = 0
                        self.camera.position.z -= 0.005 # 1.42
                        
                    if self.wnd.is_key_pressed(self.wnd.keys.E):
                        if self.wnd._fullscreen == True:
                            myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((0, 0, SharedData.FullscreenX, SharedData.FullscreenY)))
                            myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                        else:
                            PosX, PosY = self.wnd.position
                            myScreenshot = SharedData.mod_Pyautogui__.screenshot(region=((PosX, PosY, SharedData.realWidth, SharedData.realHeight)))
                            myScreenshot.save(SharedData.mod_OS__.path.join(SharedData.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                        
                        Cubemap.Exit(self, SharedData, "Inventory")
                        return None
                    
                    if self.wnd.is_key_pressed(self.wnd.keys.R):
                        Cubemap.Exit(self, SharedData, "MapGUI")
                        return None
                    if self.wnd.is_key_pressed(self.wnd.keys.L):
                        if MouseUnlock == True:
                            MouseUnlock = False
                        else:
                            MouseUnlock = True
                    if self.wnd.is_key_pressed(self.wnd.keys.SPACE):
                        Jump = True
                        JumpUP = True
                        
                    if Jump == True:
                        if JumpID < 10 and JumpUP == True:
                            JumpID += 1
                            self.camera.position.y += 0.1
                        if JumpID == 10:
                            JumpUP = False
                        if JumpID >= 0 and JumpUP == False:
                            JumpID -= 1
                            self.camera.position.y -= 0.1
                            if JumpID == 0:
                                if SharedData.sound == True:
                                    SharedData.mod_SoundUtils__.PlaySound.PlayFootstepsSound(SharedData)
                                Jump = False
                                JumpID = 0
                    
                    self.ctx.enable(SharedData.mod_ModernGL__.CULL_FACE | SharedData.mod_ModernGL__.DEPTH_TEST)

                    cam = self.camera.matrix
                    prev_cam = cam
                    
                    if (not cam[3][0] == prev_cam[3][0]) and (not cam[3][2] == prev_cam[3][2]): # collisions needs a bit of tweaking but kinda work
                        temp = col.GC(cam[3]) # modify if above to actually work so col isnt checked when not mov
                        self.camera.position.y = (temp+0.7) # put cols in thread
                        print(self.camera.position.y) # col detect does NOT acureately map to world, but does work see 6574
                    cam[3][0] = 0
                    cam[3][1] = 0
                    cam[3][2] = 0

                    self.SkyBox_texture.use(location=0)
                    self.prog['m_proj'].write(self.camera.projection.matrix)
                    self.prog['m_camera'].write(cam)
                    
                    try:
                        if MouseUnlock == True:                        
                            self.camera.rot_state(-DeltaX, -DeltaY)
                            self.wnd.mouse_exclusivity = True
                        else:
                            self.wnd.mouse_exclusivity = False
                    except Exception as Error:
                        print(Error)
                        pass
                    
                    self.ctx.front_face = 'cw'
                    self.cube.render(self.prog)
                    
                    self.ctx.front_face = 'ccw'
                    self.obj.draw(projection_matrix=self.camera.projection.matrix, camera_matrix=self.camera.matrix)
                    
                    try:
                        self.wnd.swap_buffers()
                    except Exception as Error:
                        print(Error)
                        pass
                    
                    FPS = 1/(SharedData.mod_Time__.perf_counter()-start)
                    Iteration += 1
            except Exception as Message:
                print(''.join(SharedData.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                Cubemap.Exit(self, SharedData, "Undefined")
                SharedData.GameError = str(Message)
                return None
                
                
                
    class CreateEngine:
        
        
        def __init__(self):
            pass
        
        
        def GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont):
            try:
                self.Display.fill(self.BackgroundCol)

                self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()

                PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = PycraftTitle.get_width()
                self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))

                LoadingTitle = SecondaryFont.render("Loading", self.aa, self.SecondFontCol)
                self.Display.blit(LoadingTitle, (((self.realWidth-TitleWidth)/2)+55, 50))

                self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, self.realHeight-100), (self.realWidth-100, self.realHeight-100)], 3)
                self.mod_Pygame__.draw.lines(self.Display, (self.AccentCol), self.aa, self.Progress_Line)

                DisplayMessage = LoadingFont.render(self.ProgressMessageText, self.aa, self.FontCol)
                DisplayMessageWidth = DisplayMessage.get_width()
                self.Display.blit(DisplayMessage, ((self.realWidth-DisplayMessageWidth)/2, self.realHeight-120))

                TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)
                TextFontRenderedWidth = TextFontRendered.get_width()
                self.Display.blit(TextFontRendered, ((self.realWidth-TextFontRenderedWidth)/2, self.realHeight-100))
            except Exception as error:
                print(error)

        def Play(self):
            try:
                self.mod_Pygame__.mixer.Channel(2).fadeout(2000)
                
                self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)
                self.mod_Pygame__.quit()
                self.mod_Pygame__.init()
                self.mod_Globals__.Share.initialize(self)
                try:
                    self.mod_ModernGL_window_.run_window_config(Cubemap)
                except Exception as Error:
                    print(Error)
                    pass
                return None
            except Exception as Message:
                print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                return Message, "Undefined"
            
            
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()