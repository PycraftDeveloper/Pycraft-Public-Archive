try:
    import os
    import platform
    import traceback
    import threading
    import sys
    from tkinter import messagebox
    import tkinter as tk
    import pathlib
    
    #import tkinter_utils
    
    #threading.Thread(
        # target=tkinter_utils.splash_screen.create_splash).start()
    
    import moderngl
    import pygame
    import psutil
    import pyautogui
    
    import credits
    import achievements
    import character_designer
    import settings
    import benchmark
    import game_engine
    import home
    import startup_animation
    import theme_gui
    
    from registry_utils import Registry
    
    import installer_main as Installer

    import integrated_installer_utils
    import logging_utils
    import error_utils
    import file_utils
    import threading_utils
    import display_utils
    import theme_utils
    import translation_utils
    import pycraft_startup_utils
    import tkinter_utils
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

class Startup(Registry):
    try:
        pygame.init()

        Registry.input_key = file_utils.pycraft_config_utils.read_input_key()

        error_message = ""
        try:
            file_utils.pycraft_config_utils.read_main_save()
            
        except Exception as Message:
            error_message = "".join(("file_utils > pycraft_config_utils ",
                                            f"> read_main_save: {str(Message)}"))

            error_message_detailed = "".join(
                traceback.format_exception(
                    None,
                    Message,
                    Message.__traceback__))
            
            user_error_message = "We were unable to read your main save file, we are going to recover what we can, but some settings may be reset.\nMore Details:\n\n"

            if Registry.detailed_error_messages:
                user_error_message += str(error_message_detailed)
            else:
                user_error_message += str(error_message)

            error_message += user_error_message
                
            try:
                file_utils.pycraft_config_utils.repair_lost_save()

            except Exception as Message:
                second_error_message = "".join(("file_utils > pycraft_config_utils ",
                                            f"> repair_lost_save: {str(Message)}"))

                second_error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                second_user_error_message = "We were unable to repair your main save file, this leaves Pycraft in an unrecoverable state.\nMore Details:\n\n"

                if Registry.detailed_error_messages:
                    second_user_error_message += str(second_error_message_detailed)
                else:
                    second_user_error_message += str(second_error_message)

                error_message += second_user_error_message

            error_utils.generate_error_screen.error_screen(
                error_message,
                error_message)
            
        logging_utils.log_file.clear_log()

        logging_utils.create_log_message.update_log_information(
            "Loaded <Pycraft_main>")
        
        logging_utils.create_log_message.update_log_information(
            "started <Pycraft_main>")

        moderngl.create_standalone_context()

        os.environ["SDL_VIDEO_CENTERED"] = "1"

        font_path = Registry.base_folder / "fonts" / "Book Antiqua.ttf"
        backup_font_path = Registry.base_folder / "fonts" / "NotoSans-Regular.ttf"
        icon_path = Registry.base_folder / "resources" / "general resources" / "Icon.png"

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
        
        Registry.window_icon = pygame.image.load(icon_path)

        if Registry.fps_overclock:
            input("".join(("You are entering an unlimited fps mode; ",
                            "press enter to continue at your own risk.")))

        general_thread = threading_utils.pycraft_core_threads.general_threading_utility
        Registry.thread_pycraft_general = threading.Thread(
            target=general_thread)
        Registry.thread_pycraft_general.daemon = True
        Registry.thread_pycraft_general.start()
        Registry.thread_pycraft_general.name = "thread_pycraft_general"
    except Exception as Message:
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "startup Fail",
                str(Message))
            sys.exit()
            
        except Exception as Message:
            print(Message)
            sys.exit()

class Initialize:
    def menu_selector():
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

                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(
                        pygame.SYSTEM_CURSOR_ARROW)

                Registry.mouse_x = Registry.real_window_width/2
                Registry.mouse_y = Registry.real_window_height/2
                Registry.startup_animation = True
                Registry.run_timer = 0
                Registry.go_to = None
                Registry.primary_mouse_button_down = False

                if Registry.command == "saveANDexit":
                    translation_utils.translation_caching.write_cache()
                
                    file_utils.pycraft_config_utils.save_pycraft_config()
                    
                    if Registry.error_message is not None:
                        error_utils.generate_error_screen.error_screen(
                            Registry.error_message,
                            Registry.error_message_detailed)

                    pygame.quit()
                    sys.exit()

                elif Registry.command == "credits":
                    credits.generate_credits.credits_gui()
                    Registry.command = "Undefined"
                    continue

                elif Registry.command == "achievements":
                    achievements.generate_achievements.achievements_gui()
                    Registry.command = "Undefined"

                elif Registry.command == "character_designer":
                    character_designer.generate_character_designer.character_designer_gui()
                    Registry.command = "Undefined"
                    continue

                elif Registry.command == "settings":
                    settings.generate_settings.settings_gui()
                    Registry.command = "Undefined"
                    continue

                elif Registry.command == "benchmark":
                    benchmark.generate_benchmark.benchmark_gui()
                    Registry.command = "Undefined"
                    continue

                elif Registry.command == "level_selector":
                    Registry.command = "Play"
                    continue

                elif Registry.command == "Play":
                    #from line_profiler import LineProfiler
                    game_engine.create_game_engine.game_engine()
                    #lp = LineProfiler()
                    #lp_wrapper = lp(game_engine.create_game_engine.game_engine)
                    #lp_wrapper(Registry)
                    #lp.print_stats()
                    Registry.command = "Undefined"
                    
                    display_utils.display_utils.set_display()

                    continue

                elif Registry.command == "Installer":
                    pygame.quit()
                    Installer.run_installer.Initialize()
                    sys.exit()

                elif Registry.error_message is not None:
                    error_utils.generate_error_screen.error_screen(
                        Registry.error_message,
                        Registry.error_message_detailed)

                else:
                    Registry.command = "Undefined"
                    Registry.command = home.generate_home.home_gui()
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
                error_message,
                error_message_detailed,)

    def start():
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
            Startup()

            try:
                Registry.translated_text = translation_utils.translation_caching.read_cache()

            except Exception as Message:
                log_message = "translation_utils > translation_caching > read_cache: "+str(Message)

                logging_utils.create_log_message.update_log_warning(
                    log_message)

            try:
                Registry.install_location = file_utils.fix_installer.get_install_location()
                
            except Exception as Message:
                log_message = "file_utils > fix_installer > get_install_location: "+str(Message)

                logging_utils.create_log_message.update_log_warning(
                    log_message)

                try:
                    file_utils.fix_installer.set_install_location()
                    
                except Exception as Message:
                    error_message = "".join(("file_utils > fix_installer ",
                                                f"> set_install_location: {str(Message)}"))

                    error_message_detailed = "".join(
                        traceback.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    error_utils.generate_error_screen.error_screen(
                        error_message,
                        error_message_detailed)

            AdaptiveTarget = threading_utils.pycraft_core_threads.adaptive_mode
            Registry.thread_adaptive_mode = threading.Thread(
                target=AdaptiveTarget)
            Registry.thread_adaptive_mode.daemon = True
            Registry.thread_adaptive_mode.start()
            Registry.thread_adaptive_mode.name = "thread_adaptive_mode"

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
                                "strobe effects in Pycraft.\n\n",
                                "Click 'yes' to allow for strobe effects, or 'no' ",
                                "to turn them off. You can always adjust this in ",
                                "Pycraft's settings, under 'Storage and permissions'.")))

                if Registry.show_strobe_effects == "yes":
                    Registry.show_strobe_effects = True

                else:
                    Registry.show_strobe_effects = False

            if (Registry.current_date != Registry.last_run or
                    Registry.crash):
                Registry.get_outdated = [False, True]
                
                if Registry.connection_permission:
                    try:
                        Registry.connection_status = integrated_installer_utils.check_connection.test()
                        
                    except Exception as Message:
                        log_message = "integrated_installer_utils > check_connection > test: "+str(Message)
                        
                        logging_utils.create_log_message.update_log_warning(
                            log_message)
                        
                        Registry.connection_status = False

                    if Registry.connection_status:
                        Registry.Thread_Get_outdated = threading.Thread(
                            target=integrated_installer_utils.integrated_installer.check_versions)

                        Registry.Thread_Get_outdated.daemon = True
                        Registry.Thread_Get_outdated.start()
                        Registry.Thread_Get_outdated.name = "Thread_Get_outdated"

            Registry.data_average_fps = []
            Registry.data_CPU_usage = []
            Registry.data_current_fps = []
            Registry.data_memory_usage = []

            Registry.timer = 0

            Registry.data_average_fps_Max = 1
            Registry.data_CPU_usage_Max = 1
            Registry.data_current_fps_Max = 1
            Registry.data_memory_usage_Max = 1

            display_utils.display_utils.set_display()

            if Registry.platform == "Windows":
                import win32api

                settings = win32api.EnumDisplaySettings(
                    win32api.EnumDisplayDevices().DeviceName,
                    -1)
                
                Registry.vsync_fps = getattr(
                    settings,
                    'DisplayFrequency')
                
            else:
                Registry.vsync_fps = 60

            pycraft_startup_utils.startup_test.pycraft_self_test()

            pygame.mouse.set_visible(False)
            
            startup_animation.generate_startup_gui.startup_gui()
            
            pygame.mouse.set_visible(True)

            if Registry.theme is False:
                theme_gui.create_theme_selection_menu.get_theme_gui()

            theme_utils.determine_theme_colours.get_colors()

            Initialize.menu_selector()
            
        except Exception as Message:
            error_message = "".join(("main > Initialize ",
                                            f"> start: {str(Message)}"))

            error_message_detailed = "".join(
                traceback.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            error_utils.generate_error_screen.error_screen(
                error_message,
                error_message_detailed)


if __name__ == "__main__":
    try:
        counter = 0
        for proc in psutil.process_iter(["pid", "name", "username"]):
            if "pycraft.exe" in str(proc.info["name"]).lower():
                counter += 1

        if counter >= 2:
            sys.exit()

        Initialize.start()
            
    except Exception as Message:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "startup Fail",
            str(Message))

        sys.exit()

def QueryVersion():
    """This subroutine can be used to return the current version of Pycraft.
    
    Version Naming
    Pycraft's versions will always now follow the structure; "vA.B.C"
    * Where "A" is the major revision number.
    * Where "B" is the minor revision number.
    * Where "C" is the patch and developer preview numbers (combined).

    Every version of Pycraft as of the 27/10/2022 (DD/MM/YYYY) must feature
    all 3 values. Updates also now go sequentially, so Pycraft v9.6.4 is
    newer than Pycraft v9.5.7. If either of the "A" or "B" version numbers
    is incremented in a release, documentation MUST be suitably updated,
    in addition Pycraft MUST be released on PyPi, SourceForge and as a
    release on GitHub.
        
    - Args:
        - None
            
    - Keyword Args:
        - None

    - Output:
        - version (str): Pycraft's current version.
    """
    
    return "pycraft v9.5.7"


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

    Initialize.start()
