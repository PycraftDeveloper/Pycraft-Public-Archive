if __name__ != "__main__":
    try:
        import threading
        import time
        import json
        import site
        import os
        import tkinter
        import tkinter.ttk as tkinter_ttk
        from tkinter import filedialog
        from tkinter import messagebox
        import platform

        if platform.system() == "Windows":
            from win32com.shell import shell, shellcon
            import win32com.client

        import update

        import tkinter_utils
        import installer_utils
        import text_utils
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

    class begin_install:
        def __init__(self):
            pass

        def install_screen_one(self, root, PycPath, ChooseBETA, choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Important Information",
                background="white",
                font=(None, 20)).place(x=200, y=35)

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                "".join(("Please read the below information, once you have ",
                         "familiarised yourself with the information, please ",
                         "tick the box to say that you have and then press ",
                         "continue to start the installation. Use the scroll ",
                         "wheel to scroll the text.\n\nYou can find Pycraft's ",
                         "GitHub repository here for more information: ",
                         "https://github.com/PycraftDeveloper/Pycraft\n\n",
                         "The program will be updated frequently and I shall ",
                         "do my best to keep this up to date too. I also want ",
                         "to add that you are welcome to view and change the ",
                         "program and share it with your friends. If you find ",
                         "any bugs or errors, please feel free to comment in ",
                         "the comments section any feedback so we can improve ",
                         "our program, it will all be much appreciated and give ",
                         "as much detail as you wish to give out. \n\n\nLicence\nMIT ",
                         "License\n\nCopyright (c) 2021 Thomas Jebbo\n\nPermission ",
                         "is hereby granted, free of charge, to any person obtaining ",
                         "a copy of this software and associated documentation files ",
                         "(the \"Software\"), to deal in the Software without ",
                         "restriction, including without limitation the rights to ",
                         "use, copy, modify, merge, publish, distribute, sublicense, ",
                         "and/or sell copies of the Software, and to permit persons to ",
                         "whom the Software is furnished to do so, subject to the ",
                         "following conditions:\n\nThe above copyright notice and ",
                         "this permission notice shall be included in all copies or ",
                         "substantial portions of the Software.\n\nTHE SOFTWARE IS ",
                         "PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS ",
                         "OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF ",
                         "MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND ",
                         "NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR ",
                         "COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR ",
                         "OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR ",
                         "OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE ",
                         "SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")))

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            var1 = tkinter.IntVar()

            def button_check(self, root, PycPath, ChooseBETA, choice, var1):
                data = var1.get()
                if data is None or data == 0:
                    continueButton = tkinter_ttk.Button(
                        root,
                        text="Continue")

                    continueButton.place(x=760, y=500)
                    continueButton["state"] = tkinter.DISABLED

                else:
                    continueButton = tkinter_ttk.Button(
                        root,
                        text="Continue",
                        command=lambda: begin_install.install_screen_two(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            choice))

                    continueButton.place(x=760, y=500)
                    continueButton["state"] = tkinter.NORMAL
                    root.update_idletasks()

            button_check(self, root,
                        PycPath, ChooseBETA, choice, var1)

            tkinter_ttk.Radiobutton(
                root, text="I have not read the above text",
                variable=var1,
                value=0,
                command=lambda: button_check(
                    self,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice,
                    var1)).place(x=200, y=475)

            tkinter_ttk.Radiobutton(
                root,
                text="I have read the above text",
                variable=var1,
                value=1,
                command=lambda: button_check(
                    self,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice,
                    var1)).place(x=200, y=500)

            tkinter_ttk.Button(
                root,
                text="home",
                command=lambda: installer_utils.core_installer_functionality.home(
                    self,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=680, y=500)

        def install_screen_two(self, root, PycPath, ChooseBETA, choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Set Install Location",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            OUTPUTtext = "".join(("Now we need to ask one final thing before ",
                                  "we start the install, where would you like ",
                                  "to store Pycraft?"))

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                OUTPUTtext)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            global Dir
            Dir = Registry.base_folder

            def get_dir():
                global Dir
                Dir = filedialog.askdirectory()
                if len(Dir) >= 80:
                    Dir2 = Dir[:80]+"..."
                else:
                    Dir2 = Dir

                global CurrentLocat

                CurrentLocat.destroy()
                CurrentLocat = tkinter.Label(
                    root,
                    text=("  "+Dir2+"  "),
                    background="white",
                    relief=tkinter.RIDGE)

                CurrentLocat.place(x=313, y=152.5)

                root.update_idletasks()

            tkinter_ttk.Button(
                root,
                text="Choose file location",
                command=get_dir).place(x=200, y=150)

            global CurrentLocat, UpdateUtility
            UpdateUtility = True

            ComputePath = Registry.base_folder[len(
                Registry.base_folder)-90:]

            CurrentLocat = tkinter.Label(
                root,
                text=("  "+ComputePath+"  "),
                background="white",
                relief=tkinter.RIDGE)

            CurrentLocat.place(x=313, y=152.5)

            tkinter_ttk.Button(
                root,
                text="Continue",
                command=lambda: begin_install.install_screen_three(
                    self,
                    root,
                    choice,
                    Dir)).place(x=760, y=500)

            tkinter_ttk.Button(
                root,
                text="Back",
                command=lambda: begin_install.install_screen_one(
                    self,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=680, y=500)

            root.update_idletasks()

        def install_screen_three(self, root, choice, Dir):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Downloading and installing Pycraft",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            ans = messagebox.askquestion(
                "Permissions manager",
                "".join(("Can we have permission to download files from the internet ",
                         "and also modify files on this PC at any time using this Installer?")))

            retry = True
            i = 0
            while retry:
                if ans == "yes":
                    retry = False

                    global current_location

                    current_location = None
                    infoVers = None

                    if choice == "Latest":
                        OUTPUTtext = "Found latest version as: Pycraft v0.9.5"

                        text_utils.installer_text.create_text(
                            root,
                            OUTPUTtext)

                        infoVers = "Pycraft v0.9.5"
                    else:
                        OUTPUTtext = f"Found requested version as: {choice}"

                        text_utils.installer_text.create_text(
                            root,
                            OUTPUTtext)

                        infoVers = choice

                    OUTPUTtext += "".join((f"\nDownloading and installing {infoVers} ",
                                           "and the latest versions of it's dependencies ",
                                           "(This will take a moment)"))

                    text_utils.installer_text.create_text(
                        root,
                        OUTPUTtext)

                    threading.Thread(
                        target=installer_utils.file_manipulation.download_and_install,
                        args=(self, choice,)).start()

                    start = time.perf_counter()

                    def render_progress_bar(i):
                        CompletionProgressbar = tkinter_ttk.Progressbar(
                            root,
                            orient=tkinter.HORIZONTAL,
                            length=100,
                            mode="indeterminate")

                        CompletionProgressbar.place(x=200, y=500)

                        CompletionProgressbar["value"] += i
                        root.update()

                    while threading.active_count() == 2:
                        i += 1
                        root.after(
                            50,
                            render_progress_bar(i))

                    installtime = time.perf_counter()-start

                    OUTPUTtext += f" - done in {round(installtime, 4)} seconds"
                    text_utils.installer_text.create_text(
                        root,
                        OUTPUTtext)

                    OUTPUTtext += "\nSuccessfully installed Pycraft"

                    OUTPUTtext += "\nMoving Pycraft to selected install location"
                    text_utils.installer_text.create_text(
                        root,
                        OUTPUTtext)

                    current_location = site.getusersitepackages()

                    threading.Thread(
                        target=installer_utils.file_manipulation.move_files,
                        args=(self, Dir,)).start()

                    while threading.active_count() == 2:
                        i += 1
                        root.after(
                            50,
                            render_progress_bar(i))

                    OUTPUTtext += " - done"
                    text_utils.installer_text.create_text(
                        root,
                        OUTPUTtext)

                    OUTPUTtext += "\nSuccessfully Installed Pycraft"
                    text_utils.installer_text.create_text(
                        root,
                        OUTPUTtext)

                    try:
                        global UpdateUtility
                        if UpdateUtility:
                            tkinter_ttk.Button(
                                root,
                                text="Continue",
                                command=lambda: begin_install.install_screen_four(
                                    self,
                                    root,
                                    choice,
                                    Dir)).place(x=760, y=500)

                    except:
                        update.begin_update.finished_update(
                            self,
                            root)

                    root.update_idletasks()
                else:
                    ans2 = messagebox.askquestion(
                        "Caution",
                        "".join(("We did not receive permission to download files from the ",
                                 "internet and modify files on this PC, as a result we ",
                                 "cannot install Pycraft, would you like to amend this ",
                                 "decision (yes) or close the installer (no)?")))

                    if ans2 == "no":
                        quit()

                    else:
                        retry = True
                        ans = messagebox.askquestion(
                            "Permissions manager",
                            "".join(("Can we have permission to download files from ",
                                     "the internet and also modify files on this PC ",
                                     "at any time using this Installer?")))

        def install_screen_four(self, root, choice, Dir):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Successfully Installed Pycraft",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                "".join((f"Successfully installed {choice} we hope that you enjoy using ",
                         "this project. This installer can be opened from Pycraft by ",
                         "clicking on the 'Installer' option on the main menu. The ",
                         "installer will appear differently when you open it from ",
                         "Pycraft, from there you will be able to change these settings ",
                         "again under the 'Modify' section, but you also have the option ",
                         "to 'Repair', 'Uninstall' and 'Update' Pycraft. For now though ",
                         "we have finished the install but we have some final options ",
                         "which will be applied when the GUI closes:\nDo you want to add ",
                         "Pycraft to the desktop?\nAdditionally do you want to add Pycraft ",
                         "to the start (recommended)?\nYou also have the option to view ",
                         "the release notes for this install as well.\nThanks for ",
                         "installing Pycraft!")))

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            CS = tkinter.BooleanVar(value=True)
            CSS = tkinter.BooleanVar(value=False)
            RelNot = tkinter.BooleanVar(value=True)

            global CreateDSKShortcut, CreateSTRTShortcut, ReleaseNotes

            CreateDSKShortcut = True
            CreateSTRTShortcut = False
            ReleaseNotes = True

            Config = {"PATH": Dir}
            if Registry.platform == "Linux":
                with open(
                    os.path.join(
                        Registry.base_folder,
                        ("data files//installer_config.json")), 'w') as openFile:

                    json.dump(Config, openFile)

                with open(
                        (Dir+"//data files//installer_config.json"), 'w') as openFile:

                    json.dump(Config, openFile)

            else:
                with open(
                    os.path.join(
                        Registry.base_folder,
                        ("data files\\installer_config.json")), 'w') as openFile:

                    json.dump(Config, openFile)

                with open(
                        (Dir+"\\data files\\installer_config.json"), 'w') as openFile:

                    json.dump(Config, openFile)

            def desktop_is_checked():
                global CreateDSKShortcut
                CreateDSKShortcut = CS.get()

            def start_is_checked():
                global CreateSTRTShortcut
                CreateSTRTShortcut = CSS.get()

            def toggle_release_notes():
                global ReleaseNotes
                ReleaseNotes = RelNot.get()

            def on_exit():
                try:
                    if CreateDSKShortcut:
                        desktop = os.path.join(
                            os.path.join(
                                os.environ["USERPROFILE"]),
                            "Desktop")

                        shell = client.Dispatch(
                            "WScript.Shell")

                        shortcut = shell.CreateShortCut(
                            os.path.join(
                                desktop,
                                'Pycraft.lnk'))

                        FolderDirectory = "/pycraft/resources/folder resources/FolderIcon.ico"
                        shortcut.Targetpath = Dir+"/Pycraft/main.py"
                        shortcut.IconLocation = Dir+FolderDirectory
                        shortcut.save()

                    if CreateSTRTShortcut:
                        try:
                            start = shell.SHGetSpecialFolderPath(
                                0,
                                shellcon.CSIDL_COMMON_STARTMENU)

                            shell = client.Dispatch(
                                "WScript.Shell")

                            shortcut = shell.CreateShortCut(
                                os.path.join(
                                    start,
                                    "Programs\\Pycraft.lnk"))

                            FolderDirectory = "/pycraft/resources/folder resources/FolderIcon.ico"

                            shortcut.Targetpath = Dir+"/pycraft/main.py"
                            shortcut.IconLocation = Dir+FolderDirectory
                            shortcut.save()

                        except Exception as Message:
                            print(Message)
                            messagebox.showwarning(
                                "Permission Denied",
                                "".join(("You need to run this program as an administrator ",
                                         "to be able to use this function")))

                    if ReleaseNotes:
                        import webbrowser
                        webbrowser.open(
                            "https://github.com/PycraftDeveloper/Pycraft")

                except Exception as Message:
                    messagebox.showerror(
                        "An error occurred",
                        "".join(("Pycraft has successfully installed but some of your final ",
                                 "configurations have not been made, this will change in later ",
                                 "versions of Pycraft but a quick fix is trying to restart the ",
                                 "installer, files downloaded already will be automatically ",
                                 "skipped in the download and install. Also this is an early ",
                                 "version of the installer, small issues like this will be ",
                                 "fixed in later versions of Pycraft that are build around ",
                                 f"the installer.\n\nFull error message: {Message}")))

                quit()

            tkinter_ttk.Checkbutton(
                root,
                text="Create desktop shortcut on exit",
                variable=CS,
                onvalue=True,
                offvalue=False,
                command=desktop_is_checked).place(x=200, y=250)

            tkinter_ttk.Checkbutton(
                root,
                text="Create shortcut to start on exit",
                variable=CSS,
                onvalue=True,
                offvalue=False,
                command=start_is_checked).place(x=200, y=275)

            tkinter_ttk.Checkbutton(
                root,
                text="View more details about Pycraft online (on GitHub)",
                variable=RelNot,
                onvalue=True,
                offvalue=False,
                command=toggle_release_notes).place(x=200, y=300)

            tkinter_ttk.Button(
                root,
                text="Finish",
                command=on_exit).place(x=760, y=500)

            root.update_idletasks()

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
