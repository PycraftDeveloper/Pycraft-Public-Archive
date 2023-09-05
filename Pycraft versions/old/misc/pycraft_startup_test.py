if __name__ != "__main__":
    try:
        import os
        from tkinter import messagebox
        import tkinter as tk
        import sys
        import traceback

        import pygame
        import psutil
        import moderngl_window
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
            
    class startup_test:
        """
        This class is in charge running checks on your hardware and Pycraft's file
        structure to make sure any problems with incorrect file paths are identified
        quickly and you get the best experience on your hardware.
        
        - Args:
            - None
                
        - Keyword Args:
            - None

        - Output:
            - None
        """
        def __init__(self):
            pass

        def test_for_resource(
                base_folder,
                name,
                path):
            """
            This subroutine checks a given file path to see if the resource it is
            expecting to find is present. If a resource is not at the required
            location then an error is returned.
            
            - Args:
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                - name (str): This is the name of the file we are trying to find.
                - path (str): This is the path from the 'pycraft' directory to where
                    we are expecting the file to be.
                    
            - Keyword Args:
                - None

            - Output:
                - error_message (str) OR None: If an error occurs whilst
                    navigating to the required file path (potentially a
                    folder may have moved) or the file we where expecting
                    to find is not present then 'error_message' is returned.
                    If no problems occur and the resource is found then 'None'
                    gets returned.
                - error_message_detailed (str) OR None: If an error occurs whilst
                    navigating to the required file path (potentially a
                    folder may have moved) or the file we where expecting
                    to find is not present then 'error_message_detailed' is returned.
                    If no problems occur and the resource is found then 'None'
                    gets returned. This output contains more details about exactly
                    what error has occured and can be enabled - for testing or debug
                    purposes usually - in the settings menu. This is a handy debugging
                    tool.
            """
            
            FoundFile = os.path.exists(
                os.path.join(
                    base_folder,
                    path))
            
            if FoundFile is False:
                (error_message, 
                    error_message_detailed) = startup_test.resource_not_found(
                    name,
                    os.path.join(base_folder, path))

                return error_message, error_message_detailed

            return None, None

        def resource_not_found(
                name,
                path):
            """
            This subroutine creates the error message that gets returned if a
            resource is not at its expected location.
            
            - Args:
                - name (str): This is the name of the file we are trying to find.
                - path (str): This is the path from the 'pycraft' directory to where
                    we are expecting the file to be.
                    
            - Keyword Args:
                - None

            - Output:
                - error_message (str): If an error occurs whilst
                    navigating to the required file path (potentially a
                    folder may have moved) or the file we where expecting
                    to find is not present then 'error_message' is returned.
                - error_message_detailed (str): If an error occurs whilst
                    navigating to the required file path (potentially a
                    folder may have moved) or the file we where expecting
                    to find is not present then 'error_message_detailed' is returned.
                    This output contains more details about exactly
                    what error has occured and can be enabled - for testing or debug
                    purposes usually - in the settings menu. This is a handy debugging
                    tool.
            """
            
            error_message = "".join(("Pycraftstartup_test > startup_test > ",
                                                f"pycraft_resource_test: Unable to locate: {name}"))

            error_message_detailed = "".join(("Pycraftstartup_test > startup_test > ",
                                                f"pycraft_resource_test: Unable to locate: {name} ",
                                                f"at location: {path}"))

            return error_message, error_message_detailed
            
        def pycraft_self_test(
                window_icon):
            """
            This subroutine compares the minimum requirements of Pycraft to the
            specs of your hardware to see if we can run Pycraft on your PC.
            Specs:
            - OpenGL v2.8 or newer (potentially needs to be reviewed).
            - SDL v2 or newer.
            - 260 MB of RAM or more (potentially need to be reviewed).
            
            - Args:
                - window_icon (Pygame Surface): This is the icon we use in the caption (and
                    in the taskbar on some supported OS') for Pycraft.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
            pygame.display.set_icon(window_icon)

            SDLversion = pygame.get_sdl_version()[0]
            RAM = ((psutil.virtual_memory().available)/1000000)
            # expressed in MB
            OpenGLversion = moderngl_window.conf.settings.WINDOW["gl_version"]

            if OpenGLversion[0] < 2 and OpenGLversion[1] >= 8:
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Invalid OpenGL version",
                    "".join((f"OpenGL version: {OpenGLversion[0]}.{OpenGLversion[1]} ",
                                "is not supported; try a version greater than 2.7")))

                quit()

            if SDLversion < 2:
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Invalid SDL version",
                    "".join((f"SDL version: {SDLversion} is not supported; try a ",
                                "version greater than or equal to 2")))

                quit()

            if RAM < 260:
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Minimum system requirements not met",
                    "".join(("Your system does not meet the minimum 260mb free ",
                                "memory specification needed to play this game")))

                quit()

            if sys.platform == "win32" or sys.platform == "win64":
                os.environ["SDL_VIDEO_CENTERED"] = "1"

        def pycraft_resource_test(
                self,
                override):
            """
            This subroutine is in charge of checking for every resource required by Pycraft
            to make sure that it is where Pycraft will expect it to be when it is required
            by other areas of the game. Any problems raised here may mean something is wrong
            with the structure of Pycraft. Problems here after an update or when you first install
            Pycraft can indicate an error with the install. This is run in parallel (thread).
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - override (bool): This is used to forcefully run 'pycraft_resource_test'. This
                    is used to allow the user to check for problems in the settings menu (in the
                    'Storage and permissions' section).
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
        
            try:
                if (self.current_date != self.last_run or
                        self.crash or
                        self.run_full_startup or
                        override):

                    self.error_message, self.error_message_detailed = None, None

                    if self.platform == "Linux":
                        for trackID in range(6):
                            (temporary_error_message,
                                temporary_error_message_detailed) = startup_test.test_for_resource(
                                self.base_folder,
                                f"footsteps{trackID}.wav",
                                f"resources//game engine resources//GameSounds//footstep//footsteps{trackID}.wav")
                                
                            if ((not temporary_error_message_detailed is None) and
                                    (self.error_message_detailed is None)):

                                self.error_message_detailed = temporary_error_message_detailed

                            if ((not temporary_error_message is None) and
                                    (self.error_message is None)):

                                self.error_message = temporary_error_message
                                self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "FieldAmb.ogg",
                            "resources//game engine resources//GameSounds//FieldAmb.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "FieldAmb.ogg",
                            "resources//game engine resources//GameSounds//FieldAmb.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        for trackID in range(11):
                            (temporary_error_message,
                                temporary_error_message_detailed) = startup_test.test_for_resource(
                                self.base_folder,
                                f"thunder{trackID}.ogg",
                                f"resources//game engine resources//GameSounds//thunder//thunder{trackID}.ogg")

                            if ((not temporary_error_message is None) and
                                    (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                            if ((not temporary_error_message_detailed is None) and
                                    (self.error_message_detailed is None)):

                                self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "selectorICONlight.jpg",
                            "resources//general resources//selectorICONlight.jpg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "selectorICONdark.jpg",
                            "resources//general resources//selectorICONdark.jpg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "ClearSkyTransition.gif",
                            "resources//game engine resources//skysphere//ClearSkyTransition.gif")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "GrassTexture.png",
                            "resources//game engine resources//map//GrassTexture.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "RockTexture.png",
                            "resources//game engine resources//map//RockTexture.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Crate.png",
                            "resources//benchmark resources//Crate.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "inventoryGeneral.ogg",
                            "resources//general resources//inventoryGeneral.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Click.ogg",
                            "resources//general resources//Click.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "map.obj",
                            "resources//game engine resources//map//map.obj")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "map.mtl",
                            "resources//game engine resources//map//map.mtl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Crate.obj",
                            "resources//benchmark resources//Crate.obj")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "raw_depth.glsl",
                            "shaders//raw_depth.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "shadowmap.glsl",
                            "shaders//shadowmap.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "orbital_prog.glsl",
                            "shaders//orbital_prog.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "skysphere.glsl",
                            "shaders//skysphere.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "benchmark.glsl",
                            "shaders//benchmark.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "particles_screen.glsl",
                            "shaders//particles_screen.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Full_Map.png",
                            "resources//map resources//Full_Map.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Marker.png",
                            "resources//map resources//Marker.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                    else:
                        for trackID in range(6):
                            (temporary_error_message,
                                temporary_error_message_detailed) = startup_test.test_for_resource(
                                self.base_folder,
                                f"footsteps{trackID}.wav",
                                f"resources\\game engine resources\\GameSounds\\footstep\\footsteps{trackID}.wav")

                            if ((not temporary_error_message is None) and
                                    (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                            if ((not temporary_error_message_detailed is None) and
                                    (self.error_message_detailed is None)):

                                self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "FieldAmb.ogg",
                            "resources\\game engine resources\\GameSounds\\FieldAmb.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "FieldAmb.ogg",
                            "resources\\game engine resources\\GameSounds\\FieldAmb.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        for trackID in range(11):
                            (temporary_error_message,
                                temporary_error_message_detailed) = startup_test.test_for_resource(
                                self.base_folder,
                                f"thunder{trackID}.ogg",
                                f"resources\\game engine resources\\GameSounds\\thunder\\thunder{trackID}.ogg")

                            if ((not temporary_error_message is None) and
                                    (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                            if ((not temporary_error_message_detailed is None) and
                                    (self.error_message_detailed is None)):

                                self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "selectorICONlight.jpg",
                            "resources\\general resources\\selectorICONlight.jpg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "selectorICONdark.jpg",
                            "resources\\general resources\\selectorICONdark.jpg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "ClearSkyTransition.gif",
                            "resources\\game engine resources\\skysphere\\ClearSkyTransition.gif")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "GrassTexture.png",
                            "resources\\game engine resources\\map\\GrassTexture.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "RockTexture.png",
                            "resources\\game engine resources\\map\\RockTexture.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Crate.png",
                            "resources\\benchmark resources\\Crate.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "inventoryGeneral.ogg",
                            "resources\\general resources\\inventoryGeneral.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Click.ogg",
                            "resources\\general resources\\Click.ogg")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "map.obj",
                            "resources\\game engine resources\\map\\map.obj")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "map.mtl",
                            "resources\\game engine resources\\map\\map.mtl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Crate.obj",
                            "resources\\benchmark resources\\Crate.obj")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "raw_depth.glsl",
                            "shaders\\raw_depth.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "shadowmap.glsl",
                            "shaders\\shadowmap.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "orbital_prog.glsl",
                            "shaders\\orbital_prog.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "skysphere.glsl",
                            "shaders\\skysphere.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "benchmark.glsl",
                            "shaders\\benchmark.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "particles_screen.glsl",
                            "shaders\\particles_screen.glsl")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Full_Map.png",
                            "resources\\map resources\\Full_Map.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            self.base_folder,
                            "Marker.png",
                            "resources\\map resources\\Marker.png")

                        if ((not temporary_error_message is None) and
                                (self.error_message is None)):

                                self.error_message = temporary_error_message
                                
                        if ((not temporary_error_message_detailed is None) and
                                (self.error_message_detailed is None)):

                            self.error_message_detailed = temporary_error_message_detailed

            except Exception as Message:
                self.error_message = "".join(("Pycraftstartup_test > startup_test > ",
                                             f"pycraft_resource_test: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()
