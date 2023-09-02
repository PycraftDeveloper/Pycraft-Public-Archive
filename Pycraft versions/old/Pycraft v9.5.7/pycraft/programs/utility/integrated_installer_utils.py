if __name__ != "__main__":
    try:
        from urllib import request
        import subprocess
        import sys
        import traceback
        
        from registry_utils import Registry

        import error_utils
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
            
    class integrated_installer(Registry):
        def check_versions():
            try:
                if (Registry.connection_permission and
                        Registry.connection_status):

                    List = subprocess.check_output(
                        [sys.executable, "-m", "pip", "list", "--outdated"],
                        False)

                    for i in range(len(List)):
                        if List[i:i+14] == b"Python-Pycraft":
                            Registry.outdated = True
                            Registry.total_number_of_updates = 1

                    Registry.get_outdated = [True, False]
                    
            except Exception as Message:
                error_message = "".join(("IntegratedInstaller > integrated_installer ",
                                             f"> check_versions: {str(Message)}"))

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)


    class check_connection(Registry):
        """
        This class is used to check if your PC has a working network
        connection so that updates can be checked for successfully.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        def __init__(self):
            pass

        def test():
            """
            This subroutine attempts to ping google's servers.
            If this is successfully it means there is currently an
            internet connection to your PC. This is not run in a thread,
            so therefore there is a 1 second timeout. This means that if
            there isn't an internet connection available it doesn't slow down
            Pycraft's startup too much.
            
            - Args:
                - None
                    
            - Keyword Args:
                - None

            - Output:
                - (bool): This subroutine will return True if an internet
                    connection can be established. If an internet connection could
                    not be established, nothing is returned.
            """

            try:
                request.urlopen(
                    "https://www.google.com",
                    timeout=1)

                return True
            
            except:
                return False

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
