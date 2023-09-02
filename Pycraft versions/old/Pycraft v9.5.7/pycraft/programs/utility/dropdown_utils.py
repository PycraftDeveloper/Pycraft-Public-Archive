if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import sound_utils
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
        def __init__(self):
            pass

        def draw_dropdown(
                dropdown_scroll,
                button_pos,
                font,
                backup_font,
                argument_variable,
                hovering,
                dropdown_hovering,
                mouse_over,
                scrollbar_needed,
                content,
                enabled):

            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0

            position = [
                scroll_x_offset,
                button_pos]

            rect_position = [*position]

            rendered_text_array = []
            text_height_array = []
            text_width_array = []
            text_array = []

            value = Registry.__dict__[argument_variable]

            current = content[value].capitalize()

            menu_content = []
            
            for key in content:
                menu_content.append(content[key].capitalize())

                returned_text = text_utils.text_formatter.format_text(
                    content[key].capitalize(),
                    ("left", "top"),
                    font,
                    backup_font,
                    blit=False)
                        
                rendered_text_array.append(returned_text)
                text_height_array.append(returned_text.get_height())
                text_width_array.append(returned_text.get_width())
                text_array.append(content[key])

            max_width = max(text_width_array)*1.5

            if max_width > Registry.real_window_width/2:
                max_width = Registry.real_window_width/2

            additional = 0

            item = menu_content.index(current) - dropdown_scroll

            while item + 7 > len(menu_content):
                item -= 1

            while item + 7 < 0:
                item += 1

            current_menu_height = 0
            for item in range(item, item+7):
                rect_position[1] += text_height_array[item]
                current_menu_height += text_height_array[item]

            avg_text_height = sum(text_height_array) / len(text_height_array)

            slider_y_pos = (((current_menu_height / (sum(text_height_array))) * (current_menu_height - (dropdown_scroll * avg_text_height))) + position[1])+10
            if slider_y_pos < button_pos:
                slider_y_pos = button_pos

            slider_height = sum(text_height_array) / current_menu_height
            if slider_height < 10:
                slider_height = 10

            if scroll_x_offset == 0:
                slider_x_offset = 2
            else:
                slider_x_offset = scroll_x_offset
                
            slider_rect = pygame.Rect(
                slider_x_offset,
                slider_y_pos,
                3,
                slider_height)

            pygame.draw.rect(Registry.display, Registry.shape_color, slider_rect, border_radius=2)

            position[0] += 7
            scroll_x_offset += 7

            additional = 0
            height = 10
            dropdown_hovering = False
            hovering = False
            
            item = menu_content.index(current) - dropdown_scroll

            while item + 7 > len(menu_content):
                item -= 1
                dropdown_scroll += 1

            while item + 7 < 0:
                item += 1
                dropdown_scroll -= 1

            result = Registry.__dict__[argument_variable]
                
            for item in range(item, item+7):
                if Registry.use_mouse_input:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]

                hovering = False
                            
                if (mouse_x > scroll_x_offset and
                        mouse_x < max_width and
                        mouse_y > position[1] and
                        mouse_y < position[1]+text_height_array[item] and
                        enabled):

                    hovering = True
                    dropdown_hovering = True

                    if Registry.primary_mouse_button_down:
                        if (argument_variable == "language" and
                                list(content.keys())[list(content.values()).index(text_array[item])] != Registry.__dict__[argument_variable]):

                            translated_text = {}
                            
                        pygame.mouse.set_pos(
                            scroll_x_offset+max_width+10,
                            position[1])
                        
                        Registry.primary_mouse_button_down = False
                        result = list(content.keys())[list(content.values()).index(text_array[item])]
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                if menu_content[item] == current:
                    if hovering:
                        color = Registry.font_color
                    else:
                        color = Registry.accent_color
                        
                    outline_rect = pygame.Rect(scroll_x_offset, position[1], scroll_x_offset+max_width, text_height_array[item])
                    pygame.draw.rect(Registry.display, color, outline_rect, border_radius=10, width=1)
                    Registry.display.blit(rendered_text_array[item], (position[0]+10, position[1]))
                    position[1] += text_height_array[item]
                    height += text_height_array[item]
                    additional += 1

                else:
                    if hovering:
                        color = Registry.font_color
                    else:
                        color = Registry.shape_color
                        
                    outline_rect = pygame.Rect(scroll_x_offset, position[1], max_width, text_height_array[item])
                    pygame.draw.rect(Registry.display, color, outline_rect, border_radius=10, width=1)
                    Registry.display.blit(rendered_text_array[item], (position[0]+10, position[1]))
                    position[1] += text_height_array[item]
                    height += text_height_array[item]
                    additional += 1

            mouse_over = dropdown_hovering

            setattr(
                Registry,
                argument_variable,
                result)
            
            return (
                (rect_position[1]-button_pos) + 20,
                hovering,
                mouse_over,
                dropdown_hovering,
                dropdown_scroll)

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
