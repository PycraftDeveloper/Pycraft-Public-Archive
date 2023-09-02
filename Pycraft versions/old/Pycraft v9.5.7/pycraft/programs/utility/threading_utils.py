if __name__ != "__main__":
    try:
        import time
        import traceback
        
        import psutil
        import GPUtil

        from registry_utils import Registry
        import logging_utils
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
            
    class pycraft_core_threads(Registry):
        def general_threading_utility():
            try:
                while True:
                    if Registry.draw_devmode_graph:
                        if Registry.timer >= 2:
                            CPUPercent = psutil.cpu_percent(0.5)
                            if CPUPercent > Registry.data_CPU_usage_Max:
                                Registry.data_CPU_usage_Max = CPUPercent

                            Registry.data_CPU_usage.append([
                                ((Registry.real_window_width/2)+100)+(Registry.timer),
                                200-(2)*CPUPercent])

                        time.sleep(0.5)

                    else:
                        time.sleep(1)

                    if Registry.iteration > 1000:
                        Registry.average_fps = (Registry.average_fps/Registry.iteration)
                        Registry.iteration = 1

                    if (Registry.fps < 15 or
                            Registry.fps > 500):
                        
                        information_message = "".join(("ThreadingUtil > ThreadingUtils > ",
                                        "general_threading_utility: 'Registry.fps' ",
                                        "variable contained an invalid value, ",
                                        f"this has been reset to 60 from {Registry.fps} previously"))

                        logging_utils.create_log_message.update_log_information(
                            information_message)
                        
                        Registry.fps = 60

                    else:
                        if Registry.fps_overclock is False:
                            Registry.fps = int(Registry.fps)

                    if Registry.fps_overclock is False:
                        Registry.current_fps = int(Registry.current_fps)

                    else:
                        if Registry.average_fps == float("inf"):
                            Registry.average_fps = 1
                            Registry.iteration = 1
                            
            except Exception as Message:
                Registry.error_message = "".join(("ThreadingUtils > ThreadingUtils ",
                                             f"> general_threading_utility: {str(Message)}"))

                Registry.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))
                
            logging_utils.create_log_message.update_log_information(
                "'thread_pycraft_general' has stopped")

        def adaptive_mode():
            try:
                while True:
                    if Registry.settings_preset == "adaptive":
                        ProcessPercent = psutil.Process().cpu_percent(0.1)
                        CPUPercent = psutil.cpu_percent(0.1)

                        try:
                            gpus = GPUtil.getGPUs()

                            GPUPercent = 0
                            NumOfGPUs = 0

                            for gpu in gpus:
                                NumOfGPUs += 1
                                GPUPercent += gpu.load*100

                            GPUPercent = GPUPercent/NumOfGPUs

                        except Exception as Message:
                            log_message = "ThreadingUtils > ThreadingUtils > adaptive_mode: "+str(Message)

                            logging_utils.create_log_message.update_log_information(
                                log_message)
                            
                            GPUPercent = CPUPercent

                        if CPUPercent > 75 and Registry.fps > 25:
                            Registry.fps -= 1
                            if CPUPercent > 90 and Registry.fps > 25:
                                Registry.fps -= 9

                        elif ProcessPercent > 50 and Registry.fps > 25:
                            Registry.fps -= 1
                            if ProcessPercent > 75 and Registry.fps > 25:
                                Registry.fps -= 9

                        else:
                            if GPUPercent > 50 and Registry.fps > 25:
                                Registry.fps -= 1
                                if GPUPercent > 75 and Registry.fps > 25:
                                    Registry.fps -= 9

                            else:
                                if Registry.fps < 500:
                                    Registry.fps += 1
                    else:
                        time.sleep(1)
                        
            except Exception as Message:
                Registry.error_message = "ThreadingUtils > ThreadingUtils > adaptive_mode: "+str(Message)

                Registry.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

            logging_utils.create_log_message.update_log_information(
                "'thread_adaptive_mode' has stopped")

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
