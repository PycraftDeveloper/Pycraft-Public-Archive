if __name__ != "__main__":
    try:
        from tkinter import messagebox
        import tkinter
        
        import pygame
        from PIL import Image
        from PIL import ImageTk
        from PIL import ImageFilter
        from PIL import ImageEnhance
        
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
    
    class convert_image(Registry):
        def __init__(self):
            pass

        def pil_image_to_surface(pilImage):
            return pygame.image.fromstring(
                pilImage.tobytes(),
                pilImage.size,
                pilImage.mode)

        def surface_to_pil_image(display):
            return Image.frombytes(
                "RGBA",
                display.get_size(),
                pygame_image_extensions.display_to_string(display),
                "raw")

    class pygame_image_extensions(Registry):
        def __init__(self):
            pass

        def display_to_string(display):
            surface_image = pygame.image.tostring(
                    display,
                    "RGBA")
            
            return surface_image

    class transparency_effects(Registry):
        def __init__(self):
            pass

        def create_background_image(image, darken=False):
            display_size = Registry.display.get_size()

            if Registry.fancy_graphics:
                blurred_image = image.filter(ImageFilter.GaussianBlur(2))
            else:
                blurred_image = image.filter(ImageFilter.BoxBlur(2))
                
            if darken:
                img = ImageEnhance.Brightness(blurred_image)
                blurred_image = img.enhance(0.5)
                
            enhancer = ImageEnhance.Sharpness(blurred_image)

            enhanced_image = enhancer.enhance(0.0)
                
            image = enhanced_image.resize(display_size)
            
            return image

    class tkinter_installer(Registry):
        def __init__(self):
            pass

        def open_img(root, file, offset_x=-3, offset_y=-5):
            try:
                load = Image.open(file)

                render = ImageTk.PhotoImage(load, master=root)

                img = tkinter.Label(
                    root,
                    image=render)

                img.image = render
                img.place(
                    x=offset_x,
                    y=offset_y)

                return render, load

            except Exception as Message:
                messagebox.showerror(
                    "Module Not Found",
                    "".join(("This installer requires the module Pillow, ",
                             "this should have been installed automatically ",
                             "if you got this installer from PyPi, or are ",
                             "running this as a (.exe) file.\nIf you have ",
                             "grabbed this installer from GitHub then I ",
                             "advice you to install PIL with the command:",
                             "\n\npip install pillow\n\nShould any further ",
                             "problems occur then feel free to contact the ",
                             "developer with the links available at: ",
                             "https://github.com/PycraftDeveloper/Pycraft",
                             f"\n\nFull Error Message:\n{Message}")))
                quit()

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("startup Fail",
                         "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()
