if __name__ != "__main__":
    try:
        import os

        import moderngl_window
        
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
            
    class load_programs(Registry):
        def __init__(self):
            pass

        def load_program_text(ctx):
            particles_transform = ctx.program(
                vertex_shader='''
                    #version 330

                    in vec2 in_pos;
                    in vec2 in_vel;
                    in vec3 in_color;

                    out vec2 vs_vel;
                    out vec3 vs_color;

                    void main() {
                        gl_Position = vec4(in_pos, 1.0, 1.0);
                        vs_vel = in_vel;
                        vs_color = in_color;
                    }
                    ''',
                geometry_shader='''
                    #version 330

                    layout(points) in;
                    layout(points, max_vertices = 1) out;

                    uniform float gravity;
                    uniform float ft;

                    in vec2 vs_vel[1];
                    in vec3 vs_color[1];

                    out vec2 out_pos;
                    out vec2 out_vel;
                    out vec3 out_color;

                    void main() {
                        vec2 pos = gl_in[0].gl_Position.xy;
                        vec2 velocity = vs_vel[0];

                        if (pos.y > -1.0) {
                            vec2 vel = velocity + vec2(0.0, gravity);
                            out_pos = pos + vel * ft;
                            out_vel = vel;
                            if (out_pos.x == 0.0) {
                                out_pos.y = -1.1;
                            }
                            out_color = vs_color[0];
                            EmitVertex();
                            EndPrimitive();
                        }
                    }
                    ''',
                varyings=['out_pos', 'out_vel', 'out_color'],
            )

            gpu_emitter_particles = ctx.program(
                vertex_shader='''
                    # version 330
                    #define M_PI 3.1415926535897932384626433832795
                    uniform vec2 mouse_pos;
                    uniform vec2 mouse_vel;
                    uniform float time;

                    out vec2 out_pos;
                    out vec2 out_vel;
                    out vec3 out_color;

                    float rand(float n){
                        return fract(sin(n) * 43758.5453123);
                        }

                    void main() {
                        float a = mod(time * gl_VertexID, M_PI * 2.0);
                        float r = clamp(rand(time + gl_VertexID), 0.1, 0.9);
                        out_pos = mouse_pos;
                        out_vel = vec2(sin(a), cos(a)) * r + mouse_vel;
                        out_color = vec3(0.0, 0.0, rand(time * 2.0 + gl_VertexID));
                    }
                    ''',
                varyings=['out_pos', 'out_vel', 'out_color'],
            )

            return particles_transform, gpu_emitter_particles

        def load_program_files(wnd):
            shader_path = Registry.base_folder / "shaders"
            
            CloudsProgram = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "clouds.glsl")

            depth_prog = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "raw_depth.glsl")

            shadowmap = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "shadowmap.glsl")

            sun_prog = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "orbital_prog.glsl")

            moon_prog = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "orbital_prog.glsl")

            skysphere_prog = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "skysphere.glsl")

            particles_screen = moderngl_window.WindowConfig.load_program(
                wnd,
                path=shader_path / "particles_screen.glsl")

            return (CloudsProgram,
                        depth_prog,
                        shadowmap,
                        sun_prog,
                        moon_prog,
                        skysphere_prog,
                        particles_screen)

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
