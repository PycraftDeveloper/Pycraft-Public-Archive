if __name__ != "__main__":
    try:
        import os
        import tkinter
        from tkinter import messagebox
        import pathlib
        import threading

        from registry_utils import Registry
        
        import image_utils
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
            
    class splash_screen(Registry):
        def __init__(self):
            pass
        
        def create_splash():
            directory = os.path.dirname(__file__)
            pycraft_directory = str(directory).split("\\")
            directory = ""

            for folder in range(len(pycraft_directory)-1):
                directory += f"{pycraft_directory[folder]}\\"

            base_folder = pathlib.Path(directory).parent
            
            root = tkinter.Tk()
            
            root.eval('tk::PlaceWindow . center')
            
            root.title("Loading Pycraft")
            
            root.resizable(
                False,
                False)
            
            banner_path = base_folder / "resources" / "general resources" / "pycraft_logo.png"

            _, _ = image_utils.tkinter_installer.open_img(
                root, 
                banner_path)

            #Make the window borderless
            root.overrideredirect(True)

            root.mainloop()
    
    class tkinter_info(Registry):
        def __init__(self):
            pass

        def get_permissions(permission_message):
            root = tkinter.Tk()
            root.withdraw()

            answer = messagebox.askquestion(
                "Check Permission",
                permission_message)
            
            if answer == "yes":
                return True

            else:
                return False
            
        def update_content():
            VariableInformation = ""
            for key in Registry.__dict__:
                VariableInformation += f"{key} = {str(Registry.__dict__[key])}\n"
            
            return VariableInformation
        
        def refresh_window(DataWindow, text):
            VariableInformation = tkinter_info.update_content()
            
            text["state"] = tkinter.NORMAL
            text.replace("1.0", tkinter.END, VariableInformation)
            text["state"] = tkinter.DISABLED

            text.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1)
            
            DataWindow.after(1000, lambda: tkinter_info.refresh_window(DataWindow, text))
            
        def tkinter_window():
            DataWindow = tkinter.Tk()
            DataWindow.title("Registry Information")
            DataWindow.configure(width=500, height=300)
            DataWindow.configure(bg="darkgrey")
            
            text = tkinter.Text(
                DataWindow,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT)
            
            text["bg"] = "#%02x%02x%02x" % (Registry.background_color[0],
                                                Registry.background_color[1],
                                                Registry.background_color[2])

            text["fg"] = "#%02x%02x%02x" % (Registry.font_color[0],
                                                Registry.font_color[1],
                                                Registry.font_color[2])
            
            VariableInformation = tkinter_info.update_content()

            VariableInformation = sorted(VariableInformation)
            
            for i in range(len(VariableInformation)):
                text.insert(tkinter.INSERT, VariableInformation[i])
            
            tkinter_info.refresh_window(DataWindow, text)
            
            DataWindow.after(1000, lambda: tkinter_info.refresh_window(DataWindow, text))

            DataWindow.mainloop()
            DataWindow.quit()
            
        def create_tkinter_window():
            threading.Thread(target=tkinter_info.tkinter_window).start()
                
    class tkinter_installer(Registry):
        def __init__():
            pass

        def create_display(root, platform, base_folder):
            try:
                geometry = root.winfo_geometry().split("+")
                Xpos = geometry[1]
                Ypos = geometry[2]
                root.destroy()
                
            except:
                Xpos, Ypos = 0, 0

            root = tkinter.Tk()
            #root = tkinter.Toplevel()

            root.title("Pycraft Setup Wizard")

            root.resizable(
                False,
                False)

            root.configure(bg="white")
            root.geometry(f"850x537+{int(Xpos)}+{int(Ypos)}")

            banner_path = base_folder / "resources" / "installer resource" / "Banner.png"

            render, load = image_utils.tkinter_installer.open_img(
                root, 
                banner_path)
            
            return root

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
