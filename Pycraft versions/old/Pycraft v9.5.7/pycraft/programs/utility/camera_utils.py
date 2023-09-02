if __name__ != "__main__":
    try:
        import time

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

    class compute_camera(Registry):
        """
            NYI
            
            - Args:
                - None
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
        def __init__(self):
            pass

        def camera_move_state(
                camera,
                direction,
                activate):
            
            if direction == Registry.RIGHT:
                camera._xdir = Registry.POSITIVE if activate else Registry.STILL
            if direction == Registry.LEFT:
                camera._xdir = Registry.NEGATIVE if activate else Registry.STILL
            if direction == Registry.FORWARD:
                camera._zdir = Registry.NEGATIVE if activate else Registry.STILL
            if direction == Registry.BACKWARD:
                camera._zdir = Registry.POSITIVE if activate else Registry.STILL
            if direction == Registry.UP:
                camera._ydir = Registry.POSITIVE if activate else Registry.STILL
            if direction == Registry.DOWN:
                camera._ydir = Registry.NEGATIVE if activate else Registry.STILL

        def get_camera_values(
                camera,
                camera_up):

            position = camera.position

            compute_camera.compute_camera_dir(
                camera)

            if Registry.compile_math:
                cam_matrix = math_utils.compiled_math_functions.gl_look_at(
                    position, position + camera.dir, camera_up)  # slow but works
                
            else:
                cam_matrix = math_utils.math_functions.gl_look_at(
                    position, position + camera.dir, camera_up)  # slow but works

            return cam_matrix, position
            
        def compute_camera_dir(
                camera):
            
            # Use separate time in camera so we can move it when the demo is paused
            now = time.time()
            # If the camera has been inactive for a while, a large time delta
            # can suddenly move the camera far away from the scene
            t = max(now - camera._last_time, 0)
            camera._last_time = now

            # X Movement
            if camera._xdir == Registry.POSITIVE:
                camera.position += camera.right * camera._velocity * t
            elif camera._xdir == Registry.NEGATIVE:
                camera.position -= camera.right * camera._velocity * t

            # Z Movement
            if camera._zdir == Registry.NEGATIVE:
                camera.position += camera.dir * camera._velocity * t
            elif camera._zdir == Registry.POSITIVE:
                camera.position -= camera.dir * camera._velocity * t

            # Y Movement
            if camera._ydir == Registry.POSITIVE:
                camera.position += camera.up * camera._velocity * t
            elif camera._ydir == Registry.NEGATIVE:
                camera.position -= camera.up * camera._velocity * t
                
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
