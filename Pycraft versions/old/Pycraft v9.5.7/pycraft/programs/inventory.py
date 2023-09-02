if __name__ != "__main__":
    try:
        import sys
        import os
        import traceback
        import pathlib
        
        import pygame
        import pyautogui
        from PIL import Image

        from registry_utils import Registry
        
        import sound_utils
        import display_utils
        import image_utils
        import caption_utils
        import error_utils
        import file_utils
        import tkinter_utils
        import text_utils
        import button_utils
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
            
    class generate_inventory(Registry): 
        def __init__(dictionary):
            for key in dictionary:
                setattr(Registry, key, dictionary[key])
                
            pygame.init()

        def inventory_gui(
                start_inventory,
                dictionary):
            
            try:
                generate_inventory.__init__(dictionary)
                
                Registry.input_key = file_utils.pycraft_config_utils.read_input_key()
                
                font_path = Registry.base_folder / "fonts" / "Book Antiqua.ttf"
                backup_font_path = Registry.base_folder / "fonts" / "NotoSans-Regular.ttf"
                Registry.icon_path = Registry.base_folder / "resources" / "general resources" / "Icon.png"

                Registry.title_font = pygame.font.Font(
                    font_path,
                    60)

                Registry.subtitle_font = pygame.font.Font(
                    font_path,
                    35)

                Registry.option_font = pygame.font.Font(
                    font_path,
                    30)

                Registry.large_content_font = pygame.font.Font(
                    font_path,
                    20)

                Registry.small_content_font = pygame.font.Font(
                    font_path,
                    15)

                Registry.title_backup_font = pygame.font.Font(
                    backup_font_path,
                    60)

                Registry.subtitle_backup_font = pygame.font.Font(
                    backup_font_path,
                    35)

                Registry.option_backup_font = pygame.font.Font(
                    backup_font_path,
                    30)

                Registry.large_content_backup_font = pygame.font.Font(
                    backup_font_path,
                    20)

                Registry.small_content_backup_font = pygame.font.Font(
                    backup_font_path,
                    15)
        
                Registry.window_icon = pygame.image.load(Registry.icon_path)
                
                selector_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"
                selector = pygame.image.load(selector_path)
                selector.set_colorkey(Registry.background_color)
                selector_width = selector.get_width()
                
                selection = "Weapons"

                hover1 = False
                hover2 = False
                hover3 = False
                hover4 = False
                hover5 = False
                hover6 = False
                hover7 = False
                hover8 = False

                Registry.mouse_x = Registry.real_window_width/2
                Registry.mouse_y = Registry.real_window_height/2

                while True:
                    start_inventory.wait()

                    pygame.display.init()

                    display_utils.display_utils.set_display()

                    selector.convert()

                    title_width = 0
                    WeaponsTextWidth = 0
                    RangedWeaponsTextWidth = 0
                    ShieldsTextWidth = 0
                    ArmourTextWidth = 0
                    FoodTextWidth = 0
                    ItemsTextWidth = 0
                    SpecialItemsTextWidth = 0
                    OptionsTextWidth = 0

                    if Registry.use_transparency_effects:
                        background_image_path = Registry.base_folder / "resources" / "general resources" / "PauseIMG.png"

                        background_image = Image.open(background_image_path)

                        background = image_utils.convert_image.pil_image_to_surface(
                            image_utils.transparency_effects.create_background_image(
                                background_image,
                                darken=True)).convert_alpha()

                    display_size = Registry.display.get_size()

                    while True:
                        starting_y_pos = 100
                        button_text_height = 0
                        
                        caption_utils.generate_captions.get_normal_caption(
                            "Inventory")

                        if not (Registry.error_message is None or
                                    Registry.error_message_detailed is None):
                            
                            error_utils.generate_error_screen.error_screen(
                                Registry.error_message,
                                Registry.error_message_detailed)

                        Registry.display.fill(Registry.background_color)

                        if Registry.use_transparency_effects:
                            if Registry.display.get_size() != display_size:
                                display_size = Registry.display.get_size()
                                
                                background = image_utils.convert_image.pil_image_to_surface(
                                    image_utils.transparency_effects.create_background_image(
                                        background_image,
                                        Registry.display,
                                        Registry.fancy_graphics,
                                        darken=True)).convert_alpha()

                            Registry.display.blit(background, (0, 0))

                        returned_text = text_utils.text_formatter.format_text(
                            "Pycraft",
                            ("center", "top"),
                            Registry.title_font,
                            Registry.title_backup_font)

                        title_width = returned_text.get_width()

                        text_utils.text_formatter.format_text(
                            "Inventory",
                            (((Registry.real_window_width-title_width)/2)+55, 50),
                            Registry.subtitle_font,
                            Registry.subtitle_backup_font,
                            font_color=Registry.secondary_font_color)

                        display_utils.display_functionality.core_display_functions(
                            checkEvents=False)

                        if Registry.joystick_exit:
                            break

                        for event in pygame.event.get():
                            if (event.type == pygame.QUIT or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == pygame.K_ESCAPE) or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == pygame.K_e)):
                                
                                start_inventory.clear()

                            if start_inventory.is_set():
                                if event.type == pygame.WINDOWFOCUSLOST:
                                    Registry.window_in_focus = False
                                elif event.type == pygame.WINDOWFOCUSGAINED:
                                    Registry.window_in_focus = True

                                if event.type == pygame.WINDOWSIZECHANGED:
                                    Registry.real_window_width = pygame.display.get_window_size()[0]
                                    Registry.real_window_height = pygame.display.get_window_size()[1]

                                if Registry.use_mouse_input:
                                    if (((event.type == pygame.MOUSEBUTTONDOWN or
                                            pygame.mouse.get_pressed()[0]) and
                                        (not event.type == pygame.MOUSEMOTION)) and
                                            Registry.go_to is None):

                                        Registry.primary_mouse_button_down = True

                                    else:
                                        Registry.primary_mouse_button_down = False
                                        
                                    if event.type == pygame.KEYDOWN:
                                        if (event.key == Registry.input_key[
                                                Registry.input_configuration["keyboard"]["List variables"]][0] and
                                                Registry.extended_developer_options):

                                            tkinter_utils.tkinter_info.create_tkinter_window()
                                
                                        if event.key == Registry.input_key[
                                                Registry.input_configuration["keyboard"]["Toggle full-screen"]][0]:
                                            
                                            display_utils.display_utils.update_display()

                                        if event.key == Registry.input_key[
                                                Registry.input_configuration["keyboard"]["Confirm"]][0]:
                                            
                                            Registry.primary_mouse_button_down = True

                        if not start_inventory.is_set():
                            break
                        
                        if (Registry.mouse_y >= 202*Registry.y_scale_factor and
                                    Registry.mouse_y <= 247*Registry.y_scale_factor and
                                    Registry.mouse_x >= 1155):

                            hover1 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Weapons"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.primary_mouse_button_down = False
                        else:
                            hover1 = False

                        if (Registry.mouse_y >= 252*Registry.y_scale_factor and
                                    Registry.mouse_y <= 297*Registry.y_scale_factor and
                                    Registry.mouse_x >= 1105):

                            hover2 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Ranged Weapons"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover2 = False

                        if (Registry.mouse_y >= 302*Registry.y_scale_factor and
                                    Registry.mouse_y <= 347*Registry.y_scale_factor and
                                    Registry.mouse_x >= 865):

                            hover3 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Shields"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover3 = False

                        if (Registry.mouse_y >= 402*Registry.y_scale_factor and
                                    Registry.mouse_y <= 447*Registry.y_scale_factor and
                                    Registry.mouse_x >= 1035):

                            hover4 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Armour"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover4 = False

                        if (Registry.mouse_y >= 352*Registry.y_scale_factor and
                                    Registry.mouse_y <= 397*Registry.y_scale_factor and
                                    Registry.mouse_x >= 880):

                            hover5 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Food"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover5 = False

                        if (Registry.mouse_y >= 502*Registry.y_scale_factor and
                                    Registry.mouse_y <= 547*Registry.y_scale_factor and
                                    Registry.mouse_x >= 1095):

                            hover6 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Items"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover6 = False

                        if (Registry.mouse_y >= 452*Registry.y_scale_factor and
                                    Registry.mouse_y <= 497*Registry.y_scale_factor and
                                    Registry.mouse_x >= 1095):

                            hover7 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Special Items"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover7 = False

                        if (Registry.mouse_y >= 552*Registry.y_scale_factor and
                                    Registry.mouse_y <= 597*Registry.y_scale_factor and
                                    Registry.mouse_x >= 1095):

                            hover8 = True
                            if Registry.primary_mouse_button_down:
                                selection = "Options"
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                                Registry.primary_mouse_button_down = False
                        else:
                            hover8 = False

                        returned_text = text_utils.text_formatter.format_text(
                            "Weapons",
                            ("right", 200*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover1)

                        WeaponsTextWidth = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Ranged Weapons",
                            ("right", 250*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover2)

                        RangedWeaponsTextWidth = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Shields",
                            ("right", 300*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover3)

                        ShieldsTextWidth = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Armour",
                            ("right", 350*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover5)

                        ArmourTextWidth = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Food",
                            ("right", 400*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover4)

                        FoodTextWidth = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Items",
                            ("right", 450*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover7)

                        ItemsTextWidth = returned_text.get_width()
                        
                        returned_text = text_utils.text_formatter.format_text(
                            "Special Items",
                            ("right", 500*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover6)

                        SpecialItemsTextWidth = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Options",
                            ("right", 550*Registry.y_scale_factor),
                            Registry.option_font,
                            Registry.option_backup_font,
                            underline=hover8)

                        OptionsTextWidth = returned_text.get_width()
                        
                        if hover1:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(WeaponsTextWidth+selector_width)-2,
                                    200*Registry.y_scale_factor))

                        if hover2:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(RangedWeaponsTextWidth+selector_width)-2,
                                    250*Registry.y_scale_factor))

                        if hover3:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(ShieldsTextWidth+selector_width)-2,
                                    300*Registry.y_scale_factor))

                        if hover4:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(FoodTextWidth+selector_width)-2,
                                    400*Registry.y_scale_factor))

                        if hover5:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(ArmourTextWidth+selector_width)-2,
                                    350*Registry.y_scale_factor))

                        if hover6:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(SpecialItemsTextWidth+selector_width)-2,
                                    500*Registry.y_scale_factor))

                        if hover7:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(ItemsTextWidth+selector_width)-2,
                                    450*Registry.y_scale_factor))

                        if hover8:
                            Registry.display.blit(
                                selector,
                                (Registry.real_window_width-(OptionsTextWidth+selector_width)-2,
                                    550*Registry.y_scale_factor))

                        tempfps = display_utils.display_utils.get_play_status()
                            
                        pygame.display.flip()
                        Registry.clock.tick(tempfps)

                    pygame.display.quit()
            except Exception as Message:
                error_message = "inventory > generate_inventory > inventory: "+str(Message)

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
