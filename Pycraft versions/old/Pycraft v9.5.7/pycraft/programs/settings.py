if __name__ != "__main__":
    try:
        import subprocess
        import sys
        import os
        import time
        import threading
        import json
        from tkinter import messagebox
        import traceback
        
        import pygame

        from registry_utils import Registry
        
        import pycraft_startup_utils
        import caption_utils
        import display_utils
        import file_utils
        import error_utils
        import sound_utils
        import tkinter_utils
        import drawing_utils
        import settings_utils
        import text_utils
        import translation_utils
        import theme_utils
        import input_utility
        import toggle_utils
        import slider_utils
        import remapping_utils
        import custom_theme_utils
        import button_utils
        import directory_utils
        import dropdown_utils
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
            sys.exit()
            
    class generate_settings(Registry):  
        def restart_function():
            restart_path = Registry.base_folder / "main.py"
            
            subprocess.call(
                [sys.executable,
                    restart_path] + sys.argv[1:])

        def settings_gui():
            try:
                caption_utils.generate_captions.get_normal_caption(
                    "Settings")

                button_offset = 0

                current_menu = "General"
                hover_menu = None

                Registry.mouse_x = Registry.real_window_width/2
                Registry.mouse_y = Registry.real_window_height/2

                settings_config_path = Registry.base_folder / "data files" / "settings_config.json"
                selector_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"

                with open(settings_config_path,
                        "r") as openFile:

                    settings_structure = json.load(openFile)

                selector = pygame.image.load(selector_path)
                selector.convert()

                selector_width = selector.get_width()

                initial_theme = Registry.theme

                hovering = False
                dropdown_hovering = False
                max_x = 0
                info_offset = 0
                hover_id = None
                files_to_remove = True
                clear_languages = True
                scanned_files = False
                hovering_over_key = False
                scan_directory = False
                maximum_remap_width = 0
                disable_events = False

                scrollbar_needed = False
                general_y_position = 0
                scroll = 0
                dropdown_scroll = 0
                scroll_enabled = True
                
                button_width = 0
                button_height = 0
                title_width = 0

                underline_button = False

                custom_theme_choice = None
                while True:
                    start_time = time.perf_counter()

                    if not (Registry.error_message is None or
                                Registry.error_message_detailed is None):
                        
                        error_utils.generate_error_screen.error_screen(
                            Registry.error_message,
                            Registry.error_message_detailed)

                    display_events = display_utils.display_functionality.core_display_functions(
                        return_events=True,
                        disable_events=disable_events)

                    for event in display_events:
                        if event.type == pygame.MOUSEWHEEL and dropdown_hovering:
                            if Registry.use_mouse_input:
                                pygame.mouse.set_cursor(
                                    pygame.SYSTEM_CURSOR_SIZENS)
                                
                        else:           
                            if event.type == pygame.MOUSEWHEEL and scrollbar_needed:
                                if Registry.use_mouse_input:
                                    pygame.mouse.set_cursor(
                                        pygame.SYSTEM_CURSOR_SIZENS)

                                    
                                    if str(event.y)[0] == "-":
                                        if scroll > 0:
                                            scroll -= 5

                                    else:
                                        if scroll_enabled:
                                            scroll += 5

                    caption_utils.generate_captions.get_normal_caption(
                        "Settings")

                    Registry.display.fill(Registry.background_color)

                    cover_Rect = pygame.Rect(
                        0,
                        0,
                        Registry.real_window_width,
                        90)

                    pygame.draw.rect(
                        Registry.display,
                        Registry.background_color,
                        cover_Rect)

                    returned_text = text_utils.text_formatter.format_text(
                        "Pycraft",
                        ("center", "top"),
                        Registry.title_font,
                        Registry.title_backup_font)

                    title_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Settings",
                        (((Registry.real_window_width-title_width)/2)+55, 50),
                        Registry.subtitle_font,
                        Registry.subtitle_backup_font,
                        font_color=Registry.secondary_font_color)

                    if initial_theme != Registry.theme:
                        initial_theme = Registry.theme
                        returned_text = text_utils.text_formatter.format_text(
                            "Pycraft",
                            ("center", "top"),
                            Registry.title_font,
                            Registry.title_backup_font)

                        title_width = returned_text.get_width()

                        returned_text = text_utils.text_formatter.format_text(
                            "Settings",
                            (((Registry.real_window_width-title_width)/2)+55, 50),
                            Registry.subtitle_font,
                            Registry.subtitle_backup_font,
                            font_color=Registry.secondary_font_color)

                        selector_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"
                
                        selector = pygame.image.load(selector_path)
                        selector.convert()

                        selector_width = selector.get_width()

                    button_y_position = 0
                    button_id = 0
                            
                    for key in settings_structure:
                        
                        if (key == "Developer options" and
                                Registry.extended_developer_options is False):
                            
                            font_color = Registry.shape_color
                            underline_button = False
                            
                        else:
                            if key == hover_menu:
                                underline_button = True

                            
                            font_color = Registry.font_color

                        if button_width > max_x:
                            max_x = button_width
                        
                        button_height += 50 - button_height

                        button_blit_y = (button_y_position * Registry.y_scale_factor) + button_offset

                        returned_text = text_utils.text_formatter.format_text(
                            key,
                            ("right", button_blit_y),
                            Registry.option_font,
                            Registry.option_backup_font,
                            font_color=font_color,
                            underline=underline_button)

                        underline_button = False

                        button_width = returned_text.get_width()
                        button_height = returned_text.get_height()

                        button_blit_x = (Registry.real_window_width-button_width)-2
                        
                        if key == hover_menu:
                            if not (key == "Developer options" and
                                    Registry.extended_developer_options is False):
                        
                                Registry.display.blit(
                                    selector,
                                    (Registry.real_window_width-(button_width+selector_width)-2,
                                        button_blit_y))

                        if ((Registry.mouse_x > button_blit_x and
                                    Registry.mouse_x < Registry.real_window_width and
                                    Registry.mouse_y > button_blit_y and
                                    Registry.mouse_y < button_blit_y + button_height) and
                                not (key == "Developer options" and 
                                        Registry.extended_developer_options is False)):
                            
                            hover_menu = key
                            hovering = True

                            if (Registry.primary_mouse_button_down and
                                    current_menu != key):
                                
                                current_menu = key
                                scrollbar_needed = False
                                scroll = 0
                                Registry.primary_mouse_button_down = False
                                
                                if current_menu == "Storage and permissions":
                                    scan_directory = True
                                
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()
                                    
                        else:
                            if hover_menu == key:
                                hover_menu = None

                        button_y_position += button_height

                        sub_menu = settings_structure[current_menu]

                        general_y_position = 100

                        if scan_directory:
                            scan_directory = False
                            file_utils.scan_folder.search_files()

                        if Registry.clear_languages_cache:
                            Registry.clear_languages_cache = False
                            
                            if clear_languages:
                                Registry.translated_text = {}
                                translation_utils.translation_caching.write_cache()

                                clear_languages = False
                                scan_directory = True

                        if Registry.clear_cache:
                            Registry.clear_cache = False
                            
                            if files_to_remove:
                                file_utils.delete_files.clear_temporary_files()

                                files_to_remove = False
                                scan_directory = True

                        if Registry.scan_pycraft:
                            Registry.scan_pycraft = False

                            pycraft_startup_utils.startup_test.pycraft_resource_test(
                                True)

                            scanned_files = True

                        if Registry.reset_pycraft:
                            Registry.reset_pycraft = False

                            theme = Registry.theme
                            for key in Registry.save_keys:
                                setattr(Registry, key, Registry.save_keys[key])

                            Registry.theme = theme

                            if Registry.connection_permission is None:
                                permission_message = "Can we have your permission to check the internet for updates to Pycraft?"
                                Registry.connection_permission = tkinter_utils.tkinter_info.get_permissions(
                                    permission_message)

                            if Registry.remove_file_permission is None:
                                permission_message = "Can we have your permission to send files from the Pycraft directory to the recycle bin?"
                                Registry.remove_file_permission = tkinter_utils.tkinter_info.get_permissions(
                                    permission_message)
                                
                            if Registry.show_strobe_effects is None:
                                Registry.show_strobe_effects = messagebox.askquestion(
                                    "Check Permission",
                                    "".join(("Strobe effects and bright flashes of light can ",
                                                "cause discomfort, (for example lightning), you can choose here ",
                                                "whether to enable or disable those ",
                                                "strobe effects in Pycraft.\n",
                                                "Click 'yes' to allow for strobe effects, or 'no' ",
                                                "to turn them off. You can always adjust this in ",
                                                "Pycraft's settings, under 'Storage and permissions'.")))

                                if Registry.show_strobe_effects == "yes":
                                    Registry.show_strobe_effects = True

                                else:
                                    Registry.show_strobe_effects = False
                            
                        if Registry.exit_mode == "restart":
                            if Registry.save_on_exit:
                                file_utils.pycraft_config_utils.save_pycraft_config()
                                
                            threading.Thread(
                                target=generate_settings.restart_function).start()

                            pygame.quit()
                            while True:
                                time.sleep(30)

                        if Registry.exit_mode == "exit":
                            if Registry.save_on_exit:
                                file_utils.pycraft_config_utils.save_pycraft_config()
                                
                            pygame.quit()
                            sys.exit()

                        if sub_menu[0] is not None:
                            for item in range(len(sub_menu)):
                                data = []
                                mouse_over = False

                                if scrollbar_needed:
                                    scroll_x_offset = 9

                                else:
                                    scroll_x_offset = 0
                                    
                                for entry in range(3, len(sub_menu[item])):
                                    if str(sub_menu[item][entry]) != "directory_structure":
                                        if str(sub_menu[item][entry]) == "average_fps":
                                            argument = int(Registry.average_fps/Registry.iteration)

                                        elif str(sub_menu[item][entry]) == "keybinds":
                                            pass
                                        
                                        else:
                                            if str(sub_menu[item][entry]) == "use_mouse_input":
                                                argument = not Registry.__dict__[sub_menu[item][entry]]
                                            else:
                                                argument = Registry.__dict__[sub_menu[item][entry]]
                                                
                                            if "float" in str(type(argument)):
                                                argument = int(argument)

                                            if sub_menu[item][3] == "dont_use_set_resolution":
                                                inverted_value = argument
                                                argument = not inverted_value
                                                
                                            if argument is True:
                                                argument = "Enabled"
                                                
                                            if argument is False:
                                                argument = "Disabled"
                                        
                                    data.append(argument)

                                if (sub_menu[item][3] == "music_volume" and
                                        Registry.music is False):
                                    
                                    font_color = Registry.shape_color
                                    
                                elif (sub_menu[item][3] == "sound_volume" and
                                        Registry.sound is False):
                                    
                                    font_color = Registry.shape_color

                                elif (sub_menu[item][3] == "fps" and
                                        Registry.vsync):

                                    font_color = Registry.shape_color

                                elif (sub_menu[item][3] == "aa_quality" and
                                        Registry.aa is False):

                                    font_color = Registry.shape_color

                                elif (sub_menu[item][3] == "clear_cache" and
                                        files_to_remove is False):

                                    font_color = Registry.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done."

                                elif (sub_menu[item][3] == "clear_languages_cache" and
                                        clear_languages is False):

                                    font_color = Registry.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done."

                                elif (sub_menu[item][3] == "scan_pycraft" and
                                        scanned_files is True):

                                    font_color = Registry.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done, no errors were found."

                                elif (sub_menu[item][3] == "use_mouse_input" and
                                        not Registry.joystick_connected):

                                    font_color = Registry.shape_color
                                    text_to_render = str(sub_menu[item][0]).format(*data)
                                    enabled = False
                                    
                                else:
                                    enabled = True
                                    font_color = Registry.font_color
                                    if sub_menu[item][3] == "language":
                                        language = data[0]
                                        data = Registry.language_list[language].capitalize()
                                        text_to_render = str(sub_menu[item][0]).format(data)
                                        
                                    else:
                                        if (sub_menu[item][3] == "resolution" and
                                                Registry.dont_use_set_resolution is False):
                                    
                                            font_color = Registry.shape_color
                                            enabled = False
                                    
                                        text_to_render = str(sub_menu[item][0]).format(*data)

                                returned_text = text_utils.text_formatter.format_text(
                                    text_to_render,
                                    (scroll_x_offset, general_y_position - scroll),
                                    Registry.small_content_font,
                                    Registry.small_content_backup_font)

                                text_height = returned_text.get_height()
                                            
                                argument_variable = sub_menu[item][3]
                                saved_y_position = general_y_position

                                if list(sub_menu[item][2].keys())[0] == "remap_function":
                                    remap_pos = (general_y_position + text_height + 10) - scroll
                                    options = Registry.input_configuration[Registry.selected_input_reconfig]
                                    
                                    (keybind_height,
                                        mouse_over,
                                        hovering,
                                        maximum_remap_width,
                                        disable_events) = remapping_utils.draw_setting_elements.draw_remap_function(
                                        remap_pos,
                                        options,
                                        hovering,
                                        mouse_over,
                                        Registry.small_content_font,
                                        Registry.small_content_backup_font,
                                        maximum_remap_width,
                                        display_events,
                                        scrollbar_needed)

                                    general_y_position += keybind_height

                                elif list(sub_menu[item][2].keys())[0] == "directory_structure":
                                    button_pos = (general_y_position + text_height + 10) - scroll

                                    (graph_height,
                                        hovering,
                                        mouse_over,
                                        hover_id) = directory_utils.draw_setting_elements.draw_directory_structure(
                                        button_pos,
                                        Registry.small_content_font,
                                        Registry.small_content_backup_font,
                                        hovering,
                                        mouse_over,
                                        hover_id,
                                        hovering_over_key,
                                        scrollbar_needed)

                                    general_y_position += graph_height

                                else:
                                    name = str(sub_menu[item][entry])
                                    if name == "use_mouse_input":
                                        value = not Registry.__dict__[argument_variable]

                                    else:
                                        value = Registry.__dict__[argument_variable]
                                    
                                    if list(sub_menu[item][2].keys())[0] == "button":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        button_text_array = sub_menu[item][2]["button"]
                                        
                                        (button_height,
                                            hovering,
                                            mouse_over) = button_utils.draw_setting_elements.draw_buttons(
                                            button_pos,
                                            button_text_array,
                                            Registry.small_content_font,
                                            Registry.small_content_backup_font,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            files_to_remove,
                                            clear_languages,
                                            scanned_files,
                                            scrollbar_needed)
                                        
                                        general_y_position += button_height

                                    if Registry.theme == "custom" and sub_menu[item][3] == "theme":
                                        if Registry.custom_theme is None:
                                            theme_utils.determine_theme_colours.get_colors()

                                            Registry.custom_theme = {
                                                "font_color": Registry.font_color,
                                                "background_color": Registry.background_color,
                                                "shape_color": Registry.shape_color,
                                                "accent_color": Registry.accent_color,
                                                "secondary_font_color": Registry.secondary_font_color}

                                        button_pos = (general_y_position + text_height - 5) - scroll
                                            
                                        (button_height,
                                            hovering,
                                            mouse_over,
                                            custom_theme_choice) = custom_theme_utils.draw_setting_elements.draw_custom_theme_options(
                                            button_pos,
                                            Registry.small_content_font,
                                            Registry.small_content_backup_font,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            custom_theme_choice,
                                            display_events)

                                        for i in range(len(list(Registry.custom_theme))):
                                            argument = str(Registry.custom_theme[list(Registry.custom_theme)[i]])
                                            input_result = input_utility.identify_patterns.identify_rgb(argument)
                                            if input_result is False:
                                                input_result = input_utility.identify_patterns.identify_hex(argument[1:-1])
                                                if input_result is False:
                                                    input_result = input_utility.identify_patterns.identify_text(argument, Registry.colour_presets)
                                                    if not input_result is False:
                                                        setattr(Registry, list(Registry.custom_theme)[i], input_result)
                                                else:
                                                    setattr(Registry, list(Registry.custom_theme)[i], input_result)
                                            else:
                                                setattr(Registry, list(Registry.custom_theme)[i], input_result)

                                        general_y_position += button_height

                                    if list(sub_menu[item][2].keys())[0] == "dropdown":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        if sub_menu[item][2]["dropdown"] == "<translate_languages_list>":
                                            content = Registry.language_list
                                        elif sub_menu[item][2]["dropdown"] == "<rendering_resolutions>":
                                            content = Registry.resolutions_list
                                        else:
                                            content = None

                                        argument_variable = sub_menu[item][3]
                                            
                                        (dropdown_height,
                                            hovering,
                                            mouse_over,
                                            dropdown_hovering,
                                            dropdown_scroll) = dropdown_utils.draw_setting_elements.draw_dropdown(
                                            dropdown_scroll,
                                            button_pos,
                                            Registry.small_content_font,
                                            Registry.small_content_backup_font,
                                            argument_variable,
                                            hovering,
                                            dropdown_hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            content,
                                            enabled)

                                        general_y_position += dropdown_height

                                    if list(sub_menu[item][2].keys())[0] == "multi-button":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        button_text_array = sub_menu[item][2]["multi-button"]

                                        (button_height,
                                            hovering,
                                            mouse_over) = button_utils.draw_setting_elements.draw_multi_buttons(
                                            button_pos,
                                            button_text_array,
                                            Registry.small_content_font,
                                            Registry.small_content_backup_font,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed)

                                        general_y_position += button_height

                                    if list(sub_menu[item][2].keys())[0] == "slider":
                                        slider_pos = (general_y_position + text_height + 10) - scroll
                                        slider_array = sub_menu[item][2]["slider"]
                                        minimum = slider_array[0]
                                        maximum = slider_array[1]
                                        
                                        (slider_height,
                                            hovering,
                                            mouse_over) = slider_utils.draw_setting_elements.draw_slider(
                                            slider_pos,
                                            minimum,
                                            maximum,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed)
                                        
                                        general_y_position += slider_height

                                    if list(sub_menu[item][2].keys())[0] == "toggle":
                                        toggle_pos = (general_y_position + text_height + 10) - scroll
                                        slider_array = sub_menu[item][2]["toggle"]
                                        value_0 = slider_array[0]
                                        value_1 = slider_array[1]
                                        
                                        (toggle_height,
                                            hovering,
                                            mouse_over) = toggle_utils.draw_setting_elements.draw_toggle(
                                            toggle_pos,
                                            value_0,
                                            value_1,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed,
                                            enabled)
                                        
                                        general_y_position += toggle_height

                                if mouse_over:                                    
                                    info_offset = settings_utils.draw_setting_elements.create_information_message(
                                        Registry.small_content_font,
                                        Registry.small_content_backup_font,
                                        sub_menu[item][1],
                                        saved_y_position,
                                        max_x,
                                        info_offset)
                                    
                                general_y_position += text_height

                            if (general_y_position - scroll) + 10 > Registry.real_window_height:
                                scroll_enabled = True

                            else:
                                scroll_enabled = False

                            if general_y_position > Registry.real_window_height:
                                scrollbar_needed = True
                                
                                rect = pygame.Rect(
                                    2,
                                    scroll + 2,
                                    3,
                                    Registry.real_window_height - (general_y_position % Registry.real_window_height) - 18)

                                pygame.draw.rect(
                                    Registry.display,
                                    Registry.shape_color,
                                    rect,
                                    border_radius=2)

                            else:
                                scrollbar_needed = False
                                scroll = 0

                        button_id += 1
                        
                    button_y_position *= Registry.y_scale_factor

                    button_offset = (Registry.real_window_height - button_y_position) / 2

                    drawing_utils.generate_graph.create_devmode_graph()

                    if Registry.go_to is None:
                        display_utils.display_animations.fade_in()
                            
                    else:
                        display_utils.display_animations.fade_out()

                    if not Registry.startup_animation and (Registry.go_to is not None):
                        return

                    if hovering:
                        hovering = False
                        pygame.mouse.set_cursor(
                                pygame.cursors.Cursor(
                                    pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(
                            pygame.cursors.Cursor(
                                pygame.SYSTEM_CURSOR_ARROW))

                    target_fps = display_utils.display_utils.get_play_status()
                        
                    pygame.display.flip()
                    Registry.clock.tick(target_fps)

                    Registry.run_timer += time.perf_counter()-start_time
                    
            except Exception as Message:
                error_message = (
                    f"settings > generate_settings > settings: {str(Message)}")

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
    