if __name__ != "__main__":
    try:
        import sys
        import ctypes
        
        import pygame
        import pyautogui

        from registry_utils import Registry
        import sound_utils
        import logging_utils
        import tkinter_utils
    except Exception as Message:
        try:
            import sys
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "startup Fail",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
            
    class display_functionality(Registry):
        def __init__(self):
            pass

        def core_display_functions(
                location="home",
                checkEvents=True,
                resize=True,
                return_events=False,
                disable_events=False):

            if not (Registry.error_message_detailed is None):
                raise Exception(Registry.error_message_detailed)

            if not (Registry.error_message is None):
                raise Exception(Registry.error_message)

            pygame.joystick.init()
            joystick_count = pygame.joystick.get_count()
            if joystick_count > 0:
                Registry.joystick_connected = True
            else:
                Registry.joystick_connected = False
            
            if Registry.use_mouse_input is False:
                for i in range(joystick_count):
                    joystick = pygame.joystick.Joystick(i)
                    axes = joystick.get_numaxes()
                    
                    for j in range(axes):
                        multiplier = ((60 * 4) / (Registry.average_fps / Registry.iteration))
                        axis = round(joystick.get_axis(j), 6) * multiplier

                        if j == 0:
                            Registry.mouse_x += axis * Registry.x_scale_factor
                        if j == 1:
                            Registry.mouse_y += axis * Registry.y_scale_factor

                    buttons = joystick.get_numbuttons()

                    for j in range(buttons):
                        button = joystick.get_button(j)

                        if j == 1:
                            if (button == 1 and
                                    Registry.go_to is None):
                                Registry.primary_mouse_button_down = True
                            
                            else:
                                Registry.primary_mouse_button_down = False

                        if j == 0:
                            if (button == 1 and Registry.go_to is None):
                                Registry.joystick_exit = True

                            else:
                                Registry.joystick_exit = False

                    hats = joystick.get_numhats()
                    
                    for j in range(hats):
                        hat = joystick.get_hat(j)
                        for k in range(len(hat)):
                            if int(hat[k]) == 1:
                                if Registry.joystick_hat_pressed is False:
                                    Registry.joystick_hat_pressed = True

                            if k == 0:
                                if int(hat[k]) == 1:
                                    Registry.joystick_zoom = "+"
                                if int(hat[k]) == -1:
                                    Registry.joystick_zoom = "-"

                if Registry.window_in_focus:
                    pygame.mouse.set_pos(
                        Registry.mouse_x,
                        Registry.mouse_y)
            else:
                Registry.mouse_x = pygame.mouse.get_pos()[0]
                Registry.mouse_y = pygame.mouse.get_pos()[1]

            Registry.real_window_width = pygame.display.get_window_size()[0]
            Registry.real_window_height = pygame.display.get_window_size()[1]

            if Registry.saved_window_width < 1280:
                display_utils.generate_min_display(
                    1280)

            if Registry.saved_window_height < 720:
                display_utils.generate_min_display(
                    720)

            fullscreen_x = pyautogui.size()[0]
            fullscreen_y = pyautogui.size()[1]

            if Registry.saved_window_width == fullscreen_x:
                Registry.saved_window_width = 1280

            if Registry.saved_window_height == fullscreen_y:
                Registry.saved_window_height = 720

            if not (Registry.real_window_width == fullscreen_x or
                    Registry.real_window_height == fullscreen_y):
                
                Registry.saved_window_width = pygame.display.get_window_size()[0]
                Registry.saved_window_height = pygame.display.get_window_size()[1]

            if Registry.iteration > 1000:
                Registry.average_fps = (Registry.average_fps/Registry.iteration)
                Registry.iteration = 1
                
            Registry.current_fps = Registry.clock.get_fps()
            Registry.average_fps += Registry.current_fps
            Registry.iteration += 1

            Registry.y_scale_factor = Registry.real_window_height/720
            Registry.x_scale_factor = Registry.real_window_width/1280

            if Registry.use_mouse_input is False:
                if Registry.joystick_exit:
                    Registry.joystick_exit = False
                    if Registry.sound:
                        sound_utils.play_sound.play_click_sound()

                    if location == "exit":
                        pygame.quit()
                        sys.exit()

                    else:
                        Registry.startup_animation = True
                        Registry.run_timer = 0
                        Registry.go_to = location

            if checkEvents:
                try:
                    displayEvents = pygame.event.get()
                    
                except Exception as Message:
                    joystick_fix = "<built-in function get> returned a result with an exception set"
                    if str(Message) == joystick_fix:
                        displayEvents = []
                    else:
                        logging_utils.create_log_message.update_log_warning(
                            Message)
                        
                for event in displayEvents:
                    if (((event.type == pygame.QUIT
                            or (event.type == pygame.KEYDOWN
                                    and event.key == Registry.input_key[Registry.input_configuration["keyboard"]["Back"]][0])) and
                            Registry.go_to is None and
                            disable_events is False)):

                        Registry.joystick_exit = False

                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        if location == "exit":
                            pygame.quit()
                            sys.exit()
                            
                        else:
                            Registry.startup_animation = True
                            Registry.run_timer = 0
                            Registry.go_to = location

                    if event.type == pygame.WINDOWFOCUSLOST:
                        Registry.window_in_focus = False
                    elif event.type == pygame.WINDOWFOCUSGAINED:
                        Registry.window_in_focus = True

                    if Registry.use_mouse_input:
                        if (((event.type == pygame.MOUSEBUTTONDOWN or
                                    pygame.mouse.get_pressed()[0]) and
                                (not event.type == pygame.MOUSEMOTION)) and
                                Registry.go_to is None and
                                    (not Registry.primary_mouse_button_down) and
                                    (not Registry.secondary_mouse_button_down)):

                            if event.button == Registry.input_configuration["mouse"]["Primary"]:
                                Registry.primary_mouse_button_down = True
                            elif event.button == Registry.input_configuration["mouse"]["Secondary"]:
                                Registry.secondary_mouse_button_down = True

                        else:
                            Registry.primary_mouse_button_down = False
                            Registry.secondary_mouse_button_down = False
                            
                        if (event.type == pygame.KEYDOWN and
                                disable_events is False):
                            
                            if (event.key == Registry.input_key[Registry.input_configuration["keyboard"]["List variables"]][0] and
                                    Registry.extended_developer_options):

                                tkinter_utils.tkinter_info.create_tkinter_window()
                                
                            if (event.key == Registry.input_key[Registry.input_configuration["keyboard"]["Toggle full-screen"]][0] and
                                    resize):

                                Registry.data_average_fps = []
                                Registry.data_CPU_usage = []
                                Registry.data_current_fps = []
                                Registry.data_memory_usage = []

                                Registry.timer = 0

                                Registry.data_average_fps_Max = 1
                                Registry.data_CPU_usage_Max = 1
                                Registry.data_current_fps_Max = 1
                                Registry.data_memory_usage_Max = 1
                                
                                display_utils.update_display()

                            if event.key == Registry.input_key[Registry.input_configuration["keyboard"]["Confirm"]][0]:
                                Registry.primary_mouse_button_down = True

                if return_events:
                    return displayEvents
                    
    class display_utils(Registry):
        def __init__(self):
            pass

        def update_display(
                opengl=False,
                clear_additional_arguments=True,
                fullscreen_size=pyautogui.size()):
            
            try:
                if clear_additional_arguments:
                    Registry.data_average_fps = []
                    Registry.data_CPU_usage = []
                    Registry.data_current_fps = []
                    Registry.data_memory_usage = []

                    Registry.timer = 0

                    Registry.data_average_fps_Max = 1
                    Registry.data_CPU_usage_Max = 1
                    Registry.data_current_fps_Max = 1
                    Registry.data_memory_usage_Max = 1
                    
                pygame.display.set_icon(Registry.window_icon)

                if Registry.fullscreen is False:
                    Registry.fullscreen = True
                    if opengl:
                        if Registry.vsync:
                            Registry.display = pygame.display.set_mode(
                                (Registry.saved_window_width,
                                    Registry.saved_window_height),
                                pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=1)
                            
                        else:
                            Registry.display = pygame.display.set_mode(
                                (Registry.saved_window_width,
                                    Registry.saved_window_height),
                                pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=0)

                    else:
                        Registry.display = pygame.display.set_mode(
                            (Registry.saved_window_width,
                                Registry.saved_window_height),
                            pygame.RESIZABLE)

                elif Registry.fullscreen:
                    Registry.fullscreen = False
                    if opengl:
                        if Registry.vsync:
                            Registry.display = pygame.display.set_mode(
                                (Registry.fullscreen_x,
                                    Registry.fullscreen_y),
                                pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=1)

                        else:
                            Registry.display = pygame.display.set_mode(
                                fullscreen_size,
                                pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=0)

                    else:
                        Registry.display = pygame.display.set_mode(
                            fullscreen_size,
                            pygame.FULLSCREEN)

            except Exception as Message:
                log_message = "display_utils > display_utils > update_display: "+ str(Message)
                
                logging_utils.create_log_message.update_log_warning(
                    log_message)
                
                Registry.fullscreen = True
                Registry.saved_window_width = 1280
                Registry.saved_window_height = 720
                pygame.display.quit()
                pygame.init()
                pygame.display.set_icon(Registry.window_icon)
                
                Registry.display = pygame.display.set_mode(
                    (Registry.saved_window_width, Registry.saved_window_height))

        def set_display(
                opengl=False,
                hidden=False,
                clear_additional_arguments=True,
                fullscreen_size=pyautogui.size()):
            
            try:
                if clear_additional_arguments:
                    Registry.data_average_fps = []
                    Registry.data_CPU_usage = []
                    Registry.data_current_fps = []
                    Registry.data_memory_usage = []

                    Registry.timer = 0

                    Registry.data_average_fps_Max = 1
                    Registry.data_CPU_usage_Max = 1
                    Registry.data_current_fps_Max = 1
                    Registry.data_memory_usage_Max = 1
                    
                pygame.display.set_icon(Registry.window_icon)

                if hidden:
                    Registry.display = pygame.display.set_mode(
                        (Registry.saved_window_width,
                            Registry.saved_window_height),
                        pygame.HIDDEN)

                else:
                    if Registry.fullscreen:
                        if opengl:
                            if Registry.vsync:
                                Registry.display = pygame.display.set_mode(
                                    (Registry.saved_window_width,
                                        Registry.saved_window_height),
                                    pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=1)
                                
                            else:
                                Registry.display = pygame.display.set_mode(
                                    (Registry.saved_window_width,
                                        Registry.saved_window_height),
                                    pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=0)
                        else:
                            Registry.display = pygame.display.set_mode(
                                (Registry.saved_window_width,
                                    Registry.saved_window_height),
                                pygame.RESIZABLE)
                            
                    elif Registry.fullscreen is False:
                        if opengl:
                            if Registry.vsync:
                                Registry.display = pygame.display.set_mode(
                                    fullscreen_size,
                                    pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=0)
                                
                            else:
                                Registry.display = pygame.display.set_mode(
                                    fullscreen_size,
                                    pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=1)
                        else:
                            Registry.display = pygame.display.set_mode(
                                fullscreen_size,
                                pygame.FULLSCREEN)
                            
            except Exception as Message:
                log_message = "display_utils > display_utils > set_display:", Message
                
                logging_utils.create_log_message.update_log_warning(
                    log_message)
                
                Registry.saved_window_width = 1280
                Registry.saved_window_height = 720
                
                pygame.display.quit()
                pygame.init()
                
                Registry.display = pygame.display.set_mode(
                    (Registry.saved_window_width,
                        Registry.saved_window_height))

                pygame.display.set_icon(Registry.window_icon)

        def generate_min_display(vsync, window_icon, width, height):
            pygame.display.set_icon(window_icon)
            
            if vsync:
                display = pygame.display.set_mode(
                    (width, height),
                    pygame.RESIZABLE,
                    vsync=1)
                
            else:
                display = pygame.display.set_mode(
                    (width, height),
                    pygame.RESIZABLE,
                    vsync=0)

            return display

        def get_display_location():
            hwnd = pygame.display.get_wm_info()["window"]

            prototype = ctypes.WINFUNCTYPE(
                ctypes.wintypes.BOOL,
                ctypes.wintypes.HWND,
                ctypes.POINTER(
                    ctypes.wintypes.RECT))

            paramflags = (1, "hwnd"), (2, "lprect")

            GetWindowRect = prototype(
                ("GetWindowRect", ctypes.windll.user32),
                paramflags)

            rect = GetWindowRect(hwnd)
            return rect.left+8, rect.top+31


        def get_play_status():
            
            if pygame.display.get_active():
                if Registry.platform == "Windows" and Registry.vsync:
                    tempfps = Registry.vsync_fps
                    
                else:
                    tempfps = Registry.fps
                    
                Registry.project_sleeping = False
                if not (Registry.command == "Play" or
                            Registry.command == "benchmark"):
                    
                    if Registry.music:
                        pygame.mixer.music.unpause()
                        if pygame.mixer.music.get_busy() == 0:
                            sound_utils.play_sound.play_inventory_sound()
            else:
                tempfps = 5
                Registry.project_sleeping = True
                pygame.mixer.music.fadeout(500)

            if Registry.fps_overclock:
                tempfps = 2000

            return tempfps

    class display_animations(Registry):
        def __init__(self):
            pass


        def fade_in(
                size="full"):
            
            if Registry.startup_animation:
                if size == "full":
                    HideSurface = pygame.Surface(
                        (Registry.real_window_width, Registry.real_window_height))
                else:
                    HideSurface = pygame.Surface(
                        (Registry.real_window_width, Registry.real_window_height-40))

                SurfaceAlpha = 255-(Registry.run_timer*1000)
                HideSurface.set_alpha(SurfaceAlpha)
                HideSurface.fill(Registry.background_color)
                Registry.display.blit(
                    HideSurface,
                    (0, 100))

                if SurfaceAlpha <= 0:
                    Registry.startup_animation = False

        def fade_out(
                size="full"):
            
            if Registry.startup_animation:
                if size == "full":
                    HideSurface = pygame.Surface(
                        (Registry.real_window_width, Registry.real_window_height-100))
                else:
                    HideSurface = pygame.Surface(
                        (Registry.real_window_width, Registry.real_window_height-140))

                SurfaceAlpha = 255-(Registry.run_timer*1000)
                HideSurface.set_alpha(255-SurfaceAlpha)
                HideSurface.fill(Registry.background_color)

                if Registry.go_to == "credits":
                    Registry.display.blit(
                        HideSurface,
                        (0, 0))
                else:
                    Registry.display.blit(
                        HideSurface,
                        (0, 100))

                if SurfaceAlpha <= 0:
                    Registry.startup_animation = False
                    
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
