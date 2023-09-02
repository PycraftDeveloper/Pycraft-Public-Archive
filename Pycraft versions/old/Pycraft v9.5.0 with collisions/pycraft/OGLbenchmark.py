if not __name__ == "__main__":
    print("Started <Pycraft_OGLBenchmark>")
    class LoadOGLBenchmark:
        def __init__(self):
            pass

        def Cube(self, edges, vertices):
            self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_LINES)
            for edge in edges:
                for vertex in edge:
                    self.mod_OpenGL_GL_.glVertex3fv(vertices[vertex])
            self.mod_OpenGL_GL_.glEnd()

        def CreateBenchmark(self):
            self.mod_OpenGL_GLU_.gluPerspective(45, (1280/720), 0.1, 50.0)
            self.mod_OpenGL_GL_.glTranslatef(0.0,0.0, -5)

        def RunBenchmark(self, edges, vertices):
            self.mod_OpenGL_GL_.glRotatef(1, 3, 1, 1)
            self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)
            LoadOGLBenchmark.Cube(self, edges, vertices)
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()