if __name__ != "__main__":
    try:
        import datetime
        import os
        
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
        
    class create_log_message(Registry):
        def update_log_information(text):
            
            if Registry.logging_dictionary["information"]:
                text = f"Information: {str(text)}"
                text += f" @ {datetime.datetime.now()}"
                if Registry.output_log:
                    print(text)

                log_file.update_log(text)
                
        def update_log_warning(text):
            if Registry.logging_dictionary["warnings"]:
                text = f"Warning: {str(text)}"
                text += f" @ {datetime.datetime.now()}"
                if Registry.output_log:
                    print(text)

                log_file.update_log(text)

        def update_log_error(error_text):
            if Registry.logging_dictionary["errors"]:
                text = "### ### ### ###\n\n"
                text += f"Error: {str(error_text)}"
                text += f" @ {datetime.datetime.now()}\n"
                text += "\n### ### ### ###\n"
                if Registry.output_log:
                    print(text)

                log_file.update_log(text)

    class log_file(Registry):
        def __init__(self):
            pass

        def clear_log():
            log_path = Registry.base_folder / "data files" / "log.txt"
            with open(
                    log_path,
                    "w"):

                pass

        def update_log(text):
            """This subroutine updates the log file by appending new information to the end.
            This is usually called every time a log is made.
            
            - Args:
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                - text (str): This string contains the formatted log which will be
                    added to the log.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            log_path = Registry.base_folder / "data files" / "log.txt"
            size = (os.path.getsize(log_path)/1000)/1000 #MB

            if size < 1:
                with open(
                        log_path,
                        "a") as file:

                    file.write(text)

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
