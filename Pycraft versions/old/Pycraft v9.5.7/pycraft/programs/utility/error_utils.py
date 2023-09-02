if __name__ != "__main__":
    try:
        from registry_utils import Registry
        
        import logging_utils
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
            
    class generate_error_screen(Registry):
        def __init__(self):
            pass

        def error_screen(
                error_message,
                error_message_detailed,
                close_pygame_window=True):
            
            import tkinter as TKINTER
            import sys
            from tkinter import messagebox as msgbox

            if close_pygame_window:
                try:
                    import pygame
                    pygame.init()
                    pygame.display.quit()
                    
                except Exception as Message:
                    log_message = "ErrorUtils > generate_error_screen > error_screen" + str(Message)

                    logging_utils.create_log_message.update_log_warning(
                        log_message)

            try:
                BaseWindow = TKINTER.Tk()
                BaseWindow.withdraw()
                if Registry.detailed_error_messages:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                            f"More Details:\n{error_message_detailed}"))
                    
                    logging_utils.create_log_message.update_log_error(
                        message)

                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                else:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                       f"More Details:\n{error_message}"))

                    logging_utils.create_log_message.update_log_error(
                        message)
                    
                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                sys.exit()
                
            except Exception as Message:
                try:
                    log_message = "ErrorUtils > generate_error_screen > error_screen: " + str(Message)
                    
                    logging_utils.create_log_message.update_log_warning(
                        log_message)
                    
                except Exception as Message:
                    print(Message)
                
                try:
                    BaseWindow = TKINTER.Tk()
                    BaseWindow.withdraw()
                    msgbox.showerror("Pycraft closed because an error occurred",
                                     "".join(("Pycraft closed because an error occurred\n\n",
                                              f"More Details:\n{error_message}")))

                    sys.exit()
                    
                except Exception as Message:
                    print(Message)

                quit()

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
