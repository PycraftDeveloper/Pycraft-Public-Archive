if __name__ != "__main__":
    try:
        import os
        import tkinter
        from tkinter import messagebox
        import tkinter.ttk as tkinter_ttk
        import threading
        import json
        import sys

        import install

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
            
    class begin_uninstall:
        def __init__(self):
            pass

        def uninstall_screen_one(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Modify Your install - Uninstall",
                background='white',
                font=(None, 20)).place(x=200, y=35)

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            UninstallerInstructions = "".join(("You have arrived at Pycraft's uninstall ",
                                               "utility, here you can remove Pycraft from ",
                                               "your system and/or remove the project's ",
                                               "additional files, these will be sent to ",
                                               "your recycle bin so you have the option to ",
                                               "change your mind.\n\nIf you want to feel ",
                                               "free to feedback any bugs, ideas or ",
                                               "suggestions to the developers who's contact ",
                                               "you can find here: ",
                                               "https://github.com/PycraftDeveloper/Pycraft"))

            text.insert(tkinter.INSERT, UninstallerInstructions)
            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            def get_confirmation():
                global UpdateUtility
                UpdateUtility = False
                if messagebox.askokcancel(
                    "Are you sure with your decision",
                    "".join(("Please now take the time to make sure you have ",
                             "chosen correctly as some options will clear all ",
                             "settings and progress made! \n\nPress OK to ",
                             "continue the uninstall process"))):

                    ans = messagebox.askquestion(
                        "Permissions manager",
                        "Can we have permission to remove and change some files on your PC?")

                    while ans == "no":
                        ans2 = messagebox.askquestion(
                            "Caution",
                            "".join(("We did not receive permission to remove and modify ",
                                     "files on this PC, as a result we cannot uninstall ",
                                     "Pycraft, would you like to amend this decision (yes) ",
                                     "or close the installer (no)?")))

                        if ans2 == "no":
                            quit()
                        else:
                            ans = messagebox.askquestion(
                                "Permissions manager",
                                "Can we have permission to remove and change files on your PC?")

                    if Uninstall_Option.get() == 1:
                        begin_uninstall.remove_but_keep_save(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

                    elif Uninstall_Option.get() == 2:
                        begin_uninstall.remove_but_leave(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

                    else:
                        begin_uninstall.remove_all(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

            tkinter_ttk.Button(
                root,
                text='home',
                command=lambda: installer_utils.core_installer_functionality.home(
                    self,
                    root,
                    PycPath,
                    ChooseBETA, Choice)).place(x=680, y=500)

            tkinter_ttk.Button(
                root,
                text='Continue',
                command=get_confirmation).place(x=760, y=500)

            Uninstall_Option = tkinter.IntVar()

            tkinter_ttk.Radiobutton(
                root,
                text="Remove Pycraft and additional files but keep save data",
                variable=Uninstall_Option,
                value=1).place(x=200, y=200)

            tkinter_ttk.Radiobutton(
                root,
                text="Remove Pycraft but leave additional files",
                variable=Uninstall_Option,
                value=2).place(x=200, y=225)

            tkinter_ttk.Radiobutton(
                root,
                text="Remove everything",
                variable=Uninstall_Option,
                value=3).place(x=200, y=250)

            Uninstall_Option.set(1)

            root.mainloop()


        def remove_all(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(root, Registry.platform, Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Uninstalling Pycraft and all additional files",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version} and additional files"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            FileArray = installer_utils.file_manipulation.search_files(
                self,
                PycPath)

            import site
            if Registry.platform == "Linux":
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"//Python310//site-packages"))

            else:
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"\\Python310\\site-packages"))

            FileArray = FileArray+AdditionalFileArray
            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(self,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            i = 0
            def render_progress_bar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in threading.enumerate():
                i += 1
                root.after(
                    50,
                    render_progress_bar(i))

            OUTPUTtext += f"\nSuccessfully removed {version} and additional files"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            try:
                os.rmdir(PycPath)
                
            except:
                pass

            OUTPUTtext += "\nDone"
            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            begin_uninstall.finish_uninstall(
                self,
                root)


        def remove_but_keep_save(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Uninstalling Pycraft and all additional files but keeping save data",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"
            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version} and additional files"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            FileArray = installer_utils.file_manipulation.search_files(
                self,
                PycPath)

            import site
            if Registry.platform == "Linux":
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"//Python310//site-packages"))
            
            else:
                AdditionalFileArray = installer_utils.file_manipulation.search_files(
                    self,
                    (site.getuserbase()+"\\Python310\\site-packages"))

            FileArray = FileArray+AdditionalFileArray
            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(self,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            i = 0
            def render_progress_bar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in threading.enumerate():
                i += 1
                root.after(
                    50,
                    render_progress_bar(i))

            OUTPUTtext += f"\nSuccessfully removed {version} and additional files"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nDone"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            try:
                global UpdateUtility
                if not UpdateUtility:
                    begin_uninstall.finish_uninstall(
                        self,
                        root)

            except:
                if Registry.platform == "Linux":
                    with open(
                        os.path.join(
                            Registry.base_folder,
                            ("data files//installer_config.json")), 'r') as openFile:

                        SavedData = json.load(openFile)

                else:
                    with open(
                        os.path.join(
                            Registry.base_folder,
                            ("data files\\installer_config.json")), 'r') as openFile:

                        SavedData = json.load(openFile)
                    
                Dir = SavedData["PATH"]

                install.Begininstall.installScreen_2(
                    self,
                    root,
                    Choice,
                    Dir)


        def remove_but_leave(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Uninstalling Pycraft but keeping additional files",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version}"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            FileArray = installer_utils.file_manipulation.search_files(
                self,
                PycPath)

            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            threading.Thread(
                target=installer_utils.file_manipulation.remove_files,
                args=(self,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            i = 0
            def render_progress_bar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in threading.enumerate():
                i += 1
                root.after(
                    50,
                    render_progress_bar(i))

            OUTPUTtext += f"\nSuccessfully removed {version}"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            try:
                os.rmdir(PycPath)
                
            except:
                pass

            OUTPUTtext += "\nDone"

            text_utils.installerText.create_text(
                root,
                OUTPUTtext)

            begin_uninstall.finish_uninstall(
                self,
                root)


        def finish_uninstall(self, root):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)

            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Successfully uninstalled Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = "".join(("Pycraft has been removed from your computer, ",
                                 "you can re-install the project at any time ",
                                 "from GitHub, SourceForge or PyPi. If you ",
                                 "have experienced any bugs or have any ",
                                 "suggestions then feel free to share them ",
                                 "on the project page!"))

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                EnterText)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=40)

            tkinter_ttk.Button(
                root,
                text='Quit',
                command=sys.exit).place(x=760, y=500)

            root.mainloop()

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
