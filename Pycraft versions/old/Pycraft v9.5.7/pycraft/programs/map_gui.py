if __name__ != "__main__":
    try:
        import sys
        import os
        import traceback
        
        import pygame
        from PIL import Image
        import pyautogui

        from registry_utils import Registry
        
        import sound_utils
        import display_utils
        import caption_utils
        import error_utils
        import file_utils
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

    class generate_map_gui(Registry):
        def __init__(dictionary):
            for key in dictionary:
                setattr(Registry, key, dictionary[key])
                
            pygame.init()

        def get_map_pos(in_x, in_z):
            x = 0
            z = 0
            if in_x == 0:
                x = 640
            if in_z == 0:
                z = 360
            x -= 6
            z -= 19
            return (x,z)

        def map_gui(
                start_map,
                dictionary):
            
            try:
                generate_map_gui.__init__(dictionary)
                
                Registry.input_key = file_utils.pycraft_config_utils.read_input_key()
                
                font_path = Registry.base_folder / "fonts" / "Book Antiqua.ttf"
                backup_font_path = Registry.base_folder / "fonts" / "NotoSans-Regular.ttf"
                Registry.icon_path = Registry.base_folder / "resources" / "general resources" / "Icon.png"

                Registry.title_font = pygame.font.Font(
                    font_path,
                    60)

                Registry.subtitle_font = pygame.font.Font(
                    font_path,
                    35)

                Registry.option_font = pygame.font.Font(
                    font_path,
                    30)

                Registry.large_content_font = pygame.font.Font(
                    font_path,
                    20)

                Registry.small_content_font = pygame.font.Font(
                    font_path,
                    15)

                Registry.title_backup_font = pygame.font.Font(
                    backup_font_path,
                    60)

                Registry.subtitle_backup_font = pygame.font.Font(
                    backup_font_path,
                    35)

                Registry.option_backup_font = pygame.font.Font(
                    backup_font_path,
                    30)

                Registry.large_content_backup_font = pygame.font.Font(
                    backup_font_path,
                    20)

                Registry.small_content_backup_font = pygame.font.Font(
                    backup_font_path,
                    15)
        
                Registry.window_icon = pygame.image.load(Registry.icon_path)

                map_image_path = Registry.base_folder / "resources" / "map resources" / "Full_Map.png"
                marker_image_path = Registry.base_folder / "resources" / "map resources" / "Marker.png"
                    
                MapPIL =  Image.open(map_image_path)

                Map0 = pygame.image.fromstring(
                    MapPIL.tobytes(),
                    MapPIL.size,
                    MapPIL.mode)

                MapIcon = pygame.image.load(marker_image_path)

                zoom = 0

                X,Y = 0,0
                key = ""

                MapPIL0 =  Image.open(map_image_path).resize(
                    (Registry.real_window_width,
                        Registry.real_window_height),
                    Image.ANTIALIAS)

                Map0 = pygame.image.fromstring(
                    MapPIL0.tobytes(),
                    MapPIL0.size,
                    MapPIL0.mode)

                MapPIL1 =  Image.open(map_image_path).resize(
                    (int(Registry.real_window_width*1.75),
                        int(Registry.real_window_height*1.75)),
                    Image.ANTIALIAS)

                Map1 = pygame.image.fromstring(
                    MapPIL1.tobytes(),
                    MapPIL1.size,
                    MapPIL1.mode)

                MapPIL2 =  Image.open(map_image_path).resize(
                    (int(Registry.real_window_width*2),
                        int(Registry.real_window_height*2)),
                    Image.ANTIALIAS)

                Map2 = pygame.image.fromstring(
                    MapPIL2.tobytes(),
                    MapPIL2.size,
                    MapPIL2.mode)

                while True:
                    start_map.wait()
                    
                    pygame.display.init()

                    display_utils.display_utils.set_display()

                    Map0.convert()
                    Map1.convert()
                    Map2.convert()
                    MapIcon.convert_alpha()
                    while True:
                        caption_utils.generate_captions.get_normal_caption(
                            "Map")

                        Registry.display.fill(Registry.background_color)

                        display_utils.display_functionality.core_display_functions(
                                checkEvents=False)

                        for event in pygame.event.get():
                            if (event.type == pygame.QUIT or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Back"]][0])):

                                start_map.clear()

                            if start_map.is_set():
                                if event.type == pygame.WINDOWSIZECHANGED:
                                    MapPIL0 =  Image.open(map_image_path).resize(
                                        (Registry.real_window_width,
                                            Registry.real_window_height),
                                        Image.ANTIALIAS)

                                    Map0 = pygame.image.fromstring(
                                        MapPIL0.tobytes(),
                                        MapPIL0.size,
                                        MapPIL0.mode)

                                    MapPIL1 =  Image.open(map_image_path).resize(
                                        (int(Registry.real_window_width*1.75),
                                            int(Registry.real_window_height*1.75)),
                                        Image.ANTIALIAS)

                                    Map1 = pygame.image.fromstring(
                                        MapPIL1.tobytes(),
                                        MapPIL1.size,
                                        MapPIL1.mode)

                                    MapPIL2 =  Image.open(map_image_path).resize(
                                        (int(Registry.real_window_width*2),
                                            int(Registry.real_window_height*2)),
                                        Image.ANTIALIAS)

                                    Map2 = pygame.image.fromstring(
                                        MapPIL2.tobytes(),
                                        MapPIL2.size,
                                        MapPIL2.mode)

                                if event.type == pygame.KEYDOWN:
                                    if (event.key == Registry.input_key[
                                                Registry.input_configuration["keyboard"]["List variables"]][0] and
                                            Registry.extended_developer_options):

                                        tkinter_utils.tkinter_info.create_tkinter_window()
                                
                                    if event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Jump"]][0]:
                                        
                                        zoom = 0

                                    if event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Walk forwards"]][0]:
                                        
                                        key = "w"

                                    if event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Walk backwards"]][0]:
                                        
                                        key = "s"

                                    if event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Walk right"]][0]:
                                        
                                        key = "d"

                                    if event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Walk left"]][0]:
                                        
                                        key = "a"

                                    if event.key == Registry.input_key[
                                            Registry.input_configuration["keyboard"]["Toggle full-screen"]][0]:
                                        
                                        Registry.data_average_fps = []
                                        Registry.data_CPU_usage = []
                                        Registry.data_current_fps = []
                                        Registry.data_memory_usage = []

                                        Registry.timer = 0

                                        Registry.data_average_fps_Max = 1
                                        Registry.data_CPU_usage_Max = 1
                                        Registry.data_current_fps_Max = 1
                                        Registry.data_memory_usage_Max = 1
                                        
                                        display_utils.display_utils.update_display()

                                if event.type == pygame.KEYUP:
                                    key = ""

                                if event.type == pygame.MOUSEWHEEL:
                                    if str(event.y)[0] == "-":
                                        zoom -= 1
                                    else:
                                        zoom += 1

                        if not start_map.is_set():
                            break
                            
                        if Registry.use_mouse_input is False:
                            if Registry.joystick_zoom == "-":
                                zoom -= 1
                                Registry.joystick_zoom = None

                            elif Registry.joystick_zoom == "+":
                                zoom += 1
                                Registry.joystick_zoom = None

                            joystick_mouse = pygame.mouse.get_rel()

                            if joystick_mouse[0] > 0:
                                key = "a"

                            elif joystick_mouse[0] < 0:
                                key = "d"

                            elif joystick_mouse[1] > 0:
                                key = "w"

                            elif joystick_mouse[1] < 0:
                                key = "s"

                            else:
                                key = ""

                            if Registry.joystick_exit:
                                Registry.joystick_exit = False

                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                break

                        if zoom >= 2:
                            zoom = 2
                        if zoom <= 0:
                            zoom = 0

                        if key == "w":
                            if zoom == 1:
                                Y -= 5
                            elif zoom == 2:
                                Y -= 10
                        if key == "s":
                            if zoom == 1:
                                Y += 5
                            elif zoom == 2:
                                Y += 10
                        if key == "d":
                            if zoom == 1:
                                X += 5
                            elif zoom == 2:
                                X += 10
                        if key == "a":
                            if zoom == 1:
                                X -= 5
                            elif zoom == 2:
                                X -= 10

                        if zoom == 1:
                            Registry.display.blit(
                                Map1,
                                (X,Y))

                            Registry.display.blit(
                                MapIcon,
                                generate_map_gui.get_map_pos(Registry.x, Registry.z))

                            if X <= -955:
                                X = -955
                            if Y <= -535:
                                Y = -535
                            if X >= -5:
                                X = -5
                            if Y >= -5:
                                Y = -5
                        elif zoom == 2:
                            Registry.display.blit(
                                Map2,
                                (X,Y))

                            Registry.display.blit(
                                MapIcon,
                                generate_map_gui.get_map_pos(Registry.x, Registry.z))

                            if X <= -1590:
                                X = -1590
                            if Y <= -890:
                                Y = -890
                            if X >= -10:
                                X = -10
                            if Y >= -10:
                                Y = -10
                        else:
                            Registry.display.blit(
                                Map0,
                                (0,0))

                            Registry.display.blit(
                                MapIcon,
                                generate_map_gui.get_map_pos(Registry.x, Registry.z))

                        pygame.display.flip()
                        tempfps = display_utils.display_utils.get_play_status()
                            
                        Registry.clock.tick(tempfps)

                    pygame.display.quit()
            except Exception as Message:
                error_message = "map_gui > generate_map_gui > map_gui: "+str(Message)

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "startup Fail",
        "You need to run this as part of Pycraft,please run the 'main.py' file")
    quit()
