if __name__ != "__main__":
    try:
        import random
        import math
        
        import moderngl
        import numpy
        import pyrr
        
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
            
    class particles(Registry):
        def __init__(self):
            pass

        def emit_gpu(query,
                transform_vao1,
                vbo2,
                N,
                emit_buffer_elements,
                max_emit_count,
                gpu_emitter_particles,
                weather,
                time,
                gpu_emitter_vao,
                stride,
                render_vao2,
                active_particles):
            # Transform all particles recoding how many elements were emitted by geometry shader
            with query:
                transform_vao1.transform(
                    vbo2,
                    moderngl.POINTS,
                    vertices=active_particles)

            emit_count = min(N - query.primitives,
                            emit_buffer_elements,
                            max_emit_count)

            if emit_count > 0:
                gpu_emitter_particles["mouse_pos"].value = (0, 2)

                if weather == "rain.light":
                    gpu_emitter_particles["mouse_vel"].value = (
                        0,
                        random.randint(50, 100)/100)

                if weather == "rain.heavy":
                    gpu_emitter_particles["mouse_vel"].value = (
                        0,
                        random.randint(75, 125)/100)

                if weather == "rain.heavy.thundery":
                    gpu_emitter_particles["mouse_vel"].value = (
                        0,
                        random.randint(75, 150)/100)

                gpu_emitter_particles["time"].value = max(time, 0)
                gpu_emitter_vao.transform(
                    vbo2,
                    vertices=emit_count,
                    buffer_offset=query.primitives * stride)

            active_particles = query.primitives + emit_count
            render_vao2.render(
                moderngl.POINTS, vertices=active_particles)

            return active_particles

        def gen_particles(n):
            for _ in range(n):
                # Current mouse position (2 floats)
                yield 0
                yield 2
                # Random velocity (2 floats)
                a = numpy.random.uniform(
                    0.0, numpy.pi * 2.0)
                r = numpy.random.uniform(0.1, 0.9)
                yield math.cos(a) * r + 0
                yield math.sin(a) * r + 0
                # Random color (4 floats)
                yield 0.0
                yield 0.0
                if Registry.fancy_particles:
                    yield numpy.random.uniform(0.0, 1.0)
                else:
                    yield 1.0

        def projection(wnd):
            return pyrr.matrix44.create_orthogonal_projection(
                -wnd.aspect_ratio, wnd.aspect_ratio,
                -1, 1,
                -1, 100,
                dtype='f4',
            )

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
