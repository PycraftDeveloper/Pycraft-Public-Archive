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
        
        from registry_utils import Registry
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in pycraft_startup_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class startup_test(Registry):
        def test_for_resource(
                name,
                path):

            FoundFile = os.path.exists(str(path))
            
            if FoundFile is False:
                (error_message, 
                    error_message_detailed) = startup_test.resource_not_found(
                    name,
                    path)

                return error_message, error_message_detailed

            return None, None

        def resource_not_found(
                name,
                path):
            
            error_message = "".join(("Pycraftstartup_test > startup_test > ",
                                                f"pycraft_resource_test: Unable to locate: {name}"))

            error_message_detailed = "".join(("Pycraftstartup_test > startup_test > ",
                                                f"pycraft_resource_test: Unable to locate: {name} ",
                                                f"at location: {path}"))

            return error_message, error_message_detailed
            
        def pycraft_self_test():
        
            pygame.display.set_icon(Registry.window_icon)

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

            if sys.platform == "win32" or sys.platform == "win64":
                os.environ["SDL_VIDEO_CENTERED"] = "1"

        def pycraft_resource_test(
                override):
        
            try:
                if (Registry.current_date != Registry.last_run or
                        Registry.crash or
                        Registry.run_full_startup or
                        override):

                    Registry.error_message, Registry.error_message_detailed = None, None

                    for trackID in range(6):
                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            f"footsteps{trackID}.wav",
                            Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "footstep" / f"footsteps{trackID}.wav")
                            
                        if ((not temporary_error_message_detailed is None) and
                                (Registry.error_message_detailed is None)):

                            Registry.error_message_detailed = temporary_error_message_detailed

                        if ((not temporary_error_message is None) and
                                (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "FieldAmb.ogg",
                        Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "FieldAmb.ogg")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "FieldAmb.ogg",
                        Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "FieldAmb.ogg")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    for trackID in range(11):
                        (temporary_error_message,
                            temporary_error_message_detailed) = startup_test.test_for_resource(
                            f"thunder{trackID}.ogg",
                            Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "thunder" / f"thunder{trackID}.ogg")

                        if ((not temporary_error_message is None) and
                                (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                        if ((not temporary_error_message_detailed is None) and
                                (Registry.error_message_detailed is None)):

                            Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "selectorICONlight.jpg",
                        Registry.base_folder / "resources" / "general resources" / "selectorICONlight.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "selectorICONdark.jpg",
                        Registry.base_folder / "resources" / "general resources" / "selectorICONdark.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "selectorICONdark.jpg",
                        Registry.base_folder / "resources" / "general resources" / "selectorICONcustom.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "ClearSkyTransition.gif",
                        Registry.base_folder / "resources" / "game engine resources" / "skysphere" / "ClearSkyTransition.gif")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "GrassTexture.png",
                        Registry.base_folder / "resources" / "game engine resources" / "map" / "GrassTexture.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "RockTexture.png",
                        Registry.base_folder / "resources" / "game engine resources" / "map" / "RockTexture.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "Crate.png",
                        Registry.base_folder / "resources" / "benchmark resources" / "Crate.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "inventoryGeneral.ogg",
                        Registry.base_folder / "resources" / "general resources" / "inventoryGeneral.ogg")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "Click.ogg",
                        Registry.base_folder / "resources" / "general resources" / "Click.ogg")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "map.obj",
                        Registry.base_folder / "resources" / "game engine resources" / "map" / "map.obj")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "map.mtl",
                        Registry.base_folder / "resources" / "game engine resources" / "map" / "map.mtl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "Crate.obj",
                        Registry.base_folder / "resources" / "benchmark resources" / "Crate.obj")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "raw_depth.glsl",
                        Registry.base_folder / "shaders" / "raw_depth.glsl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "shadowmap.glsl",
                        Registry.base_folder / "shaders" / "shadowmap.glsl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "orbital_prog.glsl",
                        Registry.base_folder / "shaders" / "orbital_prog.glsl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "skysphere.glsl",
                        Registry.base_folder / "shaders" / "skysphere.glsl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "benchmark.glsl",
                        Registry.base_folder / "shaders" / "benchmark.glsl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "particles_screen.glsl",
                        Registry.base_folder / "shaders" / "particles_screen.glsl")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "Full_Map.png",
                        Registry.base_folder / "resources" / "map resources" / "Full_Map.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed

                    (temporary_error_message,
                        temporary_error_message_detailed) = startup_test.test_for_resource(
                        "Marker.png",
                        Registry.base_folder / "resources" / "map resources" / "Marker.png")

                    if ((not temporary_error_message is None) and
                            (Registry.error_message is None)):

                            Registry.error_message = temporary_error_message
                            
                    if ((not temporary_error_message_detailed is None) and
                            (Registry.error_message_detailed is None)):

                        Registry.error_message_detailed = temporary_error_message_detailed
            except Exception as message:
                Registry.error_message = "".join(("Pycraftstartup_test > startup_test > ",
                                             f"pycraft_resource_test: {str(message)}"))

                Registry.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        message,
                        message.__traceback__))

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")
    
    quit()
