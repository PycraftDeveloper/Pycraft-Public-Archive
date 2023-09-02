if __name__ != "__main__":
    try:
        import sys
        import os
        import traceback
        import time
        
        import pygame
        import pyautogui
        import dill

        from registry_utils import Registry
        
        import display_utils
        import caption_utils
        import error_utils
        import file_utils
        import text_utils
        import drawing_utils
        import logging_utils
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
            
    class generate_load_screen:
        def __init__(dictionary):
            for key in dictionary:
                setattr(Registry, key, dictionary[key])
                
            pygame.init()

        def load(
                start_loading,
                additional_data,
                dictionary):

            try:
                generate_load_screen.__init__(dictionary)
                
                pygame.font.init()
                
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
                
                average_load_time = Registry.load_time[0]/Registry.load_time[1]

                while True:
                    start_loading.wait()

                    pygame.display.init()

                    display_utils.display_utils.set_display()

                    loading_progress = 0

                    splash_text = text_utils.generate_text.load_quick_text()
                    
                    start_load_timer = time.perf_counter()

                    while True:
                        current_load_time = time.perf_counter()-start_load_timer
                        if additional_data.poll():
                            loading_progress = additional_data.recv()["loading_progress"]
                        
                        if loading_progress <= 10:
                            text = "Initializing"
                        elif loading_progress <= 20:
                            text = "Creating display"
                        elif loading_progress <= 30:
                            text = "Creating celestial entities"
                        elif loading_progress <= 40:
                            text = "Loading in-game objects: Map"
                        elif loading_progress <= 50:
                            text = "Loading in-game textures: Skysphere"
                        elif loading_progress <= 60:
                            text = "Loading in-game programmes"
                        elif loading_progress <= 70:
                            text = "Applying programme configurations"
                        elif loading_progress <= 80:
                            text = "Loading in-game textures: Grass"
                        else:
                            text = "Making final touches"

                        try:
                            modifier = current_load_time/average_load_time
                        except Exception as message:
                            warning_message = str(message)
                            logging_utils.create_log_message.update_log_warning(
                                warning_message)
                            
                            modifier = 1

                        percent_complete = modifier*100
                        if percent_complete > 100:
                            percent_complete = 100
                            
                        loading_bar = 100+(modifier*(Registry.real_window_width-200))

                        if loading_bar > Registry.real_window_width-100:
                            loading_bar = Registry.real_window_width-100
                        
                        caption_utils.generate_captions.get_normal_caption(
                            "Loading")

                        if not (Registry.error_message is None or
                                    Registry.error_message_detailed is None):
                            
                            error_utils.generate_error_screen.error_screen(
                                Registry.error_message,
                                Registry.error_message_detailed)

                        Registry.display.fill(Registry.background_color)

                        returned_text = text_utils.text_formatter.format_text(
                            "Pycraft",
                            ("center", "top"),
                            Registry.title_font,
                            Registry.title_backup_font)

                        title_width = returned_text.get_width()

                        loading_text = text_utils.text_formatter.format_text(
                            "Loading",
                            (((Registry.real_window_width-title_width)/2)+55, 50),
                            Registry.subtitle_font,
                            Registry.subtitle_backup_font,
                            font_color=Registry.secondary_font_color)

                        graphics_size = ((Registry.real_window_height-120)-(loading_text.get_height()+50))-100
                        
                        drawing_utils.draw_rose.create_rose(
                            False,
                            (Registry.real_window_width-graphics_size)/2,
                            (Registry.real_window_height-graphics_size)/2,
                            graphics_size,
                            graphics_size)

                        text_utils.text_formatter.format_text(
                            text,
                            ("center", Registry.real_window_height-100),
                            Registry.small_content_font,
                            Registry.small_content_backup_font,
                            font_color=Registry.secondary_font_color)

                        text_utils.text_formatter.format_text(
                            splash_text,
                            ("center", Registry.real_window_height-120),
                            Registry.small_content_font,
                            Registry.small_content_backup_font,
                            font_color=Registry.secondary_font_color)

                        text_utils.text_formatter.format_text(
                            f"{str(int(percent_complete))}% complete",
                            ("center", Registry.real_window_height-80),
                            Registry.small_content_font,
                            Registry.small_content_backup_font,
                            font_color=Registry.secondary_font_color)

                        pygame.draw.line(
                            Registry.display,
                            Registry.shape_color,
                            (100, Registry.real_window_height-100),
                            (100+(Registry.real_window_width-200), Registry.real_window_height-100),
                            width=round(Registry.y_scale_factor))
                        
                        pygame.draw.line(
                            Registry.display,
                            Registry.accent_color,
                            (100, Registry.real_window_height-100),
                            (loading_bar, Registry.real_window_height-100),
                            width=round(Registry.y_scale_factor))

                        display_utils.display_functionality.core_display_functions(
                            checkEvents=False)

                        if Registry.joystick_exit:
                            break

                        for event in pygame.event.get():
                            if (event.type == pygame.QUIT or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == pygame.K_ESCAPE) or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == pygame.K_e)):
                                
                                start_loading.clear()
                                pygame.display.quit()

                            if start_loading.is_set():
                                if event.type == pygame.WINDOWFOCUSLOST:
                                    Registry.window_in_focus = False
                                elif event.type == pygame.WINDOWFOCUSGAINED:
                                    Registry.window_in_focus = True

                                if event.type == pygame.WINDOWSIZECHANGED:
                                    Registry.real_window_width = pygame.display.get_window_size()[0]
                                    Registry.real_window_height = pygame.display.get_window_size()[1]

                        if not start_loading.is_set():
                            break
                        
                        pygame.display.flip()
                        
                        tempfps = display_utils.display_utils.get_play_status()
                            
                        Registry.clock.tick(tempfps)

                    pygame.display.quit()
            except Exception as Message:
                error_message = "loading_screen > generate_load_screen > load: "+str(Message)

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))
                
                print(error_message_detailed)

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
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()