if __name__ != "__main__":
    try:
        import os
        import time
        import traceback
        import json

        import pygame
        
        from registry_utils import Registry
        
        import caption_utils
        import display_utils
        import drawing_utils
        import text_utils
        import error_utils
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
            
    class generate_credits(Registry):
        def credits_gui():
            try:
                caption_utils.generate_captions.get_normal_caption(
                    "Credits")

                credits_config_path = Registry.base_folder / "data files" / "credits_config.json"
                
                with open(
                        credits_config_path,
                        "r") as file:

                    credits_data = json.load(file)

                structure = []
                for key in credits_data:
                    if "<spacer" in key:
                        structure.append(" ")
                    else:
                        title = key
                        if "{Registry.version}" in title:
                            title = title.replace("{Registry.version}", f"{Registry.version}")
                        structure.append(title)
                        if str(type(credits_data[key])) == "<class 'list'>":
                            for item in credits_data[key]:
                                structure.append(item)
                        elif str(type(credits_data[key])) == "<class 'str'>":
                            structure.append(credits_data[key])


                returned_text = text_utils.text_formatter.format_text(
                    "Pycraft",
                    ("center", "top"),
                    Registry.title_font,
                    Registry.title_backup_font)

                title_width = returned_text.get_width()
                title_height = returned_text.get_height()

                credits_structure = structure

                VisualYdisplacement = Registry.real_window_height
                IntroYDisplacement = (Registry.real_window_height-title_height)/2
                timer = 5

                Holdon_exit = False
                Holdtimer = 0

                LoadText = False
                while True:
                    start_time = time.perf_counter()

                    if not (Registry.error_message is None or
                                Registry.error_message_detailed is None):
                        
                        error_utils.generate_error_screen.error_screen()

                    caption_utils.generate_captions.get_normal_caption(
                        "Credits")

                    display_utils.display_functionality.core_display_functions()

                    Registry.display.fill(Registry.background_color)

                    Ypos = 0
                    for i in range(len(credits_structure)):
                        if LoadText:
                            if i > 0:
                                if credits_structure[i-1] == " ":
                                    returned_text = text_utils.text_formatter.format_text(
                                        credits_structure[i],
                                        ("left", "top"),
                                        Registry.large_content_font,
                                        Registry.large_content_backup_font,
                                        blit=False)
                                        
                                else:
                                    returned_text = text_utils.text_formatter.format_text(
                                        credits_structure[i],
                                        ("left", "top"),
                                        Registry.small_content_font,
                                        Registry.small_content_backup_font,
                                        blit=False)
                                        
                            else:
                                returned_text = text_utils.text_formatter.format_text(
                                    credits_structure[i],
                                    ("left", "top"),
                                    Registry.large_content_font,
                                    Registry.large_content_backup_font,
                                    blit=False)

                            TextSurfaceHeight = returned_text.get_height()
                            TextSurfaceWidth = returned_text.get_width()

                            if TextSurfaceWidth > Registry.real_window_width:
                                displacement = text_utils.text_wrap.blit_text(
                                        credits_structure[i],
                                        (3, Ypos+VisualYdisplacement),
                                        Registry.small_content_font,
                                        Registry.small_content_backup_font)
                                    
                                Ypos += displacement
                                
                            else:
                                if i+1 == len(credits_structure) and Holdon_exit:
                                    TextSurface_x_pos = (Registry.real_window_width-TextSurfaceWidth)/2
                                    TextSurface_y_pos = (Registry.real_window_height-TextSurfaceHeight)/2

                                    Registry.display.blit(
                                        returned_text,
                                        (TextSurface_x_pos, TextSurface_y_pos))
                                else:
                                    if (Ypos+VisualYdisplacement >= 0 and
                                        Ypos+VisualYdisplacement <= Registry.real_window_height):

                                        TextSurface_x_pos = (Registry.real_window_width-TextSurfaceWidth)/2
                                        TextSurface_y_pos = Ypos+VisualYdisplacement

                                        Registry.display.blit(
                                            returned_text,
                                            (TextSurface_x_pos, TextSurface_y_pos))

                            Ypos += TextSurfaceHeight

                    if timer >= 1:
                        returned_text = text_utils.text_formatter.format_text(
                            "Pycraft",
                            ("center", 0+IntroYDisplacement),
                            Registry.title_font,
                            Registry.title_backup_font)

                        title_width = returned_text.get_width()

                        timer -= 1/(Registry.average_fps/Registry.iteration)
                        VisualYdisplacement = Registry.real_window_height
                    else:
                        if IntroYDisplacement <= 0:
                            cover_Rect = pygame.Rect(
                                0,
                                0,
                                Registry.real_window_width,
                                90)

                            pygame.draw.rect(
                                Registry.display,
                                Registry.background_color,
                                cover_Rect)

                            returned_text = text_utils.text_formatter.format_text(
                                "Pycraft",
                                ("center", 0+IntroYDisplacement),
                                Registry.title_font,
                                Registry.title_backup_font)

                            title_width = returned_text.get_width()

                            text_utils.text_formatter.format_text(
                                "Credits",
                                (((Registry.real_window_width-title_width)/2)+65, 50),
                                Registry.subtitle_font,
                                Registry.subtitle_backup_font,
                                font_color=Registry.secondary_font_color)

                            VisualYdisplacement -= 60/(Registry.average_fps/Registry.iteration)
                            LoadText = True
                            if Ypos+VisualYdisplacement <= Registry.real_window_height/2:
                                Holdon_exit = True
                                Holdtimer += 1/(Registry.average_fps/Registry.iteration)
                                if Holdtimer >= 5:
                                    Registry.go_to = "home"
                        else:
                            cover_Rect = pygame.Rect(
                                0,
                                0,
                                Registry.real_window_width,
                                90)

                            pygame.draw.rect(
                                Registry.display,
                                Registry.background_color,
                                cover_Rect)

                            returned_text = text_utils.text_formatter.format_text(
                                "Pycraft",
                                ("center", 0+IntroYDisplacement),
                                Registry.title_font,
                                Registry.title_backup_font)

                            title_width = returned_text.get_width()

                            text_utils.text_formatter.format_text(
                                "Credits",
                                (((Registry.real_window_width-title_width)/2)+65, 50+IntroYDisplacement),
                                Registry.subtitle_font,
                                Registry.subtitle_backup_font,
                                font_color=Registry.secondary_font_color)

                            IntroYDisplacement -= 90/(Registry.average_fps/Registry.iteration)
                            VisualYdisplacement = Registry.real_window_height

                    drawing_utils.generate_graph.create_devmode_graph()

                    if Registry.go_to is None:
                        display_utils.display_animations.fade_in()
                            
                    else:
                        display_utils.display_animations.fade_out()

                    if Registry.startup_animation is False and (Registry.go_to is not None):
                        return None

                    target_fps = display_utils.display_utils.get_play_status()

                    pygame.display.flip()
                    Registry.clock.tick(target_fps)

                    Registry.run_timer += time.perf_counter()-start_time
                    
            except Exception as Message:
                error_message = "credits > generate_credits > credits: "+str(Message)
                
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
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
