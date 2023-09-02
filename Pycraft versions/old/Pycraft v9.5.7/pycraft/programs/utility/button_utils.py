if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import sound_utils
        import setting_preset_utils
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
            
    class draw_setting_elements(Registry):
        """
        This class is in charge of rendering the button element
        that you can see used in the settings menu for Pycraft.
        
        Please note that the use of 'self' in this module is
        purely as a way to make changes to variables in Pycraft,
        and is not/should not be used in any other way for
        simplicity.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def draw_multi_buttons(
                button_pos,
                button_text_array,
                font,
                backup_font,
                argument_variable,
                hovering,
                mouse_over,
                scrollbar_needed):

            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                button_pos]

            for i in range(len(button_text_array)):
                returned_text = text_utils.text_formatter.format_text(
                    button_text_array[i],
                    ("left", "top"),
                    font,
                    backup_font,
                    blit=False)

                button_text_width = returned_text.get_width() + 20
                button_text_height = returned_text.get_height() + 20

                rect = pygame.Rect(
                    position[0],
                    position[1],
                    button_text_width,
                    button_text_height)

                if (Registry.mouse_x > position[0] and
                        Registry.mouse_x < position[0] + button_text_width and
                        Registry.mouse_y > position[1] and
                        Registry.mouse_y < position[1] + button_text_height):

                    hovering = True
                    mouse_over = True

                    if Registry.primary_mouse_button_down:
                        Registry.primary_mouse_button_down = False

                        if Registry.use_mouse_input is False:
                            Registry.mouse_y = button_pos + 5 + button_text_height

                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)
                        
                        updated_argument = Registry.__dict__[argument_variable]
                        
                        updated_argument[button_text_array[i]] = not updated_argument[button_text_array[i]]
                        setattr(Registry, argument_variable, updated_argument)

                        theme_utils.determine_theme_colours.get_colors()

                        setting_preset_utils.presets.update_profile()

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                else:
                    if Registry.__dict__[argument_variable][button_text_array[i]]:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                Registry.display.blit(
                    returned_text,
                    (position[0]+10,
                        position[1]+10))

                position[0] += button_text_width + 3

            return (button_text_height + 20,
                hovering,
                mouse_over)

        def draw_buttons(
                button_pos,
                button_text_array,
                font,
                backup_font,
                value,
                argument_variable,
                hovering,
                mouse_over,
                files_to_remove,
                clear_languages,
                scanned_files,
                scrollbar_needed):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            if (argument_variable == "aa_quality" and
                    Registry.aa is False):

                enable = False

            elif (argument_variable == "clear_cache" and
                        (files_to_remove is False or
                            Registry.remove_file_permission is False)):

                enable = False

            elif (argument_variable == "clear_languages_cache" and
                        (clear_languages is False or
                            Registry.remove_file_permission is False)):

                enable = False

            elif (argument_variable == "scan_pycraft" and
                    scanned_files):

                enable = False

            else:
                enable = True
                
            position = [
                scroll_x_offset,
                button_pos]

            for i in range(len(button_text_array)):
                if enable:
                    returned_text = text_utils.text_formatter.format_text(
                        button_text_array[i],
                        ("left", "top"),
                        font,
                        backup_font,
                        blit=False,
                        font_color=Registry.font_color)
                    
                else:
                    returned_text = text_utils.text_formatter.format_text(
                        button_text_array[i],
                        ("left", "top"),
                        font,
                        backup_font,
                        blit=False,
                        font_color=Registry.shape_color)

                button_text_width = returned_text.get_width() + 20
                button_text_height = returned_text.get_height() + 20

                rect = pygame.Rect(
                    position[0],
                    position[1],
                    button_text_width,
                    button_text_height)
                
                pygame.draw.rect(
                    Registry.display,
                    Registry.background_color,
                    rect,
                    border_radius=10)

                if (Registry.mouse_x > position[0] and
                    Registry.mouse_x < position[0] + button_text_width and
                    Registry.mouse_y > position[1] and
                    Registry.mouse_y < position[1] + button_text_height and
                        enable):

                    hovering = True
                    mouse_over = True

                    if Registry.primary_mouse_button_down:
                        Registry.primary_mouse_button_down = False

                        if Registry.use_mouse_input is False:
                            mouse_y = button_pos + 5 + button_text_height

                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)
                        
                        setattr(Registry, argument_variable, button_text_array[i])

                        theme_utils.determine_theme_colours.get_colors()

                        setting_preset_utils.presets.update_profile()

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                else:
                    if button_text_array[i] == value:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                Registry.display.blit(
                    returned_text,
                    (position[0]+10,
                        position[1]+10))

                position[0] += button_text_width + 3

            return (button_text_height + 20,
                hovering,
                mouse_over)

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
