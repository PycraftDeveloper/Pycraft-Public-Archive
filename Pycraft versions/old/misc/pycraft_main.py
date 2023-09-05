try:
    import os # 
    import platform # 
    import traceback # 
    import threading # 
    import sys # 
    from tkinter import messagebox # 
    import tkinter as tk # 
    
    import moderngl # 
    import pygame # 
    import psutil # 
    
    import registry # 
    import credits # 
    import achievements # 
    import character_designer # 
    import settings # 
    import benchmark # 
    import game_engine # 
    import home # 
    import startup_animation # 
    import pycraft_startup_test # 
    import integrated_installer # 

    import installer_main as Installer # 

    import logging_utils # 
    import error_utils # 
    import file_utils # 
    import threading_utils # 
    import joystick_utils # 
    import display_utils # 
    import tkinter_utils # 
    import theme_utils # 
except Exception as Message:
    try:
        import sys
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Startup Fail",
            str(Message))
        sys.exit()

    except Exception as Message:
        print(Message)
        sys.exit()

class Startup:
    """This class is used to make sure Pycraft starts up and initializes properly.
            
    - Args:
        - None
            
    - Keyword Args:
        - None

    - Output:
        - None
    """
    def __init__(
            self):
        """This class initializes Pycraft, this class also creates the 'self' dictionary used
        throughout Pycraft.
            
        - Args:
            - self (dict): This is used by Pycraft as a way of storing it's current
                configuration and behaviour and is required by most GUIs. Its use should be
                reduced where possible for readability reasons.
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        try:
            directory = os.path.dirname(__file__)
            pycraft_directory = str(directory).split("\\")
            directory = ""

            for folder in range(len(pycraft_directory)-1):
                directory += f"{pycraft_directory[folder]}\\"

            self.base_folder = directory
            self.platform = platform.system()

            registry.generate_registry.registry(self)

            self.input_key = file_utils.pycraft_config_utils.read_input_key(
                self.platform,
                self.base_folder)

            error_message = ""
            try:
                file_utils.pycraft_config_utils.ReadMainSave(
                    self)
                
            except Exception as Message:
                error_message = "".join(("file_utils > pycraft_config_utils ",
                                                f"> ReadMainSave: {str(Message)}"))

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))
                
                user_error_message = "We were unable to read your main save file, we are going to recover what we can, but some settings may be reset.\nMore Details:\n\n"

                if self.detailed_error_messages:
                    user_error_message += str(error_message_detailed)
                else:
                    user_error_message += str(error_message)

                error_message += user_error_message
                    
                try:
                    file_utils.pycraft_config_utils.RepairLostSave(
                        self)

                except Exception as Message:
                    second_error_message = "".join(("file_utils > pycraft_config_utils ",
                                                f"> RepairLostSave: {str(Message)}"))

                    second_error_message_detailed = "".join(
                        traceback.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    second_user_error_message = "We were unable to repair your main save file, this leaves Pycraft in an unrecoverable state.\nMore Details:\n\n"

                    if self.detailed_error_messages:
                        second_user_error_message += str(second_error_message_detailed)
                    else:
                        second_user_error_message += str(second_error_message)

                    error_message += second_user_error_message

                error_utils.generate_error_screen.error_screen(
                    self.logging_dictionary,
                    self.output_log,
                    self.detailed_error_messages,
                    error_message,
                    error_message,
                    self.platform,
                    self.base_folder)
                
            logging_utils.log_file.clear_log(
                self.platform,
                self.base_folder)

            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Loaded <Pycraft_main>", 
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Started <Pycraft_main>",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported os",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported platform",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported traceback",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported threading",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported sys",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported tkinter > messagebox",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported tkinter as tk",
                self.output_log,
                self.platform,
                self.base_folder)

                        
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported moderngl",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported pygame",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported psutil",
                self.output_log,
                self.platform,
                self.base_folder)

            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported error_utils",
                self.output_log,
                self.platform,
                self.base_folder)

            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported logging_utils",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported file_utils",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported threading_utils",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported joystick_utils",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported display_utils",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported tkinter_utils",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported theme_utils",
                self.output_log,
                self.platform,
                self.base_folder)

            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported registry",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported credits",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported achievements",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported character_designer",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported settings",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported benchmark",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported game_engine",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported Installer_main",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported home",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported startup_animation",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported pycraft_startup_test",
                self.output_log,
                self.platform,
                self.base_folder)
            
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "Imported integrated_installer",
                self.output_log,
                self.platform,
                self.base_folder)

            moderngl.create_standalone_context()

            os.environ["SDL_VIDEO_CENTERED"] = "1"

            pygame.init()

            if self.platform == "Linux":
                self.title_font = pygame.font.Font(
                    os.path.join(
                        self.base_folder,
                        ("fonts//Book Antiqua.ttf")), 60)

                self.window_icon = pygame.image.load(
                    os.path.join(
                        self.base_folder,
                        ("resources//general resources//Icon.png")))

            else:
                self.window_icon = pygame.image.load(
                    os.path.join(
                        self.base_folder,
                        ("resources\\general resources\\Icon.png")))

                self.title_font = pygame.font.Font(
                    os.path.join(
                        self.base_folder,
                        ("fonts\\Book Antiqua.ttf")), 60)

            # Will remove all fps limits in game, no way to set to 'True' in game for now.
            # False by default!

            if self.fps_overclock:
                input("".join(("You are entering an unlimited fps mode; ",
                               "press enter to continue at your own risk.")))

            general_thread = threading_utils.pycraft_core_threads.general_threading_utility
            self.thread_pycraft_general = threading.Thread(
                target=general_thread,
                args=(self,))
            self.thread_pycraft_general.daemon = True
            self.thread_pycraft_general.start()
            self.thread_pycraft_general.name = "thread_pycraft_general"

            JoystickIOtarget = joystick_utils.establish_joystick_removed.JoystickRemoved
            self.thread_joystick_removed = threading.Thread(
                target=JoystickIOtarget,
                args=(self,))
            self.thread_joystick_removed.daemon = True
            self.thread_joystick_removed.start()
            self.thread_joystick_removed.name = "thread_joystick_removed"
            
        except Exception as Message:
            try:
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Startup Fail",
                    str(Message))
                sys.exit()
                
            except Exception as Message:
                print(Message)
                sys.exit()


class Initialize:
    """This class is used to start Pycraft. It is also responsible for 'connecting'
    you to different menus and making sure Pycraft starts up correctly.
            
    - Args:
        - None
            
    - Keyword Args:
        - None

    - Output:
        - None
    """
    def menu_selector(
            self):
        """This subroutine is used to transfer you between different GUIs and programs used in
        Pycraft. This is also used to make sure that different menus in Pycraft get everything
        they need in order to start properly.
            
        - Args:
            - self (dict): This is used by Pycraft as a way of storing it's current
                configuration and behaviour and is required by most GUIs. Its use should be
                reduced where possible for readability reasons.
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        try:
            while True:
                if pygame.mixer.Channel(1).get_busy() == 1:
                    pygame.mixer.Channel(1).stop()
                if pygame.mixer.Channel(2).get_busy() == 1:
                    pygame.mixer.Channel(2).stop()
                if pygame.mixer.Channel(3).get_busy() == 1:
                    pygame.mixer.Channel(3).stop()
                if pygame.mixer.Channel(4).get_busy() == 1:
                    pygame.mixer.Channel(4).stop()
                if pygame.mixer.music.get_busy() == 0:
                    pygame.mixer.music.unpause()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2
                self.startup_animation = True
                self.run_timer = 0
                self.go_to = None
                self.mouse_button_down = False

                if self.command == "saveANDexit":
                    file_utils.pycraft_config_utils.save_pycraft_config(
                        self)
                    if self.error_message is not None:
                        error_utils.generate_error_screen.error_screen(
                            self.logging_dictionary,
                            self.output_log,
                            self.detailed_error_messages,
                            self.error_message,
                            self.error_message_detailed,
                            self.platform,
                            self.base_folder)

                    pygame.quit()
                    sys.exit()

                elif self.command == "credits":
                    credits.generate_credits.credits_gui(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "achievements":
                    achievements.generate_achievements.achievements_gui(
                        self)
                    self.command = "Undefined"

                elif self.command == "character_designer":
                    character_designer.generate_character_designer.character_designer_gui(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "settings":
                    settings.generate_settings.settings_gui(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "benchmark":
                    benchmark.generate_benchmark.benchmark_gui(
                        self)
                    self.command = "Undefined"
                    continue
 
                elif self.command == "Play":
                    #from line_profiler import LineProfiler
                    game_engine.create_game_engine.game_engine(self)
                    #lp = LineProfiler()
                    #lp_wrapper = lp(game_engine.create_game_engine.game_engine)
                    #lp_wrapper(self)
                    #lp.print_stats()
                    self.command = "Undefined"
                    self.data_average_fps = []
                    self.data_CPU_usage = []
                    self.data_current_fps = []
                    self.data_memory_usage = []

                    self.timer = 0

                    self.data_average_fps_Max = 1
                    self.data_CPU_usage_Max = 1
                    self.data_current_fps_Max = 1
                    self.data_memory_usage_Max = 1

                    (self.display,
                        self.saved_window_width,
                        self.saved_window_height) = display_utils.display_utils.set_display(
                            self.fullscreen,
                            self.vsync,
                            self.saved_window_width,
                            self.saved_window_height,
                            self.window_icon,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder)

                    continue

                elif self.command == "Installer":
                    pygame.quit()
                    Installer.RunInstaller.Initialize()
                    sys.exit()

                elif self.error_message is not None:
                    error_utils.generate_error_screen.error_screen(
                        self.logging_dictionary,
                        self.output_log,
                        self.detailed_error_messages,
                        self.error_message,
                        self.error_message_detailed,
                        self.platform,
                        self.base_folder)

                else:
                    self.command = "Undefined"
                    self.command = home.generate_home.home_gui(
                        self)
                    continue
                
        except Exception as Message:
            error_message = "".join(("main > Initialize > ",
                                         f"menu_selector: {str(Message)}"))

            error_message_detailed = "".join(
                traceback.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            error_utils.generate_error_screen.error_screen(
                self.logging_dictionary,
                self.output_log,
                self.detailed_error_messages,
                error_message,
                error_message_detailed,
                self.platform,
                self.base_folder)

    def Start():
        """This subroutine is used as the default start-up option for Pycraft. This will initialize
        a display, create all the variables (by using an earlier subroutine in this module) and get
        Pycraft ready for handing over to the main menu (home). Calling this subroutine starts Pycraft.
            
        - Args:
            - None
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        try:
            global self
            self = Startup()

            try:
                self.install_location = file_utils.FixInstaller.Getinstall_location(
                    self.platform,
                    self.base_folder)
                
            except Exception as Message:
                log_message = "file_utils > FixInstaller > Getinstall_location: "+str(Message)

                logging_utils.create_log_message.update_log_warning(
                    self.logging_dictionary,
                    log_message,
                    self.output_log,
                    self.platform,
                    self.base_folder)

                try:
                    file_utils.FixInstaller.Setinstall_location(
                        self.platform,
                        self.base_folder)
                    
                except Exception as Message:
                    error_message = "".join(("file_utils > FixInstaller ",
                                                f"> Setinstall_location: {str(Message)}"))

                    error_message_detailed = "".join(
                        traceback.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    error_utils.generate_error_screen.error_screen(
                        self.logging_dictionary,
                        self.output_log,
                        self.detailed_error_messages,
                        error_message,
                        error_message_detailed,
                        self.platform,
                        self.base_folder)

            AdaptiveTarget = threading_utils.pycraft_core_threads.AdaptiveMode
            self.thread_adaptive_mode = threading.Thread(
                target=AdaptiveTarget,
                args=(self,))
            self.thread_adaptive_mode.daemon = True
            self.thread_adaptive_mode.start()
            self.thread_adaptive_mode.name = "thread_adaptive_mode"

            if self.connection_permission is None:
                permission_message = "Can we have your permission to check the internet for updates to Pycraft?"
                self.connection_permission = tkinter_utils.tkinter_info.get_permissions(
                    permission_message)

            if self.remove_file_permission is None:
                permission_message = "Can we have your permission to send files from the Pycraft directory to the recycle bin?"

                self.remove_file_permission = tkinter_utils.tkinter_info.get_permissions(
                    permission_message)

            if self.show_strobe_effects is None:
                self.show_strobe_effects = messagebox.askquestion(
                    "Check Permission",
                    "".join(("Strobe effects and bright flashes of light can ",
                                "cause discomfort, (for example lightning), you can choose here ",
                                "whether to enable or disable those ",
                                "strobe effects in Pycraft.\n\n",
                                "Click 'yes' to allow for strobe effects, or 'no' ",
                                "to turn them off. You can always adjust this in ",
                                "Pycraft's settings, under 'Storage and permissions'.")))

                if self.show_strobe_effects == "yes":
                    self.show_strobe_effects = True

                else:
                    self.show_strobe_effects = False

            if (self.current_date != self.last_run or
                    self.crash):
                self.get_outdated = [False, True]
                
                if self.connection_permission:
                    try:
                        self.connection_status = integrated_installer.CheckConnection.test()
                        
                    except Exception as Message:
                        log_message = "integrated_installer > CheckConnection > test: "+str(Message)
                        
                        logging_utils.create_log_message.update_log_warning(
                            self.logging_dictionary,
                            log_message,
                            self.output_log,
                            self.platform,
                            self.base_folder)
                        
                        self.connection_status = False

                    if self.connection_status:
                        self.Thread_Get_outdated = threading.Thread(
                            target=integrated_installer.IntegInstaller.CheckVersions,
                            args=(self,))

                        self.Thread_Get_outdated.daemon = True
                        self.Thread_Get_outdated.start()
                        self.Thread_Get_outdated.name = "Thread_Get_outdated"

            self.data_average_fps = []
            self.data_CPU_usage = []
            self.data_current_fps = []
            self.data_memory_usage = []

            self.timer = 0

            self.data_average_fps_Max = 1
            self.data_CPU_usage_Max = 1
            self.data_current_fps_Max = 1
            self.data_memory_usage_Max = 1

            (self.display,
                self.saved_window_width,
                self.saved_window_height) = display_utils.display_utils.set_display(
                    self.fullscreen,
                    self.vsync,
                    self.saved_window_width,
                    self.saved_window_height,
                    self.window_icon,
                    self.logging_dictionary,
                    self.output_log,
                    self.platform,
                    self.base_folder)

            if self.platform == "Windows":
                import win32api

                settings = win32api.EnumDisplaySettings(
                    win32api.EnumDisplayDevices().DeviceName,
                    -1)
                
                self.vsync_fps = getattr(
                    settings,
                    'DisplayFrequency')
                
            else:
                self.vsync_fps = 60

            pycraft_startup_test.startup_test.pycraft_self_test(self.window_icon)

            pygame.mouse.set_visible(False)
            
            startup_animation.generate_startup_gui.startup_gui(
                self)
            
            pygame.mouse.set_visible(True)

            if self.theme is False:
                theme_utils.determine_theme_colours.get_theme_gui(
                    self)

            theme_utils.determine_theme_colours.get_colors(
                self)

            Initialize.menu_selector(self)
            
        except Exception as Message:
            error_message = "".join(("main > Initialize ",
                                            f"> Start: {str(Message)}"))

            error_message_detailed = "".join(
                traceback.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            error_utils.generate_error_screen.error_screen(
                self.logging_dictionary,
                self.output_log,
                self.detailed_error_messages,
                error_message,
                error_message_detailed,
                self.platform,
                self.base_folder)


if __name__ == "__main__":
    try:
        counter = 0
        for proc in psutil.process_iter(["pid", "name", "username"]):
            if "pycraft.exe" in str(proc.info["name"]).lower():
                counter += 1

        if counter >= 2:
            sys.exit()

        Initialize.Start()
            
    except Exception as Message:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Startup Fail",
            str(Message))

        sys.exit()

def QueryVersion():
    """This subroutine can be used to return the current version of Pycraft.
    
    Pycraft's naming system consists of at least 3 numbers. The first
    number signifies if the project is in a finished state. The second
    number relates to the number of significant updates Pycraft has had.
    The third number relates to smaller sub-updates, these updates are
    usually used to show progress towards larger releases.

    Each time an update is released that changes any of the first 3
    numbers, a release is added here on GitHub, on PyPi and on SourceForge,
    and will be able to be downloaded in either raw (.py) python files, or
    compiled into a (.exe) format for better ease of use.

    In addition to the first 3 numbers, there may also be two additional
    numbers. The first is separated by another point at the end of the
    version and is used to signify very minor adjustments to a release.
    These are very rarely used. More commonly however is the final number
    separated by a hyphen ("-"), this is used to indicate progress towards
    a sub-update, otherwise known as developer releases these indicate
    progress towards a release and are used to break up bigger updates.
    These are often buggy and showcase experimental features.

    ### Examples
    These are not real-world examples and have been made up for the purpose of demonstration
    - Pycraft v0.9.6: This is not Pycraft in its finished state, however it is the 
        9th big update to Pycraft, and is the 6th update towards Pycraft v0.10.0
    - Pycraft v0.9.6.1: This is also not Pycraft in its finished state, however it is the
        9th big update to Pycraft, and is the 6th update towards Pycraft v0.10.0. It is also
        the second minor release of Pycraft v0.9.6 and likely fixes game breaking bugs.
    - Pycraft v0.9.6-3: This is not Pycraft in its finished state, however it is the 9th
        big update to Pycraft, and is the 6th update towards Pycraft v0.10.0. It is also
        the 3rd developer update towards Pycraft v0.9.7.

    A better system will be added soon; we will use 3 digits to represent the version of Pycraft.
    - The first digit will be used to represent the current build update to Pycraft
    - The second digit will be used to represent a smaller improvement
    - The third digit will be used for either developer updates or for patches

    This means that Pycraft v0.9.6.0-3 will become Pycraft v9.6.3! These changes take effect
    from the 24/10/2022 (DD/MM/YYYY)
        
    - Args:
        - None
            
    - Keyword Args:
        - None

    - Output:
        - version (str) - Pycraft's current version.
    """
    
    return "pycraft v0.9.6-3"


def start():
    """This subroutine is responsible for starting Pycraft, this can be used to call Pycraft
    externally, potentially as part of another program.

    - Args:
        - None
            
    - Keyword Args:
        - None

    - Output:
        - None
    """

    Initialize.Start()
