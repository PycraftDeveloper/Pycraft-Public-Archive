if __name__ != "__main__":
    try:
        import tkinter
        import tkinter.ttk as tkinter_ttk

        import update
        import uninstall
        import install
        
        import tkinter_utils
        import installer_utils
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

    class installer_home:
        def start(self, root, PycPath, ChooseBETA, Choice):
            root = tkinter_utils.tkinter_installer.create_display(
                root,
                Registry.platform,
                Registry.base_folder)
            
            tkinter.Label(
                root,
                text="Pycraft's installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            if Registry.platform == "Windows":
                if PycPath is not None:
                    ButtonPos = (760, 500)

                    tkinter.Label(
                        root,
                        text="Modify Your install",
                        background="white",
                        font=(None, 20)).place(x=200, y=35)

                    EnterText = "".join(("Welcome back to Pycraft's Setup Wizard, we ",
                                         "have detected you already have an install of ",
                                         "Pycraft on your system, this gives you 3 ",
                                         "available options.\n\nWould you like to update, ",
                                         "modify or uninstall your version of Pycraft?",
                                         "\n\nThis will modify the installation of ",
                                         f"Pycraft at: {PycPath}"))

                    tkinter_ttk.Button(
                        root,
                        text="Update",
                        command=lambda: update.Beginupdate.updateScreen_0(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)).place(x=680, y=500)

                    RepairButton = tkinter_ttk.Button(
                        root,
                        text="Repair")
                    RepairButton["state"] = tkinter.DISABLED
                    RepairButton.place(x=600, y=500)

                    tkinter_ttk.Button(
                        root,
                        text="Uninstall",
                        command=lambda: uninstall.Beginuninstall.uninstallScreen_0(
                            self,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)).place(x=520, y=500)

                    IfCompat = tkinter.NORMAL
                else:
                    try:
                        EnterText = "".join(("Welcome to Pycraft's Setup Wizard, ",
                                             "here we will guide you through your install ",
                                             "and setup of the latest stable version of ",
                                             "Pycraft, if you wish to install the BETA ",
                                             "versions of the game, please tick the box ",
                                             "below and then once you are satisfied with ",
                                             "your choice, please press the continue ",
                                             "button, you can press the back button to ",
                                             "navigate to the previous menu or choose ",
                                             "to exit Pycraft's Setup Wizard by closing ",
                                             "the GUI.\n\nThere are a few steps to this ",
                                             "install but this shouldn't take long."))

                        IfCompat = tkinter.NORMAL

                        ButtonPos = (680, 500)

                        BETAchoice = tkinter.BooleanVar(
                            value=ChooseBETA)

                        versions = [
                            "Latest",
                            "Latest",
                            "Pycraft-v0.9.1",
                            "Pycraft-v0.9.2",
                            "Pycraft-v0.9.3",
                            "Pycraft-v0.9.4",
                            "Pycraft-v0.9.5 (latest)"]

                        VersionChoice = tkinter.StringVar()
                        VersionChoice.set(versions[0])

                        DropDown = tkinter_ttk.OptionMenu(
                            root,
                            VersionChoice,
                            *versions)

                        def get_version(BETAchoice):
                            if BETAchoice.get():
                                DropDown["state"] = tkinter.NORMAL

                            else:
                                DropDown["state"] = tkinter.DISABLED

                            DropDown.place(x=450, y=500)

                        get_version(BETAchoice)

                        tkinter_ttk.Checkbutton(
                            root,
                            text="I want to install a BETA version of Pycraft",
                            variable=BETAchoice,
                            onvalue=True,
                            offvalue=False,
                            command=lambda: get_version(BETAchoice)).place(x=200, y=500)

                        ContinueButton = tkinter_ttk.Button(
                            root,
                            text="Continue",
                            command=lambda: install.Begininstall.installScreen_0(
                                self,
                                root,
                                PycPath,
                                BETAchoice.get(),
                                VersionChoice.get()))

                        ContinueButton.place(x=760, y=500)
                        ContinueButton["state"] = IfCompat

                    except:
                        IfCompat = tkinter.DISABLED

                        EnterText = "".join(("Welcome to Pycraft's Setup Wizard, ",
                                             "here we will guide you through your ",
                                             "install and setup of the latest stable ",
                                             "version of Pycraft, if you wish to ",
                                             "install the BETA versions of the game, ",
                                             "please tick the box below and then once ",
                                             "you are satisfied with your choice, ",
                                             "please press the continue button, you ",
                                             "can press the back button to navigate ",
                                             "to the previous menu or choose to exit ",
                                             "Pycraft's Setup Wizard by closing the GUI.",
                                             "\n\nThere are a few steps to this install ",
                                             "but this shouldn't take long.\n\nIn order ",
                                             "to install Pycraft you will need to have a ",
                                             "suitable version of Python installed on ",
                                             "your system, ideally this needs to be 3.7 ",
                                             "or greater -with version checking coming ",
                                             "in a later version-. If you want to ",
                                             "install Pycraft stand-alone then on the ",
                                             "releases page of the project (here: ",
                                             "https://github.com/PycraftDeveloper/Pycraft/releases) ",
                                             "please download the (.exe) version."))

            else:
                IfCompat = tkinter.DISABLED

                ButtonPos = (680, 500)

                EnterText = ("Welcome to Pycraft's Setup Wizard, here we will ",
                             "guide you through your install and setup of the ",
                             "latest stable version of Pycraft, if you wish to ",
                             "install the BETA versions of the game, please tick ",
                             "the box below and then once you are satisfied with ",
                             "your choice, please press the continue button, you ",
                             "can press the back button to navigate to the previous ",
                             "menu or choose to exit Pycraft's Setup Wizard by ",
                             "closing the GUI.\n\nThere are a few steps to this ",
                             "install but this shouldn't take long.\n\nCurrently ",
                             "this installer is Windows only, but more OS's will ",
                             "be supported in later editions")

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
                text="Quit",
                command=lambda: installer_utils.core_installer_functionality.close(root)).place(
                        x=ButtonPos[0],
                        y=ButtonPos[1])

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
