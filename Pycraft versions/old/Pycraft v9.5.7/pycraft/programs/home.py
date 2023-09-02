if __name__ != "__main__":
    try:
        import os
        import time
        import traceback
        import threading
        import random

        import pygame
        import pyautogui
        
        from registry_utils import Registry
        
        import display_utils
        import error_utils
        import caption_utils
        import sound_utils
        import drawing_utils
        import text_utils
        import image_utils
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
            
    class generate_home(Registry):
        def create_banner():
            try:
                global show_message, MessageColor

                timer_start = 0
                RenderedText = False

                while Registry.command == "Undefined":
                    RenderRect = pygame.Rect(
                        0,
                        Registry.real_window_height-40,
                        Registry.real_window_width,
                        Registry.real_window_height)

                    Registry.display.fill(
                        Registry.background_color,
                        RenderRect)

                    if (show_message is not None and
                            MessageColor is not None and
                            RenderedText is False):
                        
                        timer_start = time.perf_counter()
                        RenderedText = True

                    if RenderedText:
                        if time.perf_counter()-timer_start < 3:
                            text_utils.text_formatter.format_text(
                                show_message,
                                ("center", "bottom"),
                                Registry.large_content_font,
                                Registry.large_content_backup_font,
                                font_color=MessageColor)

                        else:
                            show_message = None
                            MessageColor = None
                            RenderedText = False
                    else:
                        if Registry.use_mouse_input is False:
                            MessageText = "".join(("On the controller; use the D-pad to navigate the menu, ",
                                         "press 'B' to confirm or press 'Y' to exit"))

                            text_utils.text_formatter.format_text(
                                MessageText,
                                ("center", "bottom"),
                                Registry.large_content_font,
                                Registry.large_content_backup_font)

                    text_utils.text_formatter.format_text(
                        "By PycraftDev",
                        ("left", "bottom"),
                        Registry.large_content_font,
                        Registry.large_content_backup_font)

                    text_utils.text_formatter.format_text(
                        f"Version: {Registry.version}",
                        ("right", "bottom"),
                        Registry.large_content_font,
                        Registry.large_content_backup_font)

                    pygame.display.update(RenderRect)

                    target_fps = display_utils.display_utils.get_play_status()

                    Registry.clock.tick(target_fps/2)
                    
            except Exception as Message:
                if str(Message) != "display Surface quit":
                    Registry.error_message = "".join(("homeScreen > generate_home > ",
                                                 f"create_banner (thread): {str(Message)}"))

                    Registry.error_message_detailed = "".join(
                        traceback.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

        def home_gui():
            try:
                global show_message, MessageColor

                show_message = None
                MessageColor = Registry.font_color

                BannerThread = threading.Thread(
                    target=generate_home.create_banner)
                BannerThread.name = "Thread_BannerThread_HS"
                BannerThread.daemon = True
                BannerThread.start()

                caption_utils.generate_captions.get_normal_caption(
                    "Home")

                theme_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"

                selector = pygame.image.load(theme_path)
                selector.convert()

                selector_width = selector.get_width()
                hover1 = False
                hover2 = False
                hover3 = False
                hover4 = False
                hover5 = False
                hover6 = False
                hover7 = False

                pygame.display.flip()

                oldTHEME = Registry.theme
                coloursARRAY = []

                anim = False

                special = [30,
                           30,
                           30]

                TargetARRAY = []

                ColourDisplacement = 80

                increment = False

                Registry.currently_displaying_message = False

                outdated = Registry.outdated

                Registry.mouse_x = Registry.real_window_width/2
                Registry.mouse_y = Registry.real_window_height/2

                play_width = 0
                settings_width = 0
                char_designer_width = 0
                credits_width = 0
                achievements_width = 0
                benchmark_width = 0
                installer_width = 0

                prev_joystick_connected = False

                create_image_of_surface = False

                while True:
                    start_time = time.perf_counter()

                    if not (Registry.error_message is None or Registry.error_message_detailed is None):
                        error_utils.generate_error_screen.error_screen(
                            Registry.error_message,
                            Registry.error_message_detailed)

                    RenderRect = pygame.Rect(
                        0,
                        0,
                        Registry.real_window_width,
                        Registry.real_window_height-40)

                    if Registry.get_outdated == [True, False]:
                        Registry.get_outdated = [
                            True,
                            True]

                        outdated = Registry.outdated

                    if Registry.fancy_graphics:
                        coloursARRAY = []
                        if anim:
                            anim = False
                            TargetARRAY = []
                            for a in range(random.randint(0, 32)):
                                TargetARRAY.append(a)

                        if len(TargetARRAY) == 0:
                            TargetARRAY = [33]

                        for i in range(32):
                            for j in range(len(TargetARRAY)):
                                if i == TargetARRAY[j]:
                                    coloursARRAY.append(special)

                                else:
                                    coloursARRAY.append(Registry.shape_color)

                        if increment is False:
                            RandomInt = random.randint(0, 10)
                            if Registry.average_fps == 0 or Registry.iteration == 0:
                                ColourDisplacement -= RandomInt/(Registry.fps/4)

                            else:
                                ColourDisplacement -= RandomInt/((Registry.average_fps/Registry.iteration)/4)

                            special[0] = ColourDisplacement
                            special[1] = ColourDisplacement
                            special[2] = ColourDisplacement

                        if increment:
                            RandomInt = random.randint(0, 10)
                            if Registry.average_fps == 0 or Registry.iteration == 0:
                                ColourDisplacement += RandomInt/(Registry.fps/4)

                            else:
                                ColourDisplacement += RandomInt/((Registry.average_fps/Registry.iteration)/4)

                            special[0] = ColourDisplacement
                            special[1] = ColourDisplacement
                            special[2] = ColourDisplacement

                        if special[0] <= 30:
                            increment = True
                            special[0] = 30
                            special[1] = 30
                            special[2] = 30

                        if special[0] >= 80:
                            increment = False
                            anim = True
                            special[0] = 80
                            special[1] = 80
                            special[2] = 80
                    else:
                        coloursARRAY = Registry.fancy_graphics

                    if str(Registry.display) == "<Surface(Dead display)>":
                        Registry.data_average_fps = []
                        Registry.data_CPU_usage = []
                        Registry.data_current_fps = []
                        Registry.data_memory_usage = []

                        Registry.timer = 0

                        Registry.data_average_fps_Max = 1
                        Registry.data_CPU_usage_Max = 1
                        Registry.data_current_fps_Max = 1
                        Registry.data_memory_usage_Max = 1

                        fullscreen_x = pyautogui.size()[0]
                        fullscreen_y = pyautogui.size()[1]

                        display_utils.display_utils.set_display(
                                fullscreen_x,
                                fullscreen_y)

                    if not oldTHEME == Registry.theme:
                        theme_path = Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"
                        selector = pygame.image.load(theme_path)
                        selector.convert()

                        selector_width = selector.get_width()
                        oldTHEME = Registry.theme

                    Registry.display.fill(Registry.background_color, RenderRect)

                    display_utils.display_functionality.core_display_functions(
                        location="saveANDexit")

                    caption_utils.generate_captions.get_normal_caption(
                        "Home")

                    if Registry.go_to is None:
                        if (Registry.mouse_y >= 202*Registry.y_scale_factor and
                                Registry.mouse_y <= 247*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(play_width+selector_width))-2):

                            hover1 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                if Registry.show_strobe_effects is None:
                                    Registry.show_strobe_effects = messagebox.askquestion(
                                        "Check Permission",
                                        "".join(("Strobe effects and bright flashes of light can ",
                                                 "cause discomfort, (for example lightning), you can choose here ",
                                                 "whether to enable or disable those ",
                                                 "strobe effects in Pycraft.\n\n",
                                                 "Click 'yes' to allow for strobe effects, or 'no' ",
                                                 "to turn them off. You can always adjust this in ",
                                                 "Pycraft's settings, under 'Storage and permissions'.")))

                                    if Registry.show_strobe_effects == "yes":
                                        Registry.show_strobe_effects = True

                                    else:
                                        Registry.show_strobe_effects = False
                                        
                                Registry.go_to = "level_selector"
                                #Registry.startup_animation = True
                                Registry.run_timer = 0
                                create_image_of_surface = True

                        else:
                            hover1 = False

                        if (Registry.mouse_y >= 252*Registry.y_scale_factor and
                                Registry.mouse_y <= 297*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(settings_width+selector_width))-2):

                            hover2 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.go_to = "settings"
                                Registry.startup_animation = True
                                Registry.run_timer = 0

                        else:
                            hover2 = False

                        if (Registry.mouse_y >= 302*Registry.y_scale_factor and
                                Registry.mouse_y <= 347*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(char_designer_width+selector_width)-2)):

                            hover3 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.go_to = "character_designer"
                                Registry.startup_animation = True
                                Registry.run_timer = 0

                        else:
                            hover3 = False

                        if (Registry.mouse_y >= 402*Registry.y_scale_factor and
                                Registry.mouse_y <= 447*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(achievements_width+selector_width)-2)):

                            hover4 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.go_to = "achievements"
                                Registry.startup_animation = True
                                Registry.run_timer = 0

                        else:
                            hover4 = False

                        if (Registry.mouse_y >= 352*Registry.y_scale_factor and
                                Registry.mouse_y <= 397*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(credits_width+selector_width)-2)):

                            hover5 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.go_to = "credits"
                                Registry.startup_animation = True
                                Registry.run_timer = 0

                        else:
                            hover5 = False

                        if (Registry.mouse_y >= 452*Registry.y_scale_factor and
                                Registry.mouse_y <= 497*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(benchmark_width+selector_width)-2)):

                            hover6 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.go_to = "benchmark"
                                Registry.startup_animation = True
                                Registry.run_timer = 0

                        else:
                            hover6 = False

                        if (Registry.mouse_y >= 502*Registry.y_scale_factor and
                                Registry.mouse_y <= 547*Registry.y_scale_factor and
                                Registry.mouse_x >= (Registry.real_window_width-(installer_width+selector_width)-2)):

                            hover7 = True

                            if Registry.primary_mouse_button_down:
                                if Registry.sound:
                                    sound_utils.play_sound.play_click_sound()

                                Registry.go_to = "Installer"
                                Registry.startup_animation = True
                                Registry.run_timer = 0

                        else:
                            hover7 = False

                    if show_message is None:
                        if Registry.updated:
                            Registry.updated = False
                            show_message = f"Successfully updated Pycraft to v{Registry.version}"
                            MessageColor = (0, 255, 0)

                        elif outdated and Registry.total_number_of_updates == 1:
                            outdated = False
                            show_message = f"There are {Registry.total_number_of_updates} updates available!"
                            MessageColor = (0, 255, 0)

                        elif outdated and Registry.total_number_of_updates == 1:
                            outdated = False
                            show_message = "There is an update available!"
                            MessageColor = (0, 255, 0)

                        elif not prev_joystick_connected == Registry.joystick_connected:
                            prev_joystick_connected = Registry.joystick_connected
                            if Registry.joystick_connected:
                                show_message = "".join(("There is a new input device available! ",
                                                   "You can change input modes in settings"))

                                MessageColor = (0, 255, 0)

                            else:
                                if Registry.use_mouse_input:
                                    show_message = "Terminated connection to an input device"
                                    MessageColor = (255, 0, 0)

                                else:
                                    show_message = "".join(("Terminated connection to current ",
                                                       "input device, returning to ",
                                                       "default setting"))

                                    MessageColor = (255, 0, 0)
                                    Registry.use_mouse_input = True

                            Registry.device_connected_update = False

                    text_utils.text_formatter.format_text(
                        "Pycraft",
                        ("center", "top"),
                        Registry.title_font,
                        Registry.title_backup_font)

                    returned_text = text_utils.text_formatter.format_text(
                        "Play",
                        ("right", 200*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover1)

                    play_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Settings",
                        ("right", 250*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover2)

                    settings_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Character Designer",
                        ("right", 300*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover3)

                    char_designer_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Credits",
                        ("right", 350*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover5)

                    credits_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Achievements",
                        ("right", 400*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover4)

                    achievements_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Benchmark",
                        ("right", 450*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover6)

                    benchmark_width = returned_text.get_width()

                    returned_text = text_utils.text_formatter.format_text(
                        "Installer",
                        ("right", 500*Registry.y_scale_factor),
                        Registry.option_font,
                        Registry.option_backup_font,
                        underline=hover7)

                    installer_width = returned_text.get_width()

                    if hover1:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(play_width+selector_width)-2,
                                200*Registry.y_scale_factor))

                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover2:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(settings_width+selector_width)-2,
                                250*Registry.y_scale_factor))
                        
                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover3:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(char_designer_width+selector_width)-2,
                                300*Registry.y_scale_factor))

                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover5:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(credits_width+selector_width)-2,
                                350*Registry.y_scale_factor))

                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover4:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(achievements_width+selector_width)-2,
                                400*Registry.y_scale_factor))

                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover6:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(benchmark_width+selector_width)-2,
                                450*Registry.y_scale_factor))

                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif hover7:
                        Registry.display.blit(
                            selector,
                            (Registry.real_window_width-(installer_width+selector_width)-2,
                                500*Registry.y_scale_factor))

                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    else:
                        if Registry.use_mouse_input:
                            pygame.mouse.set_cursor(
                                pygame.SYSTEM_CURSOR_ARROW)

                    drawing_utils.generate_graph.create_devmode_graph()

                    drawing_utils.draw_rose.create_rose(
                        coloursARRAY,
                        51,
                        142,
                        524*Registry.x_scale_factor,
                        524*Registry.y_scale_factor)

                    if Registry.go_to is None:
                        display_utils.display_animations.fade_in(
                            size="limited")
                            
                    else:
                        display_utils.display_animations.fade_out(
                            size="limited")

                    pygame.display.update(RenderRect)

                    if create_image_of_surface:
                        if Registry.use_transparency_effects:
                            create_image_of_surface = False

                            image_utils.convert_image.surface_to_pil_image(Registry.display)
                        

                    if (Registry.startup_animation is False and
                            (Registry.go_to is not None)):
                        
                        return Registry.go_to
                        
                    target_fps = display_utils.display_utils.get_play_status()

                    Registry.clock.tick(target_fps/2)
                    Registry.run_timer += time.perf_counter()-start_time

                    if Registry.error_message is not None:
                        Registry.error_message = "homeScreen: "+str(Registry.error_message)
                        return

            except Exception as Message:
                error_message = "homeScreen > generate_home > home_gui: "+ str(Message)
                
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
