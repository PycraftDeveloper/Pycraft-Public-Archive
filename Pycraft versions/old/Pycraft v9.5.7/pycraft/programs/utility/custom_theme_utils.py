if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import sound_utils
        import theme_utils
        import translation_utils
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
        def __init__(self):
            pass

        def draw_custom_theme_options(
                button_pos,
                font,
                backup_font,
                hovering,
                mouse_over,
                scrollbar_needed,
                custom_theme_choice,
                display_events):

            if (Registry.language == "ar" or
                    Registry.language == "hy" or
                    Registry.language == "zh-tw" or
                    Registry.language == "zh-cn" or
                    Registry.language == "ka" or
                    Registry.language == "el" or
                    Registry.language == "hi" or
                    Registry.language == "he" or
                    Registry.language == "iw" or
                    Registry.language == "ja" or
                    Registry.language == "kk" or
                    Registry.language == "km" or
                    Registry.language == "ko" or
                    Registry.language == "mn" or
                    Registry.language == "my" or
                    Registry.language == "ne" or
                    Registry.language == "ps" or
                    Registry.language == "ru" or
                    Registry.language == "ta" or
                    Registry.language == "th" or
                    Registry.language == "uk" or
                    Registry.language == "ur"):
                font = backup_font
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                button_pos]

            total_height = 0

            button_text_array = []
            for key in Registry.custom_theme:
                formatted_key = key.replace("_", " ")
                formatted_color = f"({str(Registry.custom_theme[key])[1:-1]})"
                option = f"{formatted_key}: "
                details = [option, formatted_color]
                button_text_array.append(details)

            for i in range(len(button_text_array)):
                if custom_theme_choice == list(Registry.custom_theme)[i]:
                    index = 0
                    string = str(Registry.custom_theme[list(Registry.custom_theme)[i]])[1:-1]
                    for event in Registry.display_events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                if len(string) == 0:
                                    theme_utils.determine_theme_colours.get_colors(
                                        "custom")

                                    default_custom_theme = {
                                        "font_color": Registry.font_color,
                                        "background_color": Registry.background_color,
                                        "shape_color": Registry.shape_color,
                                        "accent_color": Registry.accent_color,
                                        "secondary_font_color": Registry.secondary_font_color}
            
                                    string = str(default_custom_theme[list(Registry.custom_theme)[i]])[1:-1]
                                else:
                                    string = string[:-1]
                            else:
                                try:
                                    converted = chr(event.key)
                                except:
                                    pass
                                else:
                                    if ord(converted) >= 32 and ord(converted) <= 126:
                                        string += converted
                                
                            del display_events[index]

                        index += 1

                    Registry.custom_theme[list(Registry.custom_theme)[i]] = f"[{string}]"

                    button_text_array = []
                    for key in Registry.custom_theme:
                        formatted_key = key.replace("_", " ")
                        formatted_color = f"({str(Registry.custom_theme[key])[1:-1]})"
                        option = f"{formatted_key}: "
                        details = [option, formatted_color]
                        button_text_array.append(details)
                                
                translated_output = translation_utils.string_translator.change_language(
                        button_text_array[i][0])
                
                returned_text = font.render(
                    translated_output + button_text_array[i][1],
                    Registry.aa,
                    Registry.font_color)

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

                        if custom_theme_choice == list(Registry.custom_theme)[i]:
                            custom_theme_choice = None
                        else:
                            custom_theme_choice = list(Registry.custom_theme)[i]
                            
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

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                else:
                    if custom_theme_choice == list(Registry.custom_theme)[i]:
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

                position[1] += button_text_height + 3
                total_height += button_text_height

            return (total_height + 20,
                hovering,
                mouse_over,
                custom_theme_choice)

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
