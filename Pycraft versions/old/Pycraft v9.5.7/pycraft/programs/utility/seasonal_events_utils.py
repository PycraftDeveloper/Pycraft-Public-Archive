if __name__ != "__main__":
    try:
        import date_utils
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
            
    class configure_seasonal_event:
        def __init__(self):
            pass

        def is_seasonal_event():
            date = str(date_utils.Date().get_time())
            if "-10-30" in date or "-10-31" in date:
                return "halloween"
            elif "-11-01" in date:
                return "anniversary"
            elif "-11-05" in date:
                return "bonfire_night"
            elif "-12-24" in date or "-12-25" in date:
                return "christmas"
            elif "-12-31" in date or "-01-01" in date:
                return "new_year"
            else:
                return None
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
