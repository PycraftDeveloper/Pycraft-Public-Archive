if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
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

        def create_information_message(
                font,
                backup_font,
                text,
                saved_y_position,
                max_x,
                info_offset):
            
            position = ((Registry.real_window_width/2) + 40,
                        (saved_y_position + 10) - info_offset)
            
            width = Registry.real_window_width - (max_x + 43)

            info_text_height = text_utils.text_wrap.blit_text(
                    text,
                    position,
                    font,
                    backup_font,
                    width)

            rect = pygame.Rect(
                position[0] - 10,
                position[1] - 10,
                (width - position[0]) + 20,
                info_text_height + 20)

            pygame.draw.rect(
                Registry.display,
                Registry.font_color,
                rect,
                width=1,
                border_radius=10)

            max_y_value = position[1] + info_text_height + info_offset + 20
            if max_y_value > Registry.real_window_height:
                info_offset = (max_y_value - Registry.real_window_height) + 10

            else:
                info_offset = 0

            return info_offset

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
