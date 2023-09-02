if __name__ != "__main__":
    try:
        import os
        import time
        import traceback

        import pygame
        
        from registry_utils import Registry
        
        import caption_utils
        import display_utils
        import drawing_utils
        import error_utils
        import text_utils
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
            
    class generate_character_designer(Registry):
        def character_designer_gui():
            try:
                caption_utils.generate_captions.get_normal_caption(
                    "Character Designer")

                title_width = 0

                while True:
                    start_time = time.perf_counter()

                    if not (Registry.error_message is None or Registry.error_message_detailed is None):
                        error_utils.generate_error_screen.error_screen(
                            Registry.error_message,
                            Registry.error_message_detailed)

                    display_utils.display_functionality.core_display_functions()

                    caption_utils.generate_captions.get_normal_caption(
                        "Character Designer")

                    Registry.display.fill(Registry.background_color)

                    cover_Rect = pygame.Rect(
                        0,
                        0,
                        1280,
                        90)

                    pygame.draw.rect(
                        Registry.display,
                        Registry.background_color,
                        cover_Rect)

                    returned_text = text_utils.text_formatter.format_text(
                        "Pycraft",
                        ("center", "top"),
                        Registry.title_font,
                        Registry.title_backup_font)

                    title_width = returned_text.get_width()

                    text_utils.text_formatter.format_text(
                        "Character Designer",
                        (((Registry.real_window_width-title_width)/2)+55, 50),
                        Registry.subtitle_font,
                        Registry.subtitle_backup_font,
                        font_color=Registry.secondary_font_color)

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
                error_message = "".join(("character_designer > ",
                                             "generate_character_designer > ",
                                             f"character_designer: {str(Message)}"))

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
