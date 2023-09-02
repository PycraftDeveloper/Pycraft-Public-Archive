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

        def draw_directory_structure(
                slider_pos,
                font,
                backup_font,
                hovering,
                mouse_over,
                hover_id,
                hovering_over_key,
                scrollbar_needed):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                slider_pos]

            height = 23
            total_height = height
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

            x_pos = 0
            hover_area = False
            for key in Registry.file_structure:
                width = ((Registry.real_window_width/2)/Registry.folder_size) * Registry.file_structure[key]["size"]

                if ((Registry.mouse_x > position[0] + x_pos and
                            Registry.mouse_x < position[0] + x_pos + width and
                            Registry.mouse_y > position[1] and
                            Registry.mouse_y < position[1] + height) or
                        hover_id == Registry.file_structure[key]):

                    hovering = True
                    mouse_over = True

                    if hover_id != Registry.file_structure[key]:
                        hover_id = Registry.file_structure[key]
                        hover_area = True
                
                inside_rect = pygame.Rect(
                    position[0] + x_pos,
                    position[1],
                    width,
                    height)

                if hover_id is not None:
                    if hover_id == Registry.file_structure[key]:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.file_structure[key]["color"],
                            inside_rect)
                        
                else:
                    pygame.draw.rect(
                        Registry.display,
                        Registry.file_structure[key]["color"],
                        inside_rect)

                x_pos += width

            pygame.draw.rect(
                Registry.display,
                Registry.background_color,
                rect,
                width=3,
                border_radius=10)

            padding_rect = pygame.Rect(
                position[0]-10,
                position[1]-10,
                length+20,
                height+20)

            pygame.draw.rect(
                Registry.display,
                Registry.background_color,
                padding_rect,
                width=10,
                border_radius=20)

            total_height += 20

            text_position = [scroll_x_offset, slider_pos + height + 20]

            text_max_height = 0

            hover_text = False
            for key in Registry.file_structure:
                percentage = (100/Registry.folder_size) * Registry.file_structure[key]["size"]
                    
                if (hover_id is not None or
                        hovering_over_key):

                    returned_text = text_utils.text_formatter.format_text(
                        f"{str(key)}: {int(percentage)}%",
                        text_position,
                        font,
                        backup_font,
                        blit=False)

                else:
                    returned_text = text_utils.text_formatter.format_text(
                        f"{str(key)}: {int(percentage)}%",
                        text_position,
                        font,
                        backup_font,
                        blit=False,
                        font_color=Registry.file_structure[key]["color"])
                    
                text_width = returned_text.get_width()
                text_height = returned_text.get_height()

                if text_position[0] + text_width > (Registry.real_window_width / 2):
                    text_position[0] = scroll_x_offset
                    text_position[1] += text_height + 20
                    total_height += text_height + 20

                if ((Registry.mouse_x > text_position[0] - 10 and
                            Registry.mouse_x < text_position[0] + text_width + 10 and
                            Registry.mouse_y > text_position[1] - 10 and
                            Registry.mouse_y < text_position[1] + text_height + 10) or
                        hover_id == Registry.file_structure[key]):

                    hovering = True
                    hovering_over_key = True
                    mouse_over = True

                    returned_text = text_utils.text_formatter.format_text(
                        f"{str(key)}: {int(percentage)}%",
                        text_position,
                        font,
                        backup_font,
                        blit=False,
                        font_color=Registry.file_structure[key]["color"],)
                    
                    if hover_id != Registry.file_structure[key]:
                        hover_id = Registry.file_structure[key]
                        hover_text = True
                
                if text_height > text_max_height:
                    text_max_height = text_height
                    
                Registry.display.blit(returned_text, text_position)
                text_position[0] += text_width + 20

            if hover_area is False and hover_text is False:
                hover_id = None

            if (Registry.mouse_x > position[0] and
                    Registry.mouse_x < length and
                    Registry.mouse_y > position[1] - 15 and
                    Registry.mouse_y < position[1] + height + 15):

                hovering = True
                mouse_over = True

                pygame.event.set_allowed(
                    pygame.MOUSEMOTION)

                pygame.draw.rect(
                    Registry.display,
                    Registry.font_color,
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

            total_height += text_height + 40

            return total_height, hovering, mouse_over, hover_id

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
