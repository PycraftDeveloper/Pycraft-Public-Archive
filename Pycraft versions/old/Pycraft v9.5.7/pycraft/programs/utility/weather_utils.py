if __name__ != "__main__":
    try:
        import os
        import random
        
        from PIL import Image
        from matplotlib import cm
        import numpy
        import send2trash
        
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
            
    class compute_weather(Registry):
        # 0 = transparent
        # 1 = opaque
        def __init__(self):
            pass

        def compute_cloud_model(size):
            vertices = numpy.dstack(
                numpy.mgrid[0:size, 0:size][::-1]) / size

            temp = numpy.dstack(
                [numpy.arange(0, size * size - size),
                numpy.arange(size, size * size)])

            index = numpy.pad(
                temp.reshape(size - 1, 2 * size),
                [[0, 0], [0, 1]],
                "constant",
                constant_values=-1)

            return vertices, index

        def generate_perlin_noise_2d(shape, res):
            def f(t):
                return 6*t**5 - 15*t**4 + 10*t**3

            delta = (res[0] / shape[0], res[1] / shape[1])
            d = (shape[0] // res[0], shape[1] // res[1])
            grid = numpy.mgrid[0:res[0]:delta[0],0:res[1]:delta[1]].transpose(1, 2, 0) % 1
            # Gradients
            angles = 2*numpy.pi*numpy.random.rand(res[0]+1, res[1]+1)
            gradients = numpy.dstack((numpy.cos(angles), numpy.sin(angles)))
            g00 = gradients[0:-1,0:-1].repeat(d[0], 0).repeat(d[1], 1)
            g10 = gradients[1:,0:-1].repeat(d[0], 0).repeat(d[1], 1)
            g01 = gradients[0:-1,1:].repeat(d[0], 0).repeat(d[1], 1)
            g11 = gradients[1:,1:].repeat(d[0], 0).repeat(d[1], 1)
            # Ramps
            n00 = numpy.sum(grid * g00, 2)
            n10 = numpy.sum(numpy.dstack((grid[:,:,0]-1, grid[:,:,1])) * g10, 2)
            n01 = numpy.sum(numpy.dstack((grid[:,:,0], grid[:,:,1]-1)) * g01, 2)
            n11 = numpy.sum(numpy.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
            # Interpolation
            t = f(grid)
            n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
            n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
            return numpy.sqrt(2)*((1-t[:,:,1])*n0 + t[:,:,1]*n1)
            
        def compute_cloud_noise(
                shape):
            
            world = compute_weather.generate_perlin_noise_2d(
                shape,
                (25, 25)) # multiple of shape[0]

            CloudData = world

            if Registry.remove_file_permission:
                image = Image.fromarray(
                    numpy.uint8(
                        cm.gist_earth(world)*255))

                noise_image_path = Registry.base_folder / "resources" / "game engine resources" / "clouds" / "Rnd_noise.png"

                try:
                    send2trash.send2trash(noise_image_path)
                    
                except Exception as Message:
                    log_message = "".join(("Unable to clear the previous Perlin-noise image, ",
                                        "attempting to overwrite instead. More Details:",
                                        str(Message)))

                    logging_utils.create_log_message.update_log_warning(
                        log_message)
                    
                image.save(noise_image_path)

                image.close()
            return CloudData

        def blend_weather(
                    PreviousWeather,
                    WeatherTime,
                    shadowmap,
                    Previous_Fog_Distance_Min,
                    Previous_Fog_Distance_Max,
                    Previous_color,
                    color,
                    CloudsProgram,
                    Previous_CloudsProgram_Alpha,
                    Previous_CloudsProgram_CloudColor,
                    Previous_multiplier,
                    CloudHeightMultiplier,
                    skysphere_prog,
                    Previous_prog_transparency,
                    skysphere_prog_Transparency):
            
            def mix(start, end, time, duration):
                return (((end-start)/duration)*time)+start

            if Registry.weather != PreviousWeather and WeatherTime < 3:
                if Registry.weather == "sunny":
                    shadowmap["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        1200.0,
                        WeatherTime,
                        3)

                    shadowmap["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1600.0,
                        WeatherTime,
                        3)

                    Temporary_color = mix(
                        Previous_color,
                        1.0,
                        WeatherTime,
                        3)

                    color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    CloudsProgram["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        1200.0,
                        WeatherTime,
                        3)

                    CloudsProgram["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1600.0,
                        WeatherTime,
                        3)

                    CloudsProgram["WeatherAlpha"] = mix(
                        Previous_CloudsProgram_Alpha,
                        0.0,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudColor"] = mix(
                        Previous_CloudsProgram_CloudColor,
                        1.0,
                        WeatherTime,
                        3)

                    multiplier = mix(
                        Previous_multiplier,
                        CloudHeightMultiplier,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudHeightMultiplier"] = multiplier

                    skysphere_prog["transparency"] = mix(
                        Previous_prog_transparency,
                        1.0,
                        WeatherTime,
                        3)

                elif Registry.weather == "rain.light":
                    shadowmap["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        1000.0,
                        WeatherTime,
                        3)

                    shadowmap["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1600.0,
                        WeatherTime,
                        3)

                    Temporary_color = mix(
                        Previous_color,
                        0.8,
                        WeatherTime,
                        3)

                    color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    CloudsProgram["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        1200.0,
                        WeatherTime,
                        3)

                    CloudsProgram["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1600.0,
                        WeatherTime,
                        3)

                    CloudsProgram["WeatherAlpha"] = mix(
                        Previous_CloudsProgram_Alpha,
                        0.75,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudColor"] = mix(
                        Previous_CloudsProgram_CloudColor,
                        0.75,
                        WeatherTime,
                        3)

                    multiplier = mix(
                        Previous_multiplier,
                        CloudHeightMultiplier,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudHeightMultiplier"] = multiplier

                    skysphere_prog["transparency"] = mix(
                        Previous_prog_transparency,
                        skysphere_prog_Transparency,
                        WeatherTime,
                        3)

                elif Registry.weather == "rain.heavy":
                    shadowmap["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        1000.0,
                        WeatherTime,
                        3)

                    shadowmap["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1600.0,
                        WeatherTime,
                        3)

                    Temporary_color = mix(
                        Previous_color,
                        0.7,
                        WeatherTime,
                        3)

                    color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    CloudsProgram["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        800.0,
                        WeatherTime,
                        3)

                    CloudsProgram["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1200.0,
                        WeatherTime,
                        3)

                    CloudsProgram["WeatherAlpha"] = mix(
                        Previous_CloudsProgram_Alpha,
                        1.0,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudColor"] = mix(
                        Previous_CloudsProgram_CloudColor,
                        0.35,
                        WeatherTime,
                        3)

                    multiplier = mix(
                        Previous_multiplier,
                        CloudHeightMultiplier,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudHeightMultiplier"] = multiplier

                    skysphere_prog["transparency"] = mix(
                        Previous_prog_transparency,
                        skysphere_prog_Transparency,
                        WeatherTime,
                        3)

                else:
                    shadowmap["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        600.0,
                        WeatherTime,
                        3)

                    shadowmap["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        800.0,
                        WeatherTime,
                        3)

                    Temporary_color = mix(
                        Previous_color,
                        0.6,
                        WeatherTime,
                        3)

                    color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    CloudsProgram["w_min"] = mix(
                        Previous_Fog_Distance_Min,
                        800.0,
                        WeatherTime,
                        3)

                    CloudsProgram["w_max"] = mix(
                        Previous_Fog_Distance_Max,
                        1200.0,
                        WeatherTime,
                        3)

                    CloudsProgram["WeatherAlpha"] = mix(
                        Previous_CloudsProgram_Alpha,
                        1.0,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudColor"] = mix(
                        Previous_CloudsProgram_CloudColor,
                        0.25,
                        WeatherTime,
                        3)

                    multiplier = mix(
                        Previous_multiplier,
                        CloudHeightMultiplier,
                        WeatherTime,
                        3)

                    CloudsProgram["CloudHeightMultiplier"] = multiplier

                    skysphere_prog["transparency"] = mix(
                        Previous_prog_transparency,
                        skysphere_prog_Transparency,
                        WeatherTime,
                        3)

            else:
                if Registry.weather == "sunny":
                    color.value = (1.0, 1.0, 1.0)

                elif Registry.weather == "rain.light":
                    color.value = (0.8, 0.8, 0.8)

                elif Registry.weather == "rain.heavy":
                    color.value = (0.7, 0.7, 0.7)

                else:
                    color.value = (0.6, 0.6, 0.6)

        def compute_weather(
                color,
                shadowmap,
                CloudsProgram,
                skysphere_prog,
                Time_Percent):
            
            LengthenStorm = False
            weather = ""
            skysphere_prog_Transparency = 0.0
            if random.randint(0, 100) <= 65:
                weather += "sunny"

                color.value = (1.0, 1.0, 1.0)

                shadowmap["w_min"] = 1200.0
                shadowmap["w_max"] = 1600.0

                CloudsProgram["w_min"] = 1200.0
                CloudsProgram["w_max"] = 1600.0
                CloudsProgram["WeatherAlpha"] = 0.0
                CloudsProgram["CloudColor"] = 1.0

                CloudHeightMultiplier = random.randint(1, 500)
                CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                skysphere_prog["transparency"] = 1.0

            else:
                weather += "rain"

                if random.randint(0, 100) <= 80:
                    weather += ".light"

                    color.value = (0.8, 0.8, 0.8)

                    shadowmap["w_min"] = 1000.0
                    shadowmap["w_max"] = 1600.0

                    CloudsProgram["w_min"] = 1000.0
                    CloudsProgram["w_max"] = 1600.0
                    CloudsProgram["WeatherAlpha"] = 0.75
                    CloudsProgram["CloudColor"] = 0.75

                    CloudHeightMultiplier = random.randint(139, 500)
                    CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                    if Time_Percent > 50: # night
                        skysphere_prog_Transparency = random.randint(35, 50)/100
                    else: # day
                        skysphere_prog_Transparency = random.randint(25, 40)/100
                    skysphere_prog["transparency"] = skysphere_prog_Transparency

                else:
                    weather += ".heavy"
                    CloudsProgram["WeatherAlpha"] = 1

                    if random.randint(0, 100) <= 50:
                        weather += ".thundery"

                        color.value = (0.6, 0.6, 0.6)

                        LengthenStorm = True

                        shadowmap["w_min"] = 600.0
                        shadowmap["w_max"] = 800.0

                        CloudsProgram["w_min"] = 600.0
                        CloudsProgram["w_max"] = 800.0
                        CloudsProgram["CloudColor"] = 0.25

                        CloudHeightMultiplier = random.randint(
                            278,
                            500)

                        CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                        skysphere_prog_Transparency = random.randint(0, 25)/100
                        skysphere_prog["transparency"] = skysphere_prog_Transparency

                    else:
                        color.value = (0.7, 0.7, 0.7)

                        shadowmap["w_min"] = 800.0
                        shadowmap["w_max"] = 1200.0

                        CloudsProgram["w_min"] = 800.0
                        CloudsProgram["w_max"] = 1200.0
                        CloudsProgram["CloudColor"] = 0.35

                        CloudHeightMultiplier = random.randint(
                            361,
                            500)

                        CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                        skysphere_prog_Transparency = random.randint(10, 45)/100
                        skysphere_prog["transparency"] = skysphere_prog_Transparency

            return LengthenStorm, CloudHeightMultiplier, skysphere_prog_Transparency

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