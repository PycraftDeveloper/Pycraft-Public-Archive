if __name__ != "__main__":
    try:
        import tkinter
        from tkinter import messagebox
        import tkinter.ttk as tkinter_ttk
        import threading
        import sys

        import uninstall

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

    class begin_update:
        def __init__(self):
            pass

        def update_screen_one(
                self,
                root,
                PycPath,
                ChooseBETA,
                choice):
            
            root = tkinter_utils.tkinter_installer.create_display(
                self,
                root)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Preparing to update Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = "".join(("Welcome to Pycraft's update utility, here we will ",
                                 "uninstall all of Pycraft's files as well as its ",
                                 "additional data with the exception of your saved ",
                                 "data, then reinstall the latest version.\nThe ",
                                 "update utility will prompt for both accessing and ",
                                 "downloading files from the internet and for the ",
                                 "manipulation and removal of some of your files.",
                                 "\n\nIf an update is available then you can ",
                                 "continue through the update utility, if not ",
                                 "then you can return back to the 'Modify Your ",
                                 "Install' screen.\n\n"))

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
                text='Continue',
                command=lambda: begin_update.update_screen_two(
                    self,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=760, y=500)

            tkinter_ttk.Button(
                root,
                text='home',
                command=lambda: installer_utils.core_installer_functionality.home(
                    self,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=680, y=500)

        def update_screen_two(self, root, PycPath, ChooseBETA, choice):
            root = tkinter_utils.tkinter_installer.create_display(
                self,
                root)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Checking for updates",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            ContinueButtonState = tkinter.DISABLED
            BackButtonState = tkinter.DISABLED

            i = 0
            def update_options(ContinueButtonState, BackButtonState):
                global UpdateUtility
                UpdateUtility = True

                ContinueButton = tkinter_ttk.Button(
                    root,
                    text='Continue',
                    command=lambda: uninstall.begin_uninstall.remove_but_keep_save(
                        self,
                        root,
                        PycPath,
                        ChooseBETA,
                        choice))
                ContinueButton.place(x=760, y=500)
                ContinueButton['state'] = ContinueButtonState

                BackButton = tkinter_ttk.Button(
                    root,
                    text='Back',
                    command=lambda: begin_update.update_screen_one(
                        self,
                        root,
                        PycPath,
                        ChooseBETA,
                        choice))
                BackButton.place(x=680, y=500)
                BackButton['state'] = BackButtonState

            update_options(
                ContinueButtonState,
                BackButtonState)

            ans = messagebox.askquestion(
                "Permissions manager",
                "".join(("Can we have permission to download files from the ",
                    "internet and also modify files on this PC during the ",
                    "update process?")))

            retry = True

            while retry:
                if ans == "yes":
                    retry = False
                    break

                else:
                    ans2 = messagebox.askquestion(
                        "Caution",
                        "".join(("We did not receive permission to download files ",
                                 "from the internet and modify files on this PC, as ",
                                 "a result we cannot install Pycraft, would you ",
                                 "like to amend this decision (yes) or quit the ",
                                 "installer (no)?")))

                    if ans2 == "no":
                        sys.exit()

                    else:
                        retry = True
                        ans = messagebox.askquestion(
                            "Permissions manager",
                            "".join(("Can we have permission to download files from the ",
                                "internet and also modify files on this PC at any time ",
                                "using this Installer?")))

            OUTPUTtext = "Querying versions"

            text_utils.installer_text.create_text(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nFound current install as {version}"

            text_utils.installer_text.create_text(
                root,
                OUTPUTtext)

            OUTPUTtext += "".join(("\nChecking for updates online. ",
                                   "(This might take a bit of time to complete)"))

            text_utils.installer_text.create_text(
                root,
                OUTPUTtext)

            global outdated
            outdated = False

            threading.Thread(
                target=installer_utils.core_installer_functionality.outdated_detector,
                args=(self,)).start()

            def render_progress_bar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')
                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i

                root.update()

            while "outdated_detector" in str(threading.enumerate()):
                i += 1
                root.after(
                    50,
                    render_progress_bar(i))

            if outdated is False:
                OUTPUTtext += "\nYou already have the latest version of Pycraft"

                text_utils.installer_text.create_text(
                    root,
                    OUTPUTtext)

                ContinueButtonState = tkinter.DISABLED
                BackButtonState = tkinter.NORMAL

                update_options(
                    ContinueButtonState,
                    BackButtonState)

            else:
                OUTPUTtext += "".join(("\nThere are updates available on this PC, ",
                                       "press 'continue' to start the update"))

                text_utils.installer_text.create_text(
                    root,
                    OUTPUTtext)

                ContinueButtonState = tkinter.NORMAL
                BackButtonState = tkinter.NORMAL

                update_options(
                    ContinueButtonState,
                    BackButtonState)

        def finished_update(self, root):
            root = tkinter_utils.tkinter_installer.create_display(
                self,
                root)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Finished Updating Pycraft",
                background='white',
                font=(None, 20)).place(x=200, y=40)

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                "".join(("Pycraft has successfully updated to the latest version. ",
                         "Running Pycraft now will automatically run the latest ",
                         "version.\n\nThis is a new feature so might cause some ",
                         "saved data to be lost whilst the project features ",
                         "changes to how it stores saved data.\nWe hope you ",
                         "enjoy using the latest update, feel free to leave ",
                         "feedback and view the changes on GitHub!")))

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            tkinter_ttk.Button(
                root,
                text='Finish',
                command=sys.exit).place(x=760, y=500)

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
