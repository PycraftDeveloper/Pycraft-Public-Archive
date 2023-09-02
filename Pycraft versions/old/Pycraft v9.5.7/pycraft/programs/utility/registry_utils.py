if __name__ != "__main__":
    try:
        import random
        import os
        import pathlib
        import platform
        
        import pygame
        import pyautogui
        import googletrans

        from seasonal_events_utils import configure_seasonal_event
        from date_utils import Date
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
            
    class Registry:
        directory = os.path.dirname(__file__)
        pycraft_directory = str(directory).split("\\")
        directory = ""

        for folder in range(len(pycraft_directory)-1):
            directory += f"{pycraft_directory[folder]}\\"

        base_folder = pathlib.Path(__file__).parent.parent.parent
        platform = platform.system()
        
        del directory
        del pycraft_directory
        
        # Direction Definitions
        RIGHT = 1
        LEFT = 2
        FORWARD = 3
        BACKWARD = 4
        UP = 5
        DOWN = 6

        # Movement Definitions
        STILL = 0
        POSITIVE = 1
        NEGATIVE = 2
            
        FOV = 70
        fps = 60
        fps_overclock = False
        aa = True
        aa_quality = "2x"
        accent_color = (237, 125, 49)
        auto_save_frequency = 30#2*60
        average_fps = 0
        background_color = [30, 30, 30]
        background_image = None
        camera = None
        camera_angle_speed = 3.5
        camera_enabled = True
        chosen_game = None
        clear_cache = False
        clear_languages_cache = False
        clock = pygame.time.Clock()
        colour_presets = {
            "red": (255, 0, 0),
            "dark red": (128, 0, 0),
            "green": (0, 255, 0),
            "dark green": (0, 128, 0),
            "blue": (0, 0, 255),
            "dark blue": (0, 0, 128),
            "yellow": (255, 255, 0),
            "dark yellow": (128, 128, 0),
            "turquoise": (0, 255, 255),
            "dark turquoise": (0, 128, 128),
            "purple": (255, 0, 255),
            "dark purple": (128, 0, 128),
            "light grey": (80, 80, 80),
            "dark grey": (30, 30, 30),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "orange": (237, 125, 49)
        }

        command = None
        compile_math = True
        connection_permission = None
        connection_status = False
        current_date = Date().get_time_code()
        crash = False
        ctx = 0
        current_memory_usage = 0
        currently_displaying_message = False
        custom_theme = None
        data_CPU_usage = []
        data_CPU_usage_Max = 1
        data_average_fps = []
        data_average_fps_Max = 1
        data_current_fps = []
        data_current_fps_Max = 1
        data_memory_usage = []
        data_memory_usage_Max = 1
        default_game_config = {
            "game_name": "New Game",
            "game_difficulty": "normal"
        }
        
        default_save_config = {
            "save_name": "Save 1",
            "time": Date().get_formatted_time(),
            "priority": Date().get_time_code(),
            "autosave": False,
            "position": [0, 0, 0],
            "rotation": [0, 0],
            "game_time": 0,
            "weather": "sunny",
            "day": 1
        }

        detailed_captions = False
        detailed_error_messages = False
        device_connected = False
        device_connected_update = False
        direction_args = (RIGHT, LEFT, FORWARD, BACKWARD, UP, DOWN)
        display = 0
        dont_use_set_resolution = False
        draw_devmode_graph = False
        current_fps = 60
        error_message = None
        error_message_detailed = None
        event = configure_seasonal_event.is_seasonal_event()

        exit_mode = None
        extended_developer_options = False
        fancy_graphics = True
        fancy_particles = True

        folder_size = 0

        colors = [(224, 175, 160),
                            (181, 68, 110),
                            (144, 227, 154),
                            (125, 131, 255),
                            (43, 65, 98),
                            (175, 66, 174),
                            (77, 157, 224),
                            (0, 212, 140),
                            (6, 141, 157),
                            (109, 157, 197),
                            (232, 141, 103),
                            (97, 61, 193),
                            (155, 197, 61)]
            
        chosen_colors = []

        temporary_colors = colors
        for _ in range(9):
            index = random.randint(0, len(temporary_colors)-1)
            chosen_colors.append(temporary_colors[index])
            del temporary_colors[index]
            
        file_structure = {"Source code": {"size": 0, "color": chosen_colors[0]},
                                    "Data files": {"size": 0, "color": chosen_colors[1]},
                                    "Audio": {"size": 0, "color": chosen_colors[2]},
                                    "Video": {"size": 0, "color": chosen_colors[3]},
                                    "Images": {"size": 0, "color": chosen_colors[4]},
                                    "3D objects": {"size": 0, "color": chosen_colors[5]},
                                    "Temporary": {"size": 0, "color": chosen_colors[6]},
                                    "Fonts": {"size": 0, "color": chosen_colors[7]},
                                    "Misc": {"size": 0, "color": chosen_colors[8]}}

        files_to_trash = [
                pathlib.Path("resources//benchmark resources//Crate.obj.bin"),
                pathlib.Path("resources//game engine resources//map//map.obj.bin"),
                pathlib.Path("resources//game engine resources//map//map.obj.json"),
                pathlib.Path("resources//game engine resources//clouds//Rnd_noise.png"),
                pathlib.Path("resources//general resources//PauseIMG.png")
            ]


        for dirpath, _, files in os.walk(base_folder):
            for name in files:
                if "__pycache__" in str(dirpath):
                    if ".pyc" in str(name) or ".nbc" in str(name) or ".nbi" in str(name):
                        file_path = os.path.join(dirpath, name)
                        files_to_trash.append(file_path)
        
        font_color = (255, 255, 255)
        FOV = 90
        format_text_chars = {
            "$r": (255, 0, 0), # red
            "$g": (0, 255, 0), # green
            "$b": (0, 0, 255), # blue
            "$y": (255, 255, 0), # yellow
            "$t": (0, 255, 255), # turquoise
            "$p": (255, 0, 255), # purple
            "$u": "<underline>", # underlines font
            "$c": "<bold>", # makes the font bold
            "$i": "<italics>", # makes the font to italics
            "$s": "<shape_color>", # sets the color to the (themed) shape color
            "$a": "<accent_color>", # sets the color to the (themed) accent color
            "$v": "<secondary_font_color>", # sets the color to the (themed) secondary font color
            "$/": "<fake_space>" # acts like the space character, but isn't displayed
        }

        fps = 60
        from_game_GUI = False
        from_play = False
        fullscreen = False
        fullscreen_x = pyautogui.size()[0]
        fullscreen_y = pyautogui.size()[1]
        
        game_engine_control = [[False, False],
                                    [False, False],
                                    [False, False],
                                    [False, False]]
        
        get_outdated = [False, False]
        go_to = None
        icon_path = base_folder / "resources" / "general resources" / "Icon.png"
        increased_speed = False
        input_configuration = None
        install_location = None
        iteration = 1
        joystick_connected = False
        joystick_exit = False
        joystick_hat_pressed = False
        joystick_zoom = None
        language_list = googletrans.LANGUAGES
        last_run = "29/09/2021"
        load_3D = True
        load_music = True
        load_time = [0, 1]
        logging_dictionary = {
            "information": False,
            "warnings": False,
            "errors": False}
        
        mouse_x = 0
        mouse_y = 0
        movement_args = (STILL, POSITIVE, NEGATIVE)
        music = True
        music_volume = 5
        outdated = False
        output_log = False
        play_time = 0
        primary_mouse_button_down = False
        progress_line = []
        progress_message_text = "Initiating"
        project_sleeping = False
        pygame_device_added_update = False
        pygame_device_removed_update = False
        real_window_height = 720
        real_window_width = 1280
        adaptive_fps = 60
        remove_file_permission = None
        render_fog = True
        reset_pycraft = False
        resolution = "(1280, 720)"
        resolutions_list = {
            "(1024, 576)": "(16:9) 1024 x 576",
            "(1152, 648)": "(16:9) 1152 x 648",
            "(1280, 720)": "(16:9) 1280 x 720 (HD)",
            "(1366, 768)": "(16:9) 1366 x 768",
            "(1600, 900)": "(16:9) 1600 x 900",
            "(1920, 1080)": "(16:9) 1920 x 1080 (Full HD)",
            "(2560, 1440)": "(16:9) 2560 x 1440",
            "(3840, 2160)": "(16:9) 3840 x 2160 (4K UHD)",
            "(7680, 4320)": "(16:9) 7680 x 4320 (8K UHD)"
        }
        
        resolution_preset = "default"
        run_full_startup = False
        run_timer = 0
        save_keys = {
            "theme": False,
            "settings_preset": "high",
            "adaptive_fps": 60,
            "fps": 60,
            "average_fps": 60,
            "iteration": 1,
            "FOV": 75,
            "camera_angle_speed": 3,
            "aa": True,
            "render_fog": True,
            "fancy_graphics": True,
            "fancy_particles": True,
            "sound": True,
            "sound_volume": 75,
            "music": False,
            "music_volume": 50,
            "x": 0,
            "y": 0,
            "z": 0,
            "last_run": "29/09/2021",
            "run_full_startup": True,
            "crash": False,
            "saved_window_width": 1280,
            "saved_window_height": 720,
            "fullscreen": True,
            "connection_permission": None,
            "updated": True,
            "load_time": [0, 1],
            "show_message": False,
            "show_strobe_effects": None,
            "extended_developer_options": False,
            "draw_devmode_graph": False,
            "detailed_error_messages": False,
            "logging_dictionary": {"information": False,
                                        "warnings": False,
                                        "errors": False},
            "save_on_exit": True,
            "resolution_preset": "default",
            "vsync": True,
            "aa_quality": "2x",
            "detailed_captions": False,
            "output_log": False,
            "increased_speed": False,
            "skip_time": False,
            "remove_file_permission": None,
            "input_configuration": {
                "keyboard": {
                    "Jump": "Space",
                    "Back": "Esc",
                    "Toggle full-screen": "F11",
                    "List variables": "Q",
                    "Walk forwards": "W",
                    "Walk backwards": "S", 
                    "Walk left": "A", 
                    "Walk right": "D",
                    "Open inventory": "E",
                    "Open map": "R",
                    "Unlock mouse": "L",
                    "Skip time": "K",
                    "Confirm": "Enter",
                    "Increase speed": "I"},

                "controller": {
                    "Confirm": 1,
                    "Back": 3,
                    "Open inventory": 7,
                    "Open map": 6,
                    "Jump": 3
                },
                
                "mouse": {
                    "Primary": 1,
                    "Wheel": 2,
                    "Secondary": 3
                }
                
            },
            "resolution": "(1280, 720)",
            "dont_use_set_resolution": False,
            "seasonal_events": False,
            "compile_math": True,
            "custom_theme": None,
            "language": "en",
            "use_transparency_effects": True,
            "auto_save_frequency": 2*60,
            # temp
            "position": [0, 0, 0],
            "rotation": [0, 0],
            "game_time": 0,
            "weather": "sunny",
            "day": 1
        }
        
        save_on_exit = True
        saved_window_height = 720
        saved_window_width = 1280
        scan_pycraft = False
        seasonal_events = False
        secondary_font_color = (100, 100, 100)
        secondary_mouse_button_down = False
        selected_input_reconfig = "keyboard"
        settings_preset = "Medium"
        shape_color = (80, 80, 80)
        show_strobe_effects = None
        show_message = True
        skip_time = False
        sound = True
        sound_volume = 75
        startup_animation = True
        theme = False
        themeArray = [
            [(255, 255, 255),
                [30, 30, 30],
                (80, 80, 80),
                (237, 125, 49),
                (255, 255, 255)],

            [(0, 0, 0),
                [255, 255, 255],
                (80, 80, 80),
                (237, 125, 49),
                (100, 100, 100)]]
        timer = 0
        total_move_x = 0
        total_move_y = 0
        total_move_z = 0
        total_number_of_updates = 0
        translated_text = {}
        updated = False
        use_mouse_input = True
        version = "9.5.7"
        vsync = True
        vsync_fps = 60
        window_in_focus = True
        wnd = None
        x = 0
        x_scale_factor = 0
        y = 0
        y_scale_factor = 0
        z = 0
        
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
