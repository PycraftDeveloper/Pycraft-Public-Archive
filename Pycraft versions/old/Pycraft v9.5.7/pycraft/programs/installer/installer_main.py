try:
    import platform
    import os

    import tkinter_utils
    import installer_utils
    import installer_home
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
        
class run_installer:
    def __init__(self):
        Registry.platform = platform.system()

        directory = os.path.dirname(__file__)
        if Registry.platform == "Linux":
            pycraft_directory = str(directory).split("//")
            directory = ""

            for folder in range(len(pycraft_directory)-2):
                directory += f"{pycraft_directory[folder]}//"

        else:
            pycraft_directory = str(directory).split("\\")
            directory = ""

            for folder in range(len(pycraft_directory)-2):
                directory += f"{pycraft_directory[folder]}\\"

        Registry.base_folder = directory
    
    def Initialize():
        self = run_installer()
        root = None

        ChooseBETA = False
        Choice = "Latest"

        root = tkinter_utils.tkinter_installer.create_display(
            root,
            Registry.platform,
            Registry.base_folder)

        PycPath = installer_utils.get_installer_data.get_data(
            Registry.platform,
            Registry.base_folder)

        installer_home.installer_home.start(
            self,
            root,
            PycPath,
            ChooseBETA,
            Choice)

        root.mainloop()

if __name__ == "__main__":
    run_installer.Initialize()
