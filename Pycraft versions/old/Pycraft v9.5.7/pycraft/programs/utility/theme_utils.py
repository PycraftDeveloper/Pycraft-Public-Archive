if __name__ != "__main__":
    try:
        from registry_utils import Registry
        
        import input_utility
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
            
    class determine_theme_colours(Registry):
        def __init__(self):
            pass

        def get_colors():
            if Registry.theme == "dark":
                Registry.font_color = Registry.themeArray[0][0]
                Registry.background_color = Registry.themeArray[0][1]
                Registry.shape_color = Registry.themeArray[0][2]
                Registry.accent_color = Registry.themeArray[0][3]
                Registry.secondary_font_color = Registry.themeArray[0][4]

            elif Registry.theme == "light":
                Registry.font_color = Registry.themeArray[1][0]
                Registry.background_color = Registry.themeArray[1][1]
                Registry.shape_color = Registry.themeArray[1][2]
                Registry.accent_color = Registry.themeArray[1][3]
                Registry.secondary_font_color = Registry.themeArray[1][4]

            elif Registry.theme == "custom" and not Registry.custom_theme is None:
                for i in range(len(list(Registry.custom_theme))):
                    argument = str(Registry.custom_theme[list(Registry.custom_theme)[i]])
                    input_result = input_utility.identify_patterns.identify_rgb(argument)
                    if input_result is False:
                        input_result = input_utility.identify_patterns.identify_hex(argument[1:-1])
                        if input_result is False:
                            input_result = input_utility.identify_patterns.identify_text(argument, Registry.colour_presets)
                            if not input_result is False:
                                setattr(Registry, list(Registry.custom_theme)[i], input_result)
                        else:
                            setattr(Registry, list(Registry.custom_theme)[i], input_result)
                    else:
                        setattr(Registry, list(Registry.custom_theme)[i], input_result)
                
            else:
                Registry.font_color = Registry.themeArray[0][0]
                Registry.background_color = Registry.themeArray[0][1]
                Registry.shape_color = Registry.themeArray[0][2]
                Registry.accent_color = Registry.themeArray[0][3]
                Registry.secondary_font_color = Registry.themeArray[0][4]

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
