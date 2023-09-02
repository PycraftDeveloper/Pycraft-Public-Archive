if __name__ != "__main__":
    try:
        import os
        import json
        import sys
        import site
        import shutil
        import subprocess
        from tkinter import messagebox
        
        from registry_utils import Registry

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
            
    class get_installer_data(Registry):
        def __init__(self):
            pass

        def get_data(platform, base_folder):
            installer_config_path = base_folder / "data files" / "installer_config.json"
            try:
                with open(
                        installer_config_path,
                        "r") as file:

                    SavedData = json.load(file)

            except:
                PycPath = None
                Repair = {"PATH":None}

                with open(
                        installer_config_path,
                        "w") as file:

                    json.dump(
                        Repair,
                        file)

            else:
                PycPath = SavedData["PATH"]

            return PycPath

    class core_installer_functionality(Registry):
        def __init__(self):
            pass


        def close(root):
            if messagebox.askokcancel(
                "Pycraft Setup Wizard",
                "Are you sure you want to quit?"):

                root.destroy()
                sys.exit()


        def home(self, root, PycPath, ChooseBETA, Choice):
            installer_home.installer_home.start(
                self,
                root,
                PycPath,
                ChooseBETA,
                Choice)


        def outdated_detector(InstallerImportData):
            try:
                import urllib.request as urlOpener

                urlOpener.urlopen(
                    "https://www.google.com",
                    timeout=1)

                List = subprocess.check_output(
                        [sys.executable, "-m", "pip", "list", "--outdated"],
                        False)

                global outdated

                if b"Python-Pycraft" in List:
                    outdated =  True
                    
            except Exception as Message:
                messagebox.showerror(
                    "An error has occurred",
                    "".join(("We were unable to check for updates to Pycraft, ",
                             "the most likely reason for this is a faulty ",
                             "internet connection.\n\nFull Error ",
                             f"Message:\n{Message}")))

                sys.exit()

    class file_manipulation(Registry):
        def __init__(self):
            pass

        def move_files(self, Dir):
            global current_location
            try:
                temp = str(current_location.decode("UTF-8"))[:-1]
                
            except:
                temp = site.getusersitepackages()

            try:
                if Registry.platform == "Linux":
                    shutil.copytree(
                        f"{temp}//pycraft",
                        f"{Dir}//pycraft")
                    
                else:
                    shutil.copytree(
                    f"{temp}\\pycraft",
                    f"{Dir}\\pycraft")

            except Exception as Message:
                messagebox.showerror(
                    "An error has occurred",
                    "".join(("We were unable to move Pycraft to the ",
                                "requested install location.\n\nFull Error ",
                                f"Message:\n{Message}")))

                sys.exit()


        def download_and_install(InstallerImportData, choice):
            try:
                if choice == "Latest":
                    subprocess.check_call(
                        [sys.executable,
                            "-m",
                            "pip",
                            "install",
                            "python-pycraft"],
                        False)

                else:
                    #["none", "Pycraft-v0.9.1", "Pycraft-v0.9.2", "Pycraft-v0.9.3"]
                    if choice == "Pycraft-v0.9.1":
                        subprocess.check_call(
                            [sys.executable,
                                "-m",
                                "pip",
                                "install",
                                "python-pycraft==0.9.1"],
                            False)

                    elif choice == "Pycraft-v0.9.2":
                        subprocess.check_call(
                            [sys.executable,
                                "-m",
                                "pip",
                                "install",
                                "python-pycraft==0.9.2"],
                            False)

                    elif choice == "Pycraft-v0.9.3":
                        subprocess.check_call(
                            [sys.executable,
                                "-m",
                                "pip",
                                "install",
                                "python-pycraft==0.9.3"],
                            False)

                    elif choice == "Pycraft-v0.9.4":
                        subprocess.check_call(
                            [sys.executable,
                                "-m",
                                "pip",
                                "install",
                                "python-pycraft==0.9.4"],
                            False)

                    else:
                        subprocess.check_call(
                            [sys.executable,
                                "-m",
                                "pip",
                                "install",
                                "python-pycraft"],
                            False)
                        
            except Exception as Message:
                messagebox.showerror(
                    "An error ocurred",
                    "".join(("We were unable to install the additional ",
                             "files Pycraft needs in-order to install.\n\n",
                             f"Full Error Message: {Message}")))

                sys.exit()


        def search_files(InstallerImportData, directory):
            arr = []
            print(f"Scanning {directory}")
            for dirpath, dirnames, files in os.walk(directory):
                for name in files:
                    arr.append(f"{dirpath}\{name}")
                    
            return arr


        def remove_files(InstallerImportData, FileArray, keep_save=False):
            try:
                for i in range(len(FileArray)):
                    try:
                        if keep_save:
                            if not ("Data Files" in FileArray[i] or
                                    "distutils" in FileArray[i] or
                                    "pip" in FileArray[i] or
                                    "setuptools" in FileArray[i] or
                                    "pkg_resources" in FileArray[i] or
                                    "README" in FileArray[i] or
                                    "win32" in FileArray[i] or
                                    "wheel" in FileArray[i]):

                                os.remove(FileArray[i])

                        else:
                            if not ("distutils" in FileArray[i] or
                                    "pip" in FileArray[i] or
                                    "setuptools" in FileArray[i] or
                                    "pkg_resources" in FileArray[i] or
                                    "README" in FileArray[i] or
                                    "win32" in FileArray[i] or
                                    "wheel" in FileArray[i]):

                                os.remove(FileArray[i])

                    except Exception as Message:
                        print(Message)
                        
            except Exception as Message:
                messagebox.showerror(
                    "An error ocurred",
                    "".join(("We were unable to remove some files for ",
                             f"Pycraft from your PC.\n\nFull Error Message: {Message}")))

                sys.exit()

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
