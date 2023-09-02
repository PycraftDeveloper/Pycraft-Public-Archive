if __name__ != "__main__":
    try:
        import traceback

        import pygame
        
        from registry_utils import Registry
        
        import caption_utils
        import display_utils
        import error_utils
        import sound_utils
        import theme_utils
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
            
    class create_theme_selection_menu(Registry):
        def __init__(self):
            pass
        
        def get_theme_gui():
            try:
                Registry.primary_mouse_button_down = False

                Registry.mouse_x = Registry.real_window_width/2
                Registry.mouse_y = Registry.real_window_height/2

                while True:
                    display_utils.display_functionality.core_display_functions(
                        location="saveANDexit")

                    caption_utils.generate_captions.get_normal_caption(
                        "Theme selector")

                    LightRect = pygame.Rect(
                        0,
                        100,
                        Registry.real_window_width/2,
                        Registry.real_window_height-200)

                    DarkRect = pygame.Rect(
                        Registry.real_window_width/2,
                        100,
                        Registry.real_window_width/2,
                        Registry.real_window_height-200)

                    Registry.display.fill(Registry.background_color)

                    text_utils.text_formatter.format_text(
                        "Pycraft",
                        ("center", "top"),
                        Registry.title_font,
                        Registry.title_backup_font,)

                    Registry.theme = "light"
                    
                    theme_utils.determine_theme_colours.get_colors()

                    pygame.draw.rect(
                        Registry.display,
                        Registry.background_color,
                        LightRect)

                    pygame.draw.rect(
                        Registry.display,
                        Registry.shape_color,
                        LightRect,
                        3)

                    LightModeFont = text_utils.text_formatter.format_text(
                        "Light",
                        ("center", "top"),
                        Registry.option_font,
                        Registry.option_backup_font,
                        blit=False)
                    LightModeFont_Width = LightModeFont.get_width()
                    LightModeFont_Height = LightModeFont.get_height()

                    Registry.display.blit(
                        LightModeFont,
                        (((Registry.real_window_width/2)-LightModeFont_Width)/2,
                            (Registry.real_window_height-LightModeFont_Height)/2))

                    Registry.theme = "dark"
                    
                    theme_utils.determine_theme_colours.get_colors()

                    pygame.draw.rect(
                        Registry.display,
                        Registry.background_color,
                        DarkRect)

                    pygame.draw.rect(
                        Registry.display,
                        Registry.shape_color,
                        DarkRect,
                        3)

                    DarkModeFont = text_utils.text_formatter.format_text(
                        "Dark",
                        ("center", "top"),
                        Registry.option_font,
                        Registry.option_backup_font,
                        blit=False)
                    DarkModeFont_Width = DarkModeFont.get_width()
                    DarkModeFont_Height = DarkModeFont.get_height()

                    Registry.display.blit(
                        DarkModeFont,
                        (((Registry.real_window_width+(Registry.real_window_width/2))-DarkModeFont_Width)/2,
                            (Registry.real_window_height-DarkModeFont_Height)/2))

                    if Registry.mouse_y >= 100 and Registry.mouse_y <= Registry.real_window_height-100:
                        if Registry.mouse_x <= Registry.real_window_width/2:
                            pygame.draw.rect(
                                Registry.display,
                                Registry.accent_color,
                                LightRect,
                                1)

                            Registry.theme = "light"

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                break

                        elif Registry.mouse_x >= Registry.real_window_width/2:
                            pygame.draw.rect(
                                Registry.display,
                                Registry.accent_color,
                                DarkRect,
                                1)

                            Registry.theme = "dark"
                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
 
                                break

                        theme_utils.determine_theme_colours.get_colors()

                    Choice = text_utils.text_formatter.format_text(
                        f"You have selected the {Registry.theme} theme, you can change this later in settings",
                        ("center", "top"),
                        Registry.large_content_font,
                        Registry.large_content_backup_font,
                        blit=False)
                    ChoiceWidth = Choice.get_width()
                    choice_height = Choice.get_height()

                    Registry.display.blit(
                        Choice,
                        ((Registry.real_window_width-ChoiceWidth)/2,
                            (Registry.real_window_height-choice_height)))

                    pygame.display.update()
                    Registry.clock.tick(Registry.fps)
                    
            except Exception as Message:
                error_message = "".join(("theme_gui > create_theme_selection_menu ",
                                             f"> get_theme_gui: {str(Message)}"))

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
