if __name__ != "__main__":
    try:
        import os
        import time
        
        import pygame
        import numpy
        import moderngl
        import moderngl_window
        import pyrr
        
        from registry_utils import Registry
        
        import benchmark_utils
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
            
    class run_opengl_window_benchmark(Registry):
        """
        This class is in charge of the OpenGL window benchmark seen in the benchmark
        section of Pycraft.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def setup(
                self,
                wnd):
            """
            This subroutine is in charge of loading the resources required by the OpenGL
            benchmark, including:
            1x Texture
            1x 3D Scene
            1x GLSL Shader
            And also sets the window parameters so that the OpenGL benchmark sets up in the
            same way on all devices for consistency.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - wnd (BaseWindow): This is used by ModernGL_window as the display object to
                    use for rendering and additional resource loading.
                    
            - Keyword Args:
                - None

            - Output:
                - texture (ModernGL_window Texture): This texture is rendered to the scene to
                    add additional complexity.
                - mvp (ModernGL_window Shader Attribute): This matrix is used to render the
                    position and rotation of the scene.
                - light (ModernGL_window Shader Attribute): This attribute is used to shade
                    the scene based on the position of the camera.
                - vao (ModernGL VertexArray): This is the scene we render (a cube).
                - timer (float): This is used to keep track of how long this section of the
                    benchmark has been running for, and is used in calculating the rotation
                    of our scene.
                - aspect_ratio (float): This float represents the aspect ratio we want our display
                    to be rendering at.
            """
            wnd.vsync = False
            wnd.samples = 1
            wnd.size = 1280, 720

            benchmark_shader_path = Registry.base_folder / "shaders" / "benchmark.glsl"
            benchmark_scene_path = Registry.base_folder / "resources" / "benchmark resources" / "Crate.obj"
            benchmark_texture_path = Registry.base_folder / "resources" / "benchmark resources" / "Crate.png"

            prog = moderngl_window.WindowConfig.load_program(
                wnd,
                benchmark_shader_path)

            scene = moderngl_window.WindowConfig.load_scene(
                wnd,
                benchmark_scene_path)

            texture = moderngl_window.WindowConfig.load_texture_2d(
                wnd,
                benchmark_texture_path)

            mvp = prog["Mvp"]
            light = prog["Light"]
            vao = scene.root_nodes[0].mesh.vao.instance(prog)

            timer = 0
            aspect_ratio = 16/9
            
            return texture, mvp, light, vao, timer, aspect_ratio

        def start(
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
                aspect_ratio):
            
            fpslistX = []
            fpslistY = []
            start_time = time.perf_counter()
            while iteration < 500*Setfpslength:
                pygame.display.set_caption("".join((f"Pycraft: v{Registry.version}: ",
                    "benchmark | Running OpenGL benchmark ",
                     f"@ {Setfps[fpscounter]} fps")))
                
                while iteration != Maxiteration:
                    if not Registry.clock.get_fps() == 0:
                        fpslistX.append(iteration)
                        fpslistY.append(Registry.clock.get_fps())
                        

                    angle = timer
                    ctx.clear(
                        0.0,
                        0.0,
                        0.0)

                    ctx.enable(moderngl.DEPTH_TEST)

                    camera_pos = (
                        numpy.cos(angle) * 3.0,
                        numpy.sin(angle) * 3.0,
                        2.0)

                    proj = pyrr.Matrix44.perspective_projection(
                        45.0,
                        aspect_ratio,
                        0.1,
                        100.0)

                    lookat = pyrr.Matrix44.look_at(
                        camera_pos,
                        (0.0, 0.0, 0.5),
                        (0.0, 0.0, 1.0),
                    )

                    mvp.write((proj * lookat).astype("f4"))
                    light.value = camera_pos
                    texture.use()
                    vao.render()

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (not event.key == pygame.K_SPACE))):

                            benchmark_utils.close_benchmark.exit_benchmark()

                    pygame.display.flip()
                    iteration += 1
                    Registry.clock.tick(Setfps[fpscounter])

                    timer = time.perf_counter()-start_time
                    
                fpscounter += 1
                Maxiteration += 500
                
            return fpslistX, fpslistY

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