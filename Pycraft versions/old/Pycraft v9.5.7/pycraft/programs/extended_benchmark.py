if __name__ != "__main__":
    try:
        import traceback
        
        import pygame
        
        import blank_window_benchmark
        import drawing_window_benchmark
        import OpenGL_window_benchmark
        
        from registry_utils import Registry
        
        import benchmark_utils
        import error_utils
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
            
    class Loadbenchmark(Registry):
        def run(self):
            try:
                (Setfps,
                    Setfpslength,
                    display,
                    iteration,
                    fpscounter,
                    Maxiteration) = benchmark_utils.start_benchmark.generate_benchmark()

                (fps_list_x_1,
                    fps_list_y_1) = blank_window_benchmark.run_blank_window_benchmark.start(
                    self,
                    iteration,
                    Setfpslength,
                    Setfps,
                    fpscounter,
                    Maxiteration,
                    display)

                pygame.display.set_caption(
                    "".join((f"Pycraft: v{Registry.version}: ",
                    "benchmark | Preparing Animated benchmark")))

                benchmark_utils.clear_benchmark.run_spacer()

                (fps_list_x_2,
                    fps_list_y_2) = drawing_window_benchmark.run_drawing_window_benchmark.start(
                    self,
                    iteration,
                    Setfpslength,
                    Setfps,
                    fpscounter,
                    Maxiteration,
                    display)

                pygame.display.set_caption(
                "".join((f"Pycraft: v{Registry.version}: benchmark | ",
                            f"Preparing OpenGL benchmark")))
                
                benchmark_utils.clear_benchmark.run_spacer()

                (display,
                    ctx,
                    wnd) = benchmark_utils.start_benchmark.generate_opengl_benchmark()

                (texture,
                    mvp,
                    light,
                    vao,
                    timer,
                    aspect_ratio) = OpenGL_window_benchmark.run_opengl_window_benchmark.setup(
                        self,
                        wnd)

                (fps_list_x_3,
                    fps_list_y_3) = OpenGL_window_benchmark.run_opengl_window_benchmark.start(
                    self,
                    iteration,
                    Setfpslength,
                    Setfps,
                    fpscounter,
                    Maxiteration,
                    ctx,
                    texture,
                    mvp,
                    light,
                    vao,
                    timer,
                    aspect_ratio)

                return (fps_list_x_1,
                            fps_list_y_1,
                            fps_list_x_2,
                            fps_list_y_2,
                            fps_list_x_3,
                            fps_list_y_3)
                
            except Exception as Message:
                error_message = "Extendedbenchmark > Loadbenchmark > run: "+str(Message)
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
