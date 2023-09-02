if __name__ != "__main__":
    try:
        import threading
        
        import pygame
        import psutil
        
        from registry_utils import Registry
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
            
    class generate_captions(Registry): 
        def get_loading_caption(
                version,
                num):

            if num == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (-)")
            elif num == 1:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (\)")
            elif num == 2:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (|)")
            elif num == 3:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (/)")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading")

        def get_normal_caption(
                location):
            
            if Registry.detailed_captions:
                hours = int((Registry.play_time/60)/60)
                minutes = int(Registry.play_time/60)
                seconds = int(Registry.play_time)

                Position = f"{round(Registry.x, 2)}, {round(Registry.y, 2)}, {round(Registry.z, 2)}"
                Velocity = f"{Registry.total_move_x}, {Registry.total_move_y}, {Registry.total_move_z}"

                time = f"{hours} : {minutes} : {seconds}"

                if Registry.fps_overclock:
                    try:
                        fps_text = "".join((f"fps: 2000 current_fps: {int(Registry.current_fps)} ",
                                        f"average_fps: N/A iteration: {Registry.iteration} | "))

                        pygame.display.set_caption(
                            "".join((f"Pycraft: v{Registry.version}: {location} | ",
                                        f"Play Time: {time} | ",
                                        f"Pos: {Position} | ",
                                        f"V: {Velocity} | ",
                                        fps_text,
                                        f"MemUsE: {int(Registry.current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"Theme: {Registry.theme} | ",
                                        f"Thread Count: {threading.active_count()}")))

                    except:
                        fps_text = f"fps: 2000 current_fps: NaN* average_fps: N/A iteration: {Registry.iteration} | "

                        pygame.display.set_caption(
                            "".join((f"Pycraft: v{Registry.version}: {location} | ",
                                        f"Play Time: {time} | ",
                                        f"Pos: {Position} | ",
                                        f"V: {Velocity} | ",
                                        fps_text,
                                        f"MemUsE: {int(Registry.current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"Theme: {Registry.theme} | ",
                                        f"Thread Count: {threading.active_count()}")))

                else:
                    fps_text = "".join((f"fps: {Registry.fps} current_fps: {int(Registry.current_fps)} ",
                                    f"average_fps: {int(Registry.average_fps/Registry.iteration)} ",
                                    f"iteration: {Registry.iteration} | "))

                    pygame.display.set_caption(
                        "".join((f"Pycraft: v{Registry.version}: {location} | ",
                                    f"Play Time: {time} | ",
                                    f"Pos: {Position} | ",
                                    f"V: {Velocity} | ",
                                    fps_text,
                                    f"MemUsE: {int(Registry.current_memory_usage)}% | ",
                                    f"CPUUsE: {psutil.cpu_percent()}% | ",
                                    f"Theme: {Registry.theme} | ",
                                    f"Thread Count: {threading.active_count()}")))

            else:
                pygame.display.set_caption(f"Pycraft: v{Registry.version}: {location}")

        def set_OpenGL_caption():
            if Registry.detailed_captions:
                time_seconds = int(play_time)
                time_minutes = int(play_time/60)
                time_hours = int((play_time/60)/60)

                minutes = time_minutes-(60*time_hours)
                seconds = time_seconds-(60*time_minutes)

                time = f"{time_hours} : {minutes} : {seconds}"

                play_time = "".join((f"Play Time: {time} Game Time: ",
                                    f"{round(Registry.Time_Percent, 1)} ",
                                    f": {Registry.day-1} | "))

                Position = "".join((f"Pos: {round(Registry.camera.position[0], 2)}, ",
                                    f"{round(Registry.camera.position[1], 2)}, ",
                                    f"{round(Registry.camera.position[2], 2)} | "))

                Velocity = "".join((f"V: {Registry.total_move_x}, ",
                                    f"{Registry.total_move_y}, ",
                                    f"{Registry.total_move_z} | "))

                MemUse = f"MemUsE: {int(Registry.current_memory_usage)}% | "

                CPUUsE = f"CPUUsE: {psutil.cpu_percent()}% | "

                ThreadCount = f"Thread Count: {threading.active_count()}"

                if Registry.fps_overclock:
                    try:
                        fps = "".join((f"fps: 2000 current_fps: {int(Registry.current_fps)} ",
                                        f"average_fps: N/A iteration: {Registry.iteration} | "))

                        pygame.display.set_caption("".join((f"Pycraft: v{Registry.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {Registry.weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))
                        
                    except:
                        fps = f"fps: 2000 current_fps: NaN* average_fps: N/A iteration: {Registry.iteration} | "

                        pygame.display.set_caption("".join((f"Pycraft: v{Registry.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {Registry.weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))
                else:
                    try:
                        fps = "".join((f"fps: {Registry.fps} current_fps: ",
                                f"{int(Registry.current_fps)} average_fps: ",
                                f"{int(Registry.average_fps/Registry.iteration)} ",
                                f"iteration: {Registry.iteration} | "))

                        pygame.display.set_caption("".join((f"Pycraft: v{Registry.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {Registry.weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))

                    except:
                        fps = "".join((f"fps: {Registry.fps} current_fps: ",
                                f"{int(Registry.current_fps)} average_fps: ",
                                f"{int(Registry.average_fps/Registry.iteration)} ",
                                f"iteration: {Registry.iteration} | "))

                        pygame.display.set_caption("".join((f"Pycraft: v{Registry.version}: Playing ",
                                                        play_time,
                                                        f"Weather: {Registry.weather} | ",
                                                        Position,
                                                        Velocity,
                                                        fps,
                                                        MemUse,
                                                        CPUUsE,
                                                        ThreadCount)))
            else:
                pygame.display.set_caption(f"Pycraft: v{Registry.version}: Playing")

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
