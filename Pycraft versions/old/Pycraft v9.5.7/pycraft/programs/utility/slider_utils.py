if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
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

        def draw_slider(
                slider_pos,
                minimum,
                maximum,
                value,
                argument_variable,
                hovering,
                mouse_over,
                scrollbar_needed):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            if (argument_variable == "music_volume" and
                    Registry.music is False):

                enable = False

            elif (argument_variable == "sound_volume" and
                    Registry.sound is False):

                enable = False

            elif (argument_variable == "fps" and
                    Registry.vsync):

                enable = False

            else:
                enable = True

            position = [
                scroll_x_offset,
                slider_pos]

            height = 10
            slider_range = maximum - minimum
            length = Registry.real_window_width/2

            rect = pygame.Rect(
                position[0],
                position[1],
                length,
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

            circle_pos_x = ((value - minimum) /
                            (slider_range / length)) + scroll_x_offset
            circle_pos_y = position[1] + height/2
            circle_pos = (circle_pos_x, circle_pos_y)

            if (Registry.mouse_x > position[0] and
                    Registry.mouse_x < length and
                    Registry.mouse_y > position[1] - 15 and
                    Registry.mouse_y < position[1] + height + 15 and
                    enable):

                hovering = True
                mouse_over = True

                if Registry.primary_mouse_button_down:
                    pygame.event.set_blocked(
                        pygame.MOUSEMOTION)
                    
                    Registry.__dict__[argument_variable] = (
                        (slider_range / length) * Registry.mouse_x) + minimum
                    
                    new_value = ((slider_range/length) * Registry.mouse_x) + minimum
                    
                    setattr(Registry, argument_variable, new_value)

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
                    pygame.event.set_allowed(
                        pygame.MOUSEMOTION)

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
