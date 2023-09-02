if __name__ != "__main__":
    try:
        import math

        import pyrr
        import numpy
        import numba
        
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
            
    class math_functions(Registry):
        def __init__(self):
            pass

        def gl_look_at(pos, target, up):
            x, y, z = math_functions.compute_position(
                pos, target, up)

            translate = pyrr.Matrix44.identity(dtype="f4")
            translate[3][0] = -pos.x
            translate[3][1] = -pos.y
            translate[3][2] = -pos.z

            rotate = pyrr.Matrix44.identity(dtype="f4")
            rotate[0][0] = x[0]  # -- X
            rotate[1][0] = x[1]
            rotate[2][0] = x[2]
            rotate[0][1] = y[0]  # -- Y
            rotate[1][1] = y[1]
            rotate[2][1] = y[2]
            rotate[0][2] = z[0]  # -- Z
            rotate[1][2] = z[1]
            rotate[2][2] = z[2]

            return rotate * translate[:, numpy.newaxis]

        def normalize(v):
            norm = numpy.linalg.norm(v)
            if norm == 0:
                return v
            return v / norm

        def compute_position(pos, target, up):
            z = math_functions.normalize(pos - target)
            x = math_functions.normalize(numpy.cross(math_functions.normalize(up), z))
            y = numpy.cross(z, x)
            return x, y, z

        def perspective_fov(fov, aspect_ratio, near_plane, far_plane):
            num = 1.0 / math.tan(fov / 2.0)
            num9 = num / aspect_ratio
            return numpy.array([
                [num9, 0.0, 0.0, 0.0],
                [0.0, num, 0.0, 0.0],
                [0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
                [0.0, 0.0, (near_plane * far_plane) /
                 (near_plane - far_plane), 0.0]
            ], dtype="f4")

        def look_at(camera_position, camera_target, up_vector):
            vector = camera_target - camera_position

            x = numpy.linalg.norm(vector)
            vector = vector / x

            vector2 = numpy.cross(up_vector, vector)
            vector2 = vector2 / numpy.linalg.norm(vector2)

            vector3 = numpy.cross(vector, vector2)
            return numpy.array([
                [vector2[0], vector3[0], vector[0], 0.0],
                [vector2[1], vector3[1], vector[1], 0.0],
                [vector2[2], vector3[2], vector[2], 0.0],
                [-numpy.dot(vector2, camera_position), -numpy.dot(
                    vector3, camera_position), numpy.dot(vector, camera_position), 1.0]
            ], dtype="f4")

        def multiply(light_proj, sun_light_look_at):
            return light_proj * sun_light_look_at

    class compiled_math_functions(Registry):
        def __init__(self):
            pass

        def gl_look_at(pos, target, up):
            x, y, z = compiled_math_functions.compute_position(
                pos, target, up)

            translate = pyrr.Matrix44.identity(dtype="f4")
            translate[3][0] = -pos.x
            translate[3][1] = -pos.y
            translate[3][2] = -pos.z

            rotate = pyrr.Matrix44.identity(dtype="f4")
            rotate[0][0] = x[0]  # -- X
            rotate[1][0] = x[1]
            rotate[2][0] = x[2]
            rotate[0][1] = y[0]  # -- Y
            rotate[1][1] = y[1]
            rotate[2][1] = y[2]
            rotate[0][2] = z[0]  # -- Z
            rotate[1][2] = z[1]
            rotate[2][2] = z[2]

            return rotate * translate[:, numpy.newaxis]

        @numba.njit(fastmath=True, cache=True)
        def compute_position(pos, target, up):
            def normalize(v):
                norm = numpy.linalg.norm(v)
                if norm == 0:
                    return v
                return v / norm
            
            z = normalize(pos - target)
            x = normalize(numpy.cross(normalize(up), z))
            y = numpy.cross(z, x)
            return x, y, z

        @numba.njit(fastmath=True, cache=True)
        def perspective_fov(fov, aspect_ratio, near_plane, far_plane):
            num = 1.0 / math.tan(fov / 2.0)
            num9 = num / aspect_ratio
            return numpy.array([
                [num9, 0.0, 0.0, 0.0],
                [0.0, num, 0.0, 0.0],
                [0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
                [0.0, 0.0, (near_plane * far_plane) /
                 (near_plane - far_plane), 0.0]
            ], dtype="f4")

        @numba.njit(fastmath=True, cache=True)
        def look_at(camera_position, camera_target, up_vector):
            vector = camera_target - camera_position

            x = numpy.linalg.norm(vector)
            vector = vector / x

            vector2 = numpy.cross(up_vector, vector)
            vector2 = vector2 / numpy.linalg.norm(vector2)

            vector3 = numpy.cross(vector, vector2)
            return numpy.array([
                [vector2[0], vector3[0], vector[0], 0.0],
                [vector2[1], vector3[1], vector[1], 0.0],
                [vector2[2], vector3[2], vector[2], 0.0],
                [-numpy.dot(vector2, camera_position), -numpy.dot(
                    vector3, camera_position), numpy.dot(vector, camera_position), 1.0]
            ], dtype="f4")

        @numba.njit(fastmath=True, cache=True)
        def multiply(light_proj, sun_light_look_at):
            return light_proj * sun_light_look_at

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
