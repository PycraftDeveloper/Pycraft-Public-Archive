if __name__ != "_main_":
    try:
        import traceback
        import os
        import threading
        import time
        
        import pygame
        
        from registry_utils import Registry
        
        import theme_utils
        import display_utils
        import error_utils
        import pycraft_startup_utils
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
            
    class generate_startup_gui(Registry):
        def startup_gui():
            try:
                if Registry.theme is False:
                    Registry.theme = "dark"
                    update_theme_later = True
                    
                else:
                    update_theme_later = False

                theme_utils.determine_theme_colours.get_colors()

                if update_theme_later:
                    Registry.theme = False

                font_path = Registry.base_folder / "fonts" / "Book Antiqua.ttf"
                
                NameFont = pygame.font.Font(
                    font_path,
                    45)

                NameText = NameFont.render(
                    "PycraftDev",
                    True,
                    Registry.font_color)
                NameTextWidth = NameText.get_width()
                NameTextHeight = NameText.get_height()

                Registry.real_window_width = pygame.display.get_window_size()[0]
                Registry.real_window_height = pygame.display.get_window_size()[1]

                Registry.display.fill(Registry.background_color)
                
                pygame.display.flip()
                pygame.display.set_caption(f"Pycraft: v{Registry.version}: Welcome")

                PresentsText = Registry.subtitle_font.render(
                    "presents",
                    True,
                    Registry.font_color)

                presentOffSet = 39

                PycraftText = Registry.title_font.render(
                    "Pycraft",
                    True,
                    Registry.font_color)
                TitleTextWidth = PycraftText.get_width()

                PycraftstartPos = pygame.Vector2(
                    ((Registry.real_window_width-TitleTextWidth)/2,
                        Registry.real_window_height/2 - NameTextHeight))

                PycraftEndPos = pygame.Vector2(
                    PycraftstartPos.x,
                    0)

                Registry.clock = pygame.time.Clock()

                InterpolateSpeed = 0.02

                timer = 2

                while timer > 0 and Registry.run_full_startup:
                    display_utils.display_functionality.core_display_functions(
                        location="exit",
                        resize=False)

                    Registry.display.fill(Registry.background_color)
                    
                    timer -= 0.01

                    Registry.display.blit(
                        NameText,
                        ((Registry.real_window_width-NameTextWidth)/2,
                            Registry.real_window_height/2 - NameTextHeight))

                    if timer <= 1:
                        Registry.display.blit(
                            PresentsText,
                            ((Registry.real_window_width-NameTextWidth)/2 + presentOffSet,
                                Registry.real_window_height/2 + NameTextHeight - 77))

                    pygame.display.flip()
                    Registry.clock.tick(60)

                Thread_ResourceCheck = threading.Thread(
                    target=pycraft_startup_utils.startup_test.pycraft_resource_test,
                    args=(False,))
                Thread_ResourceCheck.name = "Thread_ResourceCheck"
                Thread_ResourceCheck.start()

                runtimer = 0

                while True:
                    display_utils.display_functionality.core_display_functions(
                        location="exit",
                        resize=False)

                    RefreshTime = time.perf_counter()

                    Registry.display.fill(Registry.background_color)

                    if "Thread_ResourceCheck" not in str(threading.enumerate()):
                        if not (Registry.error_message is None or
                                    Registry.error_message_detailed is None):
                            
                            error_utils.generate_error_screen.error_screen()
                            
                        PycraftstartPos = pygame.math.Vector2.lerp(
                            PycraftstartPos,
                            PycraftEndPos,
                            InterpolateSpeed)

                    Registry.display.blit(
                        PycraftText,
                        (PycraftstartPos.x, PycraftstartPos.y))

                    pygame.display.flip()
                    Registry.clock.tick(60)

                    if PycraftstartPos.y <= 1:
                        PycraftstartPos = PycraftEndPos
                        Registry.run_full_startup = False
                        break

                    runtimer += time.perf_counter()-RefreshTime

            except Exception as Message:
                error_message = "".join(("startupAnimation > generate_startup_gui ",
                                             f"> start: {str(Message)}"))

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
