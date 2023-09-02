if __name__ != "__main__":
    try:
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
            
    class draw_rose(Registry):
        def __init__(self):
            pass

        def create_rose(
                coloursARRAY,
                x_pos,
                y_pos,
                width,
                height):

            x_scale_factor = width/524
            y_scale_factor = height/524

            x_pos = x_pos-(51*x_scale_factor)
            y_pos = y_pos-(142*y_scale_factor)
            
            if coloursARRAY is False:
                coloursARRAY = []
                for _ in range(32):
                    coloursARRAY.append(Registry.shape_color)

            octagon = [((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos)]

            pygame.draw.polygon(
                Registry.display,
                Registry.shape_color,
                octagon,
                width=2)

            if Registry.aa:
                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[0],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[1],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[2],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[3],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[4],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))
                
                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[5],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[6],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[7],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[8],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[9],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[10],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[11],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[12],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[13],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[14],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[15],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[16],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[17],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[18],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[19],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[20],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[21],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[22],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[23],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[24],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[27],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[28],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[29],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[30],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    coloursARRAY[31],
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))
                
            else:
                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[0],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[1],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[2],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[3],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[4],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)
                
                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[5],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[6],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[7],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[8],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[9],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[10],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[11],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[12],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[13],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[14],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[15],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[16],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[17],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[18],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[19],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[20],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[21],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[22],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[23],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[24],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[27],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[28],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[29],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[30],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    coloursARRAY[31],
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

    class generate_graph(Registry):
        def __init__(self):
            pass

        def create_devmode_graph():
            if Registry.draw_devmode_graph:
                if ((Registry.real_window_width/2)+100)+Registry.timer >= Registry.real_window_width:
                    Registry.data_average_fps = []
                    Registry.data_CPU_usage = []
                    Registry.data_current_fps = []
                    Registry.data_memory_usage = []

                    Registry.timer = 0

                    Registry.data_average_fps_Max = 1
                    Registry.data_current_fps_Max = 1
                    Registry.data_memory_usage_Max = 50
                    Registry.data_CPU_usage_Max = 50

                BackingRect = pygame.Rect(
                    (Registry.real_window_width/2)+100,
                    0,
                    Registry.real_window_width,
                    200)

                pygame.draw.rect(
                    Registry.display,
                    Registry.shape_color,
                    BackingRect)

                SwapMemory = psutil.swap_memory()
                VirtualMemory = psutil.virtual_memory()

                TotalMemory = SwapMemory.total+VirtualMemory.total
                UsedMemory = SwapMemory.used+VirtualMemory.used

                current_memory_usage = (100/TotalMemory)*(UsedMemory)

                if Registry.timer >= 2:
                    Registry.data_average_fps.append(
                        [((Registry.real_window_width/2)+100)+timer,
                            200-(100/data_average_fps_Max)*(Registry.average_fps/(Registry.iteration))])

                    try:
                        Registry.data_current_fps.append(
                            [((Registry.real_window_width/2)+100)+timer,
                                200-(100/Registry.data_current_fps_Max)*int(Registry.current_fps)])

                    except:
                        Registry.data_current_fps.append(
                            [((Registry.real_window_width/2)+100)+timer,
                                200-(100/Registry.data_current_fps_Max)*int(2000)])

                    Registry.data_memory_usage.append(
                        [((Registry.real_window_width/2)+100)+timer,
                            200-(2)*current_memory_usage])

                if Registry.fps_overclock:
                    data_average_fps_Max = 2000
                elif (Registry.average_fps/(Registry.iteration)) > data_average_fps_Max:
                    data_average_fps_Max = (Registry.average_fps/(Registry.iteration))

                if Registry.current_fps > data_current_fps_Max:
                    data_current_fps_Max = Registry.current_fps

                if current_memory_usage > data_memory_usage_Max:
                    data_memory_usage_Max = current_memory_usage

                Registry.timer += 0.2
                if Registry.timer >= 5:
                    pygame.draw.lines(
                        Registry.display,
                        (255, 0, 0),
                        False,
                        Registry.data_average_fps)

                    pygame.draw.lines(
                        Registry.display,
                        (0, 255, 0),
                        False,
                        Registry.data_current_fps)

                    pygame.draw.lines(
                        Registry.display,
                        (0, 0, 255),
                        False,
                        Registry.data_memory_usage)

                if len(Registry.data_CPU_usage) >= 2:
                    pygame.draw.lines(
                        Registry.display,
                        (255, 0, 255),
                        False,
                        Registry.data_CPU_usage)

                if Registry.fps_overclock:
                    try:
                        runFont = Registry.small_content_font.render(
                            "".join((f"MemUsE: {int(current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"fps: {Registry.fps} current_fps: {int(Registry.current_fps)} average_fps: ",
                                        f"N/A iteration: {Registry.iteration}")),
                            Registry.aa,
                            (255, 255, 255))

                    except:
                        runFont = Registry.small_content_font.render(
                            "".join((f"MemUsE: {int(current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"fps: {Registry.fps} current_fps: NaN* average_fps: ",
                                        f"N/A iteration: {Registry.iteration}")),
                            Registry.aa,
                            (255, 255, 255))
                else:
                    runFont = Registry.small_content_font.render(
                        "".join((f"MemUsE: {int(current_memory_usage)}% | ",
                                    f"CPUUsE: {psutil.cpu_percent()}% | ",
                                    f"fps: {Registry.fps} current_fps: {int(Registry.current_fps)} average_fps: ",
                                    f"{int(Registry.average_fps/Registry.iteration)} ",
                                    f"iteration: {Registry.iteration}")),
                        Registry.aa,
                        (255, 255, 255))

                Registry.display.blit(
                    runFont,
                    ((Registry.real_window_width/2)+105, 0))

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
