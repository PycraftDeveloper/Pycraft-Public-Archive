if __name__ != "__main__":
    try:
        import os
        import time
        import traceback
        
        import pygame
        import cpuinfo
        import psutil
        import pyautogui

        import extended_benchmark

        from registry_utils import Registry
        
        import benchmark_utils
        import display_utils
        import error_utils
        import text_utils
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
            
    class generate_benchmark(Registry):
        def benchmark_gui():
            try:
                pygame.mixer.music.fadeout(500)

                pygame.display.set_caption(f"Pycraft: v{Registry.version}: Benchmark")

                title_font = Registry.title_font.render(
                    "Pycraft",
                    Registry.aa,
                    Registry.font_color)

                title_width = title_font.get_width()

                benchmark_font = Registry.subtitle_font.render(
                    "Benchmark",
                    Registry.aa,
                    Registry.secondary_font_color)

                fps_information_text = Registry.large_content_font.render(
                    "fps benchmark results",
                    Registry.aa,
                    Registry.font_color)
                fps_information_text_width = fps_information_text.get_width()

                file_information_text = Registry.large_content_font.render(
                    "Read test results",
                    Registry.aa,
                    Registry.font_color)
                file_information_text_width = file_information_text.get_width()

                hardware_information_text = Registry.large_content_font.render(
                    "Hardware results",
                    Registry.aa,
                    Registry.font_color)
                hardware_information_text_width = hardware_information_text.get_width()

                sixty_fps_data = Registry.small_content_font.render(
                    "60 Hz",
                    Registry.aa,
                    Registry.accent_color)

                one_four_four_fps_data = Registry.small_content_font.render(
                    "144 Hz",
                    Registry.aa,
                    Registry.accent_color)

                two_forty_fps_data = Registry.small_content_font.render(
                    "240 Hz",
                    Registry.aa,
                    Registry.accent_color)

                benchmark_information_text = ["".join(("Welcome to the benchmark section; ",
                                                 "press SPACE to continue, or any ",
                                                 "other key to leave at any time ")),
                    " ",
                    "Purpose",
                    "The benchmark section is designed for a few tasks:",
                    "".join(("1. To give an insight into the performance ",
                            "you will likely get when playing the ",
                            "project, which you can then use to ",
                            "change settings.")),

                    "".join(("2. The data collected in the benchmark ",
                             "section can be used for automating control ",
                             "of settings automatically when ADAPTIVE ",
                             "mode is selected in settings.")),

                    "".join(("3. To give a repeatable demonstration ",
                             "of how the project performs with your ",
                             "current hardware setup or software configuration.")),
                    " ",
                    "Structure",
                    "".join(("The benchmark will automatically run a ",
                             "variety of tests, this includes a disk ",
                             "read check, as well as a CPU and GPU ",
                             "based load. In the order of occurrence:")),
                    " ",
                    "".join(("1. Once the user has initiated the ",
                             "benchmark (by pressing SPACE), a small ",
                             "amount of information is collected on ",
                             "the hardware your device is running, ",
                             "we try to obtain the CPU's name, as ",
                             "well as its max clock speed, as well as ",
                             "the amount of available memory and how ",
                             "much is used. This is used solely for ",
                             "the results GUI at the end of the menu ",
                             "and is not stored or shared anywhere).")),

                    "".join(("2. Next we enter 1 of 3 graphics oriented ",
                             "tests, starting with a blank screen test ",
                             "to establish a baseline.")),

                    "".join(("3. Then we enter test 2 of the 3 graphics ",
                             "test, this is much more CPU intensive, ",
                             "as lots more data is being processed ",
                             "and drawn to the display.")),

                    "".join(("4. To conclude the graphics test, we enter ",
                             "graphics test 3, this tests 3D performance ",
                             "as well as basic lighting, it is likely ",
                             "your device will get a very good score here ",
                             "as this is very GPU dependant but not ",
                             "difficult to run.")),

                    "".join(("5. Finally we enter a disk read test, in ",
                             "which a 1 MB file is read over a period ",
                             "of time to establish a rough indication ",
                             "of drive performance.")),
                    " ",
                    "Results",
                    "".join(("Once the series of tests has completed, ",
                             "you will be shown a screen that displays ",
                             "your results, listing the scores (minimum ",
                             "and maximum) for the graphics tests, as ",
                             "well as displaying them on a line graph. ",
                             "It is at this point that you are given the ",
                             "results of the disk read test, as well as ",
                             "the information on the hardware in your ",
                             "system, which we collected earlier.")),
                    " ",
                    "Important things to note",
                    "".join(("During this test, the open window may ",
                             "appear unresponsive, or that nothing is ",
                             "happening, you can observe that the ",
                             "caption details some information on the ",
                             "test what section the process is on, if ",
                             "the details change after a period of time ",
                             "then the window is responding. You may ",
                             "also observer your device heating up, ",
                             "this array of tests is designed to ",
                             "challenge and push your hardware, ",
                             "it is unlikely that your device ",
                             "will reach these temperatures whilst ",
                             "playing the game, but the benchmark is ",
                             "engineered so that the more CPU/GPU ",
                             "intensive tests are quicker, to avoid ",
                             "damage to hardware. The only data ",
                             "collected by this benchmark is scores ",
                             "on how your system has done, which ",
                             "can be used in the ADAPTIVE pre-set ",
                             "in settings, where settings are ",
                             "toggled automatically based on your ",
                             "performance in this test. No data ",
                             "is shared externally."))]

                stage = 0

                resize = False

                while True:
                    start_time = time.perf_counter()

                    display_utils.display_functionality.core_display_functions(
                        checkEvents=False)

                    if stage == -1:
                        pass

                    if stage == 0:
                        Registry.display.fill(Registry.background_color)
                        cover_Rect = pygame.Rect(
                            0,
                            0,
                            1280,
                            90)

                        pygame.draw.rect(
                            Registry.display,
                            Registry.background_color,
                            cover_Rect)

                        Registry.display.blit(
                            title_font,
                            ((Registry.real_window_width-title_width)/2, 0))

                        Registry.display.blit(
                            benchmark_font,
                            (((Registry.real_window_width-title_width)/2)+65, 50))

                        Ypos = 100
                        for i in range(len(benchmark_information_text)):
                            displacement = text_utils.text_wrap.blit_text(
                                    benchmark_information_text[i],
                                    (3, Ypos))
                                
                            Ypos += displacement

                    if stage == 1:
                        pygame.display.set_caption(
                            f"Pycraft: v{Registry.version}: Benchmark | Getting System Information")

                        CPUname = cpuinfo.get_cpu_info()["brand_raw"]
                        CPUcores = psutil.cpu_count(logical=False)
                        CPU_max_Freq = psutil.cpu_freq().max
                        CPUid = f"{CPUname} w/{CPUcores} cores @ {CPU_max_Freq} MHz"

                        RAMtotal = round((psutil.virtual_memory().total/1000000000), 2)
                        RAMpercent = psutil.virtual_memory().percent
                        RAMid = f"{RAMtotal} GB of memory, with {RAMpercent}% used"

                        CPUhwINFO = Registry.small_content_font.render(
                            CPUid,
                            Registry.aa,
                            Registry.font_color)
                        CPUhwINFOwidth = CPUhwINFO.get_width()

                        RAMhwINFO = Registry.small_content_font.render(
                            RAMid,
                            Registry.aa,
                            Registry.font_color)
                        RAMhwINFOwidth = RAMhwINFO.get_width()

                        stage += 1

                    if stage == 2:
                        try:
                            fps_Results = extended_benchmark.Loadbenchmark.run()
                            fpslistX = fps_Results[0]
                            fpslistY = fps_Results[1]
                            fpslistX2 = fps_Results[2]
                            fpslistY2 = fps_Results[3]
                            fpslistX3 = fps_Results[4]
                            fpslistY3 = fps_Results[5]
                            
                        except Exception as Message:
                            log_message = "benchmark > generate_benchmark > benchmark: "+str(Message)
                            
                            logging_utils.create_log_message.update_log_information(
                                log_message)
                            
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
                    
                            pygame.display.set_caption(
                                f"Pycraft: v{Registry.version}: Benchmark | Cancelled benchmark")

                            Registry.startup_animation = True
                            Registry.run_timer = 0
                            Registry.go_to = "home"
                            stage = -1
                            
                        else:
                            pygame.display.set_caption(
                                "".join((f"Pycraft: v{Registry.version}: Benchmark",
                                         "|",
                                         "Finished fps based benchmarks")))

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

                            stage += 1
                            
                    if stage == 3:
                        pygame.display.set_caption(
                            f"Pycraft: v{Registry.version}: Benchmark | Processing Results")
                        
                        try:
                            Max1 = max(fpslistY)
                            Min1 = min(fpslistY)

                            Max2 = max(fpslistY2)
                            Min2 = min(fpslistY2)

                            Max3 = max(fpslistY3)
                            Min3 = min(fpslistY3)
                        except Exception as Message:
                            log_message = "".join(("(User cancelled) benchmark ",
                                                       "> generate_benchmark > benchmark:",
                                                       f"{str(Message)}"))

                            logging_utils.create_log_message.update_log_information(
                                log_message)

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
                            
                            pygame.display.set_caption(
                                f"Pycraft: v{Registry.version}: Benchmark | Cancelled benchmark")

                            Registry.startup_animation = True
                            Registry.run_timer = 0
                            Registry.go_to = "home"

                        GlobalMaxArray = [Max1, Max2, Max3]

                        GlobalMax = max(GlobalMaxArray)

                        Registry.adaptive_fps = GlobalMax/2

                        temp = []
                        for i in range(len(fpslistY)):
                            relative_y = (300/GlobalMax) * fpslistY[i]
                            temp.append(130+(300-relative_y)) # 300
                        fpsListY = temp

                        temp = []
                        for i in range(len(fpslistY2)):
                            relative_y = (300/GlobalMax) * fpslistY2[i]
                            temp.append(130+(300-relative_y)) # 300
                        fpsListY2 = temp

                        temp = []
                        for i in range(len(fpslistY3)):
                            relative_y = (300/GlobalMax) * fpslistY3[i]
                            temp.append(130+(300-relative_y)) # 300
                        fpsListY3 = temp

                        multiplier = len(fpslistX)/(Registry.real_window_width-20)
                        Results1 = []
                        for i in range(len(fpslistY)):
                            Results1.append([(fpslistX[i]/multiplier), fpsListY[i]])

                        multiplier = len(fpslistX2)/(Registry.real_window_width-20)
                        Results2 = []
                        for i in range(len(fpslistY2)):
                            Results2.append([(fpslistX2[i]/multiplier), fpsListY2[i]])

                        multiplier = len(fpslistX3)/(Registry.real_window_width-20)
                        Results3 = []
                        for i in range(len(fpslistY3)):
                            Results3.append([(fpslistX3[i]/multiplier), fpsListY3[i]])

                        stage += 1

                    if stage == 4:
                        pygame.display.set_caption(
                            f"Pycraft: v{Registry.version}: Benchmark | Results")

                        Registry.display.fill(Registry.background_color)

                        Registry.display.blit(
                            title_font,
                            ((Registry.real_window_width-title_width)/2, 0))

                        Registry.display.blit(
                            benchmark_font,
                            (((Registry.real_window_width-title_width)/2)+65, 50))

                        fpsRect = pygame.Rect(
                            10,
                            130,
                            Registry.real_window_width-20,
                            300)

                        pygame.draw.rect(
                            Registry.display,
                            Registry.shape_color,
                            fpsRect,
                            0)

                        pygame.draw.lines(
                            Registry.display,
                            (255, 0, 0),
                            False,
                            Results1,
                            width=1)

                        pygame.draw.lines(
                            Registry.display,
                            (0, 255, 0),
                            False,
                            Results2,
                            width=1)

                        pygame.draw.lines(
                            Registry.display,
                            (0, 0, 255),
                            False,
                            Results3,
                            width=1)

                        pygame.draw.line(
                            Registry.display,
                            Registry.accent_color,
                            (10, int(130+(300-((300/GlobalMax)*60)))),
                            (Registry.real_window_width-20, int(130+(300-((300/GlobalMax)*60)))))

                        Registry.display.blit(
                            sixty_fps_data,
                            (13, int(130+(300-((300/GlobalMax)*60)))))

                        pygame.draw.line(
                            Registry.display,
                            Registry.accent_color,
                            (10, int(130+(300-((300/GlobalMax)*144)))),
                            (Registry.real_window_width-20, int(130+(300-((300/GlobalMax)*144)))))

                        Registry.display.blit(
                            one_four_four_fps_data,
                            (13, int(130+(300-((300/GlobalMax)*140)))))

                        pygame.draw.line(
                            Registry.display,
                            Registry.accent_color,
                            (10, int(130+(300-((300/GlobalMax)*240)))),
                            (Registry.real_window_width-20, int(130+(300-((300/GlobalMax)*240)))))

                        Registry.display.blit(two_forty_fps_data,
                                          (13, int(130+(300-((300/GlobalMax)*240)))))

                        HideRect = pygame.Rect(
                            0,
                            110,
                            Registry.real_window_width,
                            330)

                        pygame.draw.rect(
                            Registry.display,
                            Registry.background_color,
                            HideRect,
                            20)

                        Registry.display.blit(
                            fps_information_text,
                            ((Registry.real_window_width-fps_information_text_width)-3, 100))

                        Registry.display.blit(
                            file_information_text,
                            ((Registry.real_window_width-file_information_text_width)-3, 430))

                        Registry.display.blit(
                            hardware_information_text,
                            ((Registry.real_window_width-hardware_information_text_width)-3, 480))

                        Registry.display.blit(
                            CPUhwINFO,
                            ((Registry.real_window_width-CPUhwINFOwidth)-3, 500))

                        Registry.display.blit(
                            RAMhwINFO,
                            ((Registry.real_window_width-RAMhwINFOwidth)-3, 516))

                        RedResults = "".join(("Blank screen test (red); Minimum: ",
                                                f"{round(Min1, 4)} fps, Maximum: ",
                                                f"{round(Max1, 4)} fps"))

                        GreenResults = "".join(("Drawing screen test (green); Minimum: ",
                                                f"{round(Min2, 4)} fps, Maximum: ",
                                                f"{round(Max2, 4)} fps"))

                        BlueResults = "".join(("OpenGL screen test (blue); Minimum: ",
                                               f"{round(Min3, 4)} fps, Maximum: ",
                                               f"{round(Max3, 4)} fps"))

                        GreenInfo = Registry.small_content_font.render(
                            GreenResults,
                            Registry.aa,
                            Registry.font_color)

                        BlueInfo = Registry.small_content_font.render(
                            BlueResults,
                            Registry.aa,
                            Registry.font_color)

                        RedInfo = Registry.small_content_font.render(
                            RedResults,
                            Registry.aa,
                            Registry.font_color)

                        Registry.display.blit(
                            GreenInfo,
                            (3, 430))
                        Registry.display.blit(
                            BlueInfo,
                            (3, 445))
                        Registry.display.blit(
                            RedInfo,
                            (3, 460))

                        if resize:
                            stage = 4
                            resize = False

                    if Registry.use_mouse_input is False:
                        if (stage == 0 and
                                Registry.primary_mouse_button_down):

                            stage += 1

                        if Registry.joystick_exit:
                            Registry.joystick_exit = False
                            generate_benchmark.benchmark_exit()

                    for event in pygame.event.get():
                        if ((event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (event.key != pygame.K_SPACE) and
                                    stage <= 3) or
                            (event.type == pygame.KEYDOWN and
                                    event.key == pygame.K_ESCAPE)) and
                                Registry.use_mouse_input):

                            benchmark_utils.close_benchmark.exit_benchmark()
                            
                        if ((event.type == pygame.KEYDOWN and
                              event.key == pygame.K_SPACE) and
                            stage == 0):

                            stage += 1
                        if event.type == pygame.VIDEORESIZE:
                            resize = True

                    if Registry.go_to is None:
                        display_utils.display_animations.fade_in()
                            
                    else:
                        display_utils.display_animations.fade_out()

                    if Registry.startup_animation is False and (Registry.go_to is not None):
                        return None

                    target_fps = display_utils.display_utils.get_play_status()

                    pygame.display.flip()
                    Registry.clock.tick(target_fps)

                    Registry.run_timer += time.perf_counter()-start_time
                    
            except Exception as Message:
                error_message = "benchmark > generate_benchmark > benchmark: "+str(Message)

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
