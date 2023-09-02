if __name__ != "__main__":
    try:
        import math

        import numpy
        import pyrr
        
        from registry_utils import Registry

        import math_utils
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
            
    class shadowmapping_mathematics(Registry):
        def __init__(self):
            pass

        def compute_celestial_entities(
                skybox_distance,
                sun_radius,
                sun_prog,
                moon_prog,
                scene_pos,
                projection_matrix,
                matrix,
                position):
            
            distance = (skybox_distance-sun_radius)/1.355

            if Registry.game_time >= 1056:
                Registry.game_time = 0
                Registry.day += 1

            sun_prepro_time = (Registry.game_time/168)-1.5707975

            SunPos_YZ = math.cos(
                sun_prepro_time) * distance

            SunPos_X = math.sin(
                sun_prepro_time) * distance

            sun_lightpos = numpy.array(
                (SunPos_X + position.x,
                    SunPos_YZ + position.y,
                    0),
                dtype="f4")

            moon_prepro_time = (Registry.game_time/168)-4.7123925

            MoonPos_YZ = math.cos(
                moon_prepro_time) * distance
            MoonPos_X = math.sin(
                moon_prepro_time) * distance

            moon_lightpos = numpy.array(
                (MoonPos_X + position.x,
                    MoonPos_YZ + position.y,
                    0),
                dtype="f4")

            sun_prog["m_proj"].write(projection_matrix)
            sun_prog["m_camera"].write(matrix)
            sun_prog["m_model"].write(
                pyrr.Matrix44.from_translation(
                    sun_lightpos + scene_pos,
                    dtype="f4"))

            moon_prog["m_proj"].write(projection_matrix)
            moon_prog["m_camera"].write(matrix)
            moon_prog["m_model"].write(
                pyrr.Matrix44.from_translation(
                    moon_lightpos + scene_pos,
                    dtype="f4"))

            return sun_lightpos, moon_lightpos

        def compute_shadows(
                mvp,
                light,
                sun_lightpos,
                aspect_ratio,
                mvp_depth,
                mvp_shadow,
                bias_matrix,
                projection,
                matrix,
                target,
                up):
            
            mvp[0].write(projection.astype("f4").tobytes())
            mvp[1].write(matrix.astype("f4").tobytes())

            # build light camera
            light.value = tuple(sun_lightpos)

            if Registry.compile_math:
                sun_light_look_at = math_utils.compiled_math_functions.look_at(
                    sun_lightpos,
                    target,
                    up)
                
            else:
                sun_light_look_at = math_utils.math_functions.look_at(
                    sun_lightpos,
                    target,
                    up)

            if Registry.compile_math:
                # light projection matrix (scene dependant)
                light_proj = math_utils.compiled_math_functions.perspective_fov(
                    90.0 / 2,
                    aspect_ratio,
                    0.01,
                    2000.0)

            else:
                # light projection matrix (scene dependant)
                light_proj = math_utils.math_functions.perspective_fov(
                    90.0 / 2,
                    aspect_ratio,
                    0.01,
                    2000.0)

            if Registry.compile_math:
                # light model view projection matrix
                mvp_light = math_utils.compiled_math_functions.multiply(
                    light_proj,
                    sun_light_look_at)

            else:
                # light model view projection matrix
                mvp_light = math_utils.math_functions.multiply(
                    light_proj,
                    sun_light_look_at)

            # send uniforms to shaders
            mvp_depth[0].write(bias_matrix.astype("f4").tobytes())
            mvp_depth[1].write(mvp_light.astype("f4").tobytes())
            mvp_shadow.write(mvp_light.astype("f4").tobytes())

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
