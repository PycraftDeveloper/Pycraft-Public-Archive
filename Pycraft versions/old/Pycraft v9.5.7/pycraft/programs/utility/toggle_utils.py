if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import sound_utils
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

        def draw_toggle(
                toggle_pos,
                value_0,
                value_1,
                value,
                argument_variable,
                hovering,
                mouse_over,
                scrollbar_needed,
                enabled):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [scroll_x_offset, toggle_pos]
                
            height = 10

            rect = pygame.Rect(
                position[0],
                position[1],
                36,
                height)

            pygame.draw.rect(
                Registry.display,
                Registry.shape_color,
                rect,
                border_radius=10)

            pygame.draw.rect(
                Registry.display,
                Registry.background_color,
                rect,
                width=3,
                border_radius=10)

            if argument_variable == "dont_use_set_resolution":
                data = value
                value = not data

            if value == value_0:
                toggle_value = 30 + scroll_x_offset
                    
            if value == value_1:
                toggle_value = 10 + scroll_x_offset

            circle_pos_x = toggle_value
            circle_pos_y = position[1] + height/2
            circle_pos = (circle_pos_x, circle_pos_y)

            if Registry.music is False:
                pygame.mixer.music.fadeout(500)

            if (Registry.mouse_x > position[0] and
                    Registry.mouse_x < 36 + 20 and
                    Registry.mouse_y > position[1] - 15 and
                    Registry.mouse_y < position[1] + height + 15 and
                    enabled):

                hovering = True
                mouse_over = True

                if Registry.primary_mouse_button_down:
                    Registry.primary_mouse_button_down = False
                    
                    setattr(
                        Registry,
                        argument_variable,
                        not Registry.__dict__[argument_variable])

                    if Registry.use_mouse_input is False:
                        Registry.mouse_x += 36

                    if Registry.sound:
                        sound_utils.play_sound.play_click_sound()

                else:
                    pygame.draw.rect(
                        Registry.display,
                        Registry.font_color,
                        rect,
                        width=1,
                        border_radius=10)

                    pygame.draw.circle(
                        Registry.display,
                        Registry.font_color,
                        circle_pos,
                        radius=10)

                    pygame.draw.circle(
                        Registry.display,
                        Registry.background_color,
                        circle_pos,
                        radius=6)

            else:
                if value:
                    pygame.draw.rect(
                        Registry.display,
                        Registry.accent_color,
                        rect,
                        width=1,
                        border_radius=10)

                    pygame.draw.circle(
                        Registry.display,
                        Registry.accent_color,
                        circle_pos,
                        radius=10)
                    pygame.draw.circle(
                        Registry.display,
                        Registry.background_color,
                        circle_pos,
                        radius=6)

                else:
                    pygame.draw.rect(
                        Registry.display,
                        Registry.shape_color,
                        rect,
                        width=1,
                        border_radius=10)

                    pygame.draw.circle(
                        Registry.display,
                        Registry.shape_color,
                        circle_pos,
                        radius=10)

                    pygame.draw.circle(
                        Registry.display,
                        Registry.background_color,
                        circle_pos,
                        radius=6)

            return height + 20, hovering, mouse_over
        
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
