if __name__ != "__main__":
    try:
        import traceback
        import json
        import time
        import datetime

        import pygame
        from PIL import ImageGrab

        from registry_utils import Registry
        
        import error_utils
        import display_utils
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
            
    class access_other_guis(Registry):
        def __init__(self):
            pass

        def access_gui(
                load_inventory,
                load_map,
                start_inventory,
                start_map,
                camera):
            
            try:
                if load_inventory:
                    '''save_information = {}
                    for key in Registry.default_save_config:
                        if key == "time":
                            iso_time = datetime.datetime.now()
            
                            iso_day = f"{iso_time.day: 03d}".strip()
                            iso_month = f"{iso_time.month: 03d}".strip()
                            iso_year = iso_time.year
                            
                            iso_hour = f"{iso_time.hour: 03d}".strip()
                            iso_minute = f"{iso_time.minute: 03d}".strip()
                            iso_second = f"{iso_time.second: 03d}".strip()
                            formatted_iso_time = f"{iso_day}/{iso_month}/{iso_year} at {iso_hour}:{iso_minute}:{iso_second}"
                            
                            save_information[key] = formatted_iso_time
                            
                        elif key == "priority":
                            save_priority = int(f"{iso_year}{iso_month}{iso_day}{iso_hour}{iso_minute}{iso_second}")
                            save_information[key] = save_priority
                            
                        elif key == "position":
                            save_information[key] = [*camera.position]
                            
                        elif key == "rotation":
                            save_information[key] = [camera.yaw, camera.pitch]
                            
                        else:
                            save_information[key] = Registry.__dict__[key]
                            
                    with open(Registry.base_folder / "temporary" / "game_states.json", "w") as file:
                        json.dump(save_information, file)'''
                    
                    if Registry.use_transparency_effects:
                        bbox = (
                            *display_utils.display_utils.get_display_location(),
                            *pygame.display.get_window_size())

                        image = ImageGrab.grab(bbox)

                        pause_image_path = Registry.base_folder / "resources" / "general resources" / "PauseIMG.png"
                    
                        image.save(pause_image_path)

                    pygame.event.set_grab(False)
                    pygame.mouse.set_visible(True)
                    
                    start_inventory.set()
                    
                    while start_inventory.is_set():
                        pygame.event.poll()
                        time.sleep(1)

                    if Registry.sound:
                        sound_utils.play_sound.play_click_sound()
                    
                    load_inventory = False

                    pygame.event.set_grab(True)
                    pygame.mouse.set_visible(False)

                elif load_map:
                    pygame.event.set_grab(False)
                    pygame.mouse.set_visible(True)

                    start_map.set()

                    while start_map.is_set():
                        pygame.event.poll()
                        time.sleep(1)

                    if Registry.sound:
                        sound_utils.play_sound.play_click_sound()
                    
                    load_map = False

                    pygame.event.set_grab(True)
                    pygame.mouse.set_visible(False)


                return load_inventory, load_map
                
            except Exception as Message:
                error_message = "".join(("GameEngineUtils > access_other_guis ",
                                                        f"> access_gui: {str(Message)}"))

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