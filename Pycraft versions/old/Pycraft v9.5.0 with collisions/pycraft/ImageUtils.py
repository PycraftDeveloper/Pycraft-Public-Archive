if not __name__ == "__main__":
    print("Started <Pycraft_ImageUtils>")
    class ConvertImage:
        def __init__(self):
            pass

        def pilImageToSurface(self, pilImage):
            return self.mod_Pygame__.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()