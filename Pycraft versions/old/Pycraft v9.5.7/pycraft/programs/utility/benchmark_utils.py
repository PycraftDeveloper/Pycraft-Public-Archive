if __name__ != "__main__":
    try:
        import pygame
        import moderngl
        import moderngl_window
        import pyautogui

        from registry_utils import Registry
        
        import pycraft_main
        
        import display_utils
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
            
    class close_benchmark(Registry):
        """
        This class is in charge of switching back from the benchmark UI to Pycraft and
        making sure that the benchmark engine is reset so it behaves as expected next time
        the user goes to open up the benchmark menu.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass
        
        def exit_benchmark(self):
            """
            This procedure is in charge of switching back from the benchmark UI to Pycraft and
            making sure that the benchmark engine is reset so it behaves as expected next time
            the user goes to open up the benchmark menu.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            pygame.display.quit()
            pygame.display.init()
            Registry.command = "Undefined"
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

            (Registry.display,
                Registry.saved_window_width,
                Registry.saved_window_height) = display_utils.display_utils.set_display(
                    Registry.fullscreen,
                    Registry.vsync,
                    Registry.saved_window_width,
                    Registry.saved_window_height,
                    Registry.window_icon,
                    Registry.logging_dictionary,
                    Registry.output_log,
                    Registry.platform,
                    Registry.base_folder,
                    fullscreen_x,
                    fullscreen_y)
                
            pycraft_main.Initialize.menu_selector(self)

    class start_benchmark(Registry):
        """
        This class is in charge of creating and setting up the different
        environments used for each component of the graphics benchmark.
        This is done so that they all start with the same starting conditions
        to make the tests fair for comparison between different stages of the
        benchmark, and also between different devices running this benchmark.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        def __init__(self):
            pass

        def generate_benchmark(create_display=True):
            """
            This function does the bulk of the setup that you would find between different
            areas of the graphics benchmark to make sure that each test is repeatable and setup
            in the same way.
            
            - Args:
                - None
                
            - Keyword Args:
                - create_display (bool): This option controls wether a Pygame surface object
                    should be created or not. Often if a Pygame surface object isn't created
                    here then it will be in the 'generate_opengl_benchmark' function which is below this.

            - Output:
                - set_fps (array): This is an array of integers that stores FPS targets for the benchmark
                    section of Pycraft, with each element being a different FPS to try to reach, getting
                    progressively harder. The FPS from this array is updated every 500 iterations of the
                    benchmark.
                - set_fps_length (int): This is the length of the 'set_fps' array, we use this instead
                    of specifying an integer in order to allow us to make changes later on in Pycraft's
                    development about how many targets to use for the benchmark section.
                - display (Pygame Surface | None): The display object is used throughout Pycraft. This is
                    the identifier we use when we want to interact with/draw to/update Pycraft's gui.
                    Pygame is the main windowing engine used in Pycraft.
                    OR
                    If the keyword parameter 'create_display' is set to False, then None is returned.
                - iteration (int): In the benchmarking process, iteration is used to keep track of
                    how long the benchmark has been running.
                - fps_counter (int): This is used to store the index used to calculate the next element in the
                    'set_fps' array, this is used so Pycraft know's what to set the FPS to next, and what to set
                    the caption to so that it displays the current FPS being tested.
                - max_iteration (int): This is used to calculate after how many iterations we move onto the next
                    targeted FPS, currently this is set to increase the FPS every 500 'iteration's.
            """
            set_fps = [15,
                        30,
                        45,
                        60,
                        75,
                        90,
                        105,
                        120,
                        135,
                        150,
                        200,
                        250,
                        300,
                        350,
                        500]

            set_fps_length = len(set_fps)

            if create_display:
                if pygame.display.get_init():
                    pygame.display.quit()
                    pygame.display.init()

                display = pygame.display.set_mode((1280, 720))

            else:
                display = None

            iteration = 0
            fps_counter = 0
            max_iteration = 500

            return set_fps, set_fps_length, display, iteration, fps_counter, max_iteration

        def generate_opengl_benchmark():
            """
            This function handles the specific setup for any OpenGL benchmark environment.
            This is still used in partnership with 'generate_benchmark' however does extend its
            functionality with OpenGL specific data.
            
            - Args:
                - None
                
            - Keyword Args:
                - None

            - Output:
                - display (Pygame Surface | None): The display object is used throughout Pycraft. This is
                    the identifier we use when we want to interact with/draw to/update Pycraft's gui.
                    Pygame is the main windowing engine used in Pycraft.
                    OR
                    If the keyword parameter 'create_display' is set to False, then None is returned.
                - ctx (Context object): This is used by ModernGL for loading OpenGL resources
                    and enabling access to OpenGL features.
                - wnd (BaseWindow): This is used by ModernGL_window as the display object to
                    use for rendering and additional resource loading.
            """
            if pygame.display.get_init():
                pygame.display.quit()
                pygame.display.init()

            display = pygame.display.set_mode(
                (1280, 720),
                pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                vsync=0)

            ctx = moderngl.create_context(standalone=False)

            wnd = moderngl_window.get_local_window_cls("pygame2")

            moderngl_window.activate_context(wnd, ctx)

            return display, ctx, wnd

    class clear_benchmark(Registry):
        """
        This class is in charge of running a simple spacer to act as a gap between
        each of the graphics benchmarks. This is used as a time to reset arguments
        between each test, although that is not handled here.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
            
        def __init__(self):
            pass
        
        def run_spacer(
                self,
                display,
                background_color,
                clock):
            """
            This procedure is in charge of running a simple spacer to act as a gap between
            each of the graphics benchmarks. This is used as a time to reset arguments
            between each test, although that is not handled here.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier
                    we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing
                    engine used in Pycraft.
                - background_color (array): An array containing the RGB colour values used to represent the colour of
                    the background to the window at this time.
                - clock (Clock): The clock object is used by Pygame as a way of controlling the frame-rate and other
                    frame-rate specific functions. We use this to limit the FPS throughout Pycraft.
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            iteration = 0

            while iteration != 60:
                display.fill(background_color)

                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or
                        (event.type == pygame.KEYDOWN and
                            (not event.key == pygame.K_SPACE))):

                        close_benchmark.exit_benchmark(self)

                pygame.display.flip()
                iteration += 1
                clock.tick(60)

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
